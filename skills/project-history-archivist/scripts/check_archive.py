#!/usr/bin/env python3
"""Check a normalized project-history ledger without pretending to verify sources.

Input: JSON object with a `conversations` array. Each item has `id`, `status`,
`turns`, `coverage`, and `gaps` as described in references/records.md.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


VALID_STATUS = {"full", "partial", "inaccessible"}
USER_ROLES = {"user"}
CODEX_ROLES = {"assistant", "codex"}
CHANGE_ACTIONS = {"created", "modified", "deleted", "renamed"}
COVERAGE_KEYS = (
    "first_turn_confirmed",
    "last_turn_confirmed",
    "prompts_inspected",
    "responses_inspected",
    "progress_inspected",
    "timestamps_checked",
)


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def check(data: object) -> tuple[dict[str, object], list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(data, dict) or not isinstance(data.get("conversations"), list):
        return {}, ["Root must be an object with a conversations array."], []
    conversations = data["conversations"]
    seen_ids: set[str] = set()
    changed_paths: set[str] = set()
    commits: set[str] = set()
    counts = {"full": 0, "partial": 0, "inaccessible": 0, "prompts": 0}

    for index, conversation in enumerate(conversations, 1):
        label = f"conversation {index}"
        if not isinstance(conversation, dict):
            errors.append(f"{label}: must be an object")
            continue
        cid = conversation.get("id")
        if not nonempty(cid):
            errors.append(f"{label}: missing nonempty id")
        elif cid in seen_ids:
            errors.append(f"{label}: duplicate id {cid}")
        else:
            seen_ids.add(cid)
            label = f"conversation {cid}"
        if not nonempty(conversation.get("title")):
            warnings.append(f"{label}: title unavailable; record a source or gap")
        status = conversation.get("status")
        if status not in VALID_STATUS:
            errors.append(f"{label}: status must be full, partial, or inaccessible")
        else:
            counts[status] += 1
        gaps = conversation.get("gaps", [])
        if not isinstance(gaps, list):
            errors.append(f"{label}: gaps must be an array")
            gaps = []
        if status != "full" and not any(nonempty(g) for g in gaps):
            errors.append(f"{label}: {status} status requires a named retrieval gap")

        coverage = conversation.get("coverage")
        if not isinstance(coverage, dict):
            errors.append(f"{label}: missing coverage object")
            coverage = {}
        for key in COVERAGE_KEYS:
            if key not in coverage:
                errors.append(f"{label}: coverage.{key} missing")
            elif not isinstance(coverage[key], bool):
                errors.append(f"{label}: coverage.{key} must be boolean")
            elif status == "full" and not coverage[key]:
                errors.append(f"{label}: full status conflicts with false coverage.{key}")

        turns = conversation.get("turns", [])
        if not isinstance(turns, list):
            errors.append(f"{label}: turns must be an array")
            turns = []
        if status == "full" and not turns:
            errors.append(f"{label}: full conversation has no turns")
        if status == "inaccessible" and turns:
            warnings.append(f"{label}: has turns but is marked inaccessible")
        user_count = codex_count = 0
        for turn_index, turn in enumerate(turns, 1):
            if not isinstance(turn, dict):
                errors.append(f"{label} turn {turn_index}: must be an object")
                continue
            role = turn.get("role")
            if role in USER_ROLES:
                user_count += 1
                counts["prompts"] += 1
            elif role in CODEX_ROLES:
                codex_count += 1
            if role in USER_ROLES | CODEX_ROLES and not (
                nonempty(turn.get("content")) or nonempty(turn.get("source_ref"))
            ):
                errors.append(f"{label} turn {turn_index}: missing content/source_ref")
            if role in USER_ROLES and not nonempty(turn.get("content")):
                warnings.append(f"{label} turn {turn_index}: original user prompt is not stored")
            if not nonempty(turn.get("source_ref")):
                warnings.append(f"{label} turn {turn_index}: no source locator")
        if status == "full" and (not user_count or not codex_count):
            warnings.append(f"{label}: full conversation lacks a user or Codex turn; verify source")

        events = conversation.get("events", [])
        if not isinstance(events, list):
            errors.append(f"{label}: events must be an array")
            events = []
        for event_index, event in enumerate(events, 1):
            if not isinstance(event, dict):
                errors.append(f"{label} event {event_index}: must be an object")
                continue
            if event.get("action") in CHANGE_ACTIONS and nonempty(event.get("path")):
                changed_paths.add(event["path"])
            if event.get("action") == "inspected_only" and event.get("changed") is True:
                errors.append(f"{label} event {event_index}: inspected_only cannot be changed")
            if nonempty(event.get("commit")) and nonempty(event.get("evidence_ref")):
                commits.add(event["commit"])
            if event.get("action") in CHANGE_ACTIONS and not nonempty(event.get("evidence_ref")):
                warnings.append(f"{label} event {event_index}: changed file lacks evidence_ref")

    summary: dict[str, object] = {
        "discovered": len(conversations),
        "full": counts["full"],
        "partial": counts["partial"],
        "inaccessible": counts["inaccessible"],
        "prompts_captured": counts["prompts"],
        "unique_changed_paths": len(changed_paths),
        "correlated_commits": len(commits),
    }
    if counts["full"] + counts["partial"] + counts["inaccessible"] != len(conversations):
        errors.append("Discovered conversations do not reconcile with retrieval statuses")
    return summary, errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=Path, help="Normalized JSON ledger")
    args = parser.parse_args()
    try:
        data = json.loads(args.ledger.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Cannot read ledger: {exc}", file=sys.stderr)
        return 2
    summary, errors, warnings = check(data)
    print(json.dumps(summary, indent=2))
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
