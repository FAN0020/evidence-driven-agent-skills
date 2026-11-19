#!/usr/bin/env python3
"""Read-only, metadata-first inventory of all commits reachable from local refs."""

import argparse
import collections
import json
import math
from pathlib import Path
import re
import subprocess
import sys


SUBJECT_RULES = [
    ("revert", re.compile(r"\b(revert|rollback|backout)\b", re.I), 7),
    ("performance", re.compile(r"\b(optimi[sz]|speed|faster|latency|perf|cache|throughput|oom)\w*", re.I), 6),
    ("architecture", re.compile(r"\b(architect|refactor|migrat|restructur|redesign|rewrite)\w*", re.I), 6),
    ("fix", re.compile(r"\b(fix|bug|repair|regression|crash|correct)\w*", re.I), 5),
    ("feature", re.compile(r"\b(add|implement|introduc|support|feature|enable)\w*", re.I), 4),
    ("test", re.compile(r"\b(test|eval|benchmark|metric)\w*", re.I), 3),
    ("docs", re.compile(r"\b(doc|readme|comment)\w*", re.I), 1),
]


def git(repo, *args):
    result = subprocess.run(
        ["git", "-C", str(repo), "-c", "core.quotePath=false", *args],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "git command failed")
    return result.stdout


def classify(subject, files, parent_count, focus):
    category, base = "other", 1
    for label, pattern, weight in SUBJECT_RULES:
        if pattern.search(subject):
            category, base = label, weight
            break
    if parent_count > 1:
        category, base = "merge", max(base, 2)
    score = base + min(3, math.floor(math.log2(len(files) + 1)))
    if focus and any(path == focus or path.startswith(focus + "/") for path in files):
        score += 8
    return category, score


def inventory(repo, focus):
    raw = git(repo, "log", "--all", "--format=%x1e%H%x1f%aI%x1f%s%x1f%P", "--name-only")
    commits = []
    for record in raw.split("\x1e"):
        if not record.strip():
            continue
        lines = record.strip("\n").splitlines()
        header = lines[0].split("\x1f")
        if len(header) != 4:
            raise RuntimeError("Unexpected git log record format")
        sha, date, subject, parents = header
        files = [line for line in lines[1:] if line]
        category, score = classify(subject, files, len(parents.split()), focus)
        commits.append({
            "sha": sha, "date": date, "subject": subject, "parents": parents.split(),
            "files": files, "category": category, "score": score,
        })
    return commits


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path, help="Local Git repository")
    parser.add_argument("--path", default="", help="Relative path to prioritize, without filtering history")
    parser.add_argument("--max-candidates", type=int, default=30)
    parser.add_argument("--json-out", type=Path, help="Optional full inventory cache outside the repo")
    args = parser.parse_args()
    if args.max_candidates < 0:
        parser.error("--max-candidates must be nonnegative")
    try:
        repo = Path(git(args.repo, "rev-parse", "--show-toplevel").strip()).resolve()
        focus = args.path.strip("/")
        commits = inventory(repo, focus)
        refs = git(repo, "for-each-ref", "--format=%(refname)").splitlines()
        shallow = git(repo, "rev-parse", "--is-shallow-repository").strip() == "true"
        if args.json_out:
            target = args.json_out.resolve()
            if target == repo or repo in target.parents:
                parser.error("--json-out must be outside the analyzed repository")
            target.write_text(json.dumps({
                "repo": str(repo), "shallow": shallow, "refs": refs,
                "focus": focus, "commits": commits,
            }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"Saved full inventory: {target}")
        counts = collections.Counter(commit["category"] for commit in commits)
        print(f"Repository: {repo}")
        print(f"Reachable commits: {len(commits)} | refs: {len(refs)} | shallow: {shallow}")
        print("Heuristic categories: " + ", ".join(f"{key}={counts[key]}" for key in sorted(counts)))
        print("Candidate commits (metadata ranking only; inspect patches before drawing conclusions):")
        for commit in sorted(commits, key=lambda item: (-item["score"], item["date"], item["sha"]))[:args.max_candidates]:
            print(f'{commit["score"]:2} {commit["sha"][:12]} {commit["date"][:10]} '
                  f'{commit["category"]:<12} {len(commit["files"]):3} files  {commit["subject"]}')
    except (RuntimeError, OSError) as exc:
        print(f"history_index: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
