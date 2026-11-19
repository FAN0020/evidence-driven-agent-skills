---
name: repo-evolution-learning
description: Learn an existing repository through its architecture, Git evolution, feature history, and engineering decisions; turn commit-linked evidence into a staged learning path. Use for learning from a repo, not ordinary code review or implementation.
---

# Repo Evolution Learning

Help a learner understand how a repository works now, how it got there, and what engineering lessons its history supports. Optimize for useful understanding per unit of reading and model context, without losing the history needed to support the answer.

## Choose the learning lens

- **Architecture evolution:** Trace the whole repository's major phases, subsystems, interfaces, and turning points.
- **Feature evolution:** Trace one feature, symbol, or path through introduction, fixes, replacement, and current behavior. Follow renames and callers; do not assume the current path covers its entire history.
- **Own-project lessons:** Reconstruct a team's iterations, experiments, regressions, and validation, then extract reusable lessons and a next learning exercise.

These lenses can be combined. Establish the learner's baseline from the request or prior context, then select the smallest scope that answers it. If an existing audit gives the history, use it as an index and verify only claims that matter or remain unclear. For a full engineering retrospective or target-product transfer, use `software-history-lessons` where available; this skill adds learner sequencing and hands-on exercises.

## Collect evidence efficiently

1. Identify the authoritative repository and record the current branch, HEAD, status, remotes, and available refs. Keep repository investigation read-only unless separately authorized.
2. Build a **complete inventory of the scoped accessible history** before selecting commits to inspect. Local Git CLI is usually efficient; a GitHub connector can serve a remote or private repository when local history is unavailable. Account for branches, merges, tags, deleted paths, and incomplete clones when material. State the visibility limit.
3. For local Git, optionally run `python3 scripts/history_index.py --repo /absolute/path/to/repo --max-candidates 30 [--path path/prefix]`. It prints a bounded ranking from commit metadata and touched paths; `--json-out /path/index.json` saves the full inventory only when a durable index is useful. Its scores are search aids, never evidence of importance or causality.
4. Cluster commits by actual subsystem, feature, or problem chain. Inspect a bounded set of decisive patches with `git show`, `git diff`, `git log --follow`, blame, source, tests, docs, issues, or CI as relevant. Expand a cluster when an apparent fix is later reverted, superseded, or contradicted. Do not feed every patch to the model by default.
5. Reuse a saved SHA inventory when revisiting the repository; compare with current reachable SHAs, then inspect new history and any older chains it changes. Do not treat cached interpretation as proof after refs or code have changed.

## Reconstruct rather than narrate commits

Start with a concise map of the **current** architecture so the learner knows where changes land. For each meaningful evolution chain, establish: prior behavior → observed problem or goal → change → measured or documented outcome → later fate or trade-off. Distinguish what code *does* from why someone *intended* it. Do not infer a proven performance gain from an optimization-looking diff. Attach commit SHA, path/symbol, test, log, issue, or release locator to material claims.

Label conclusions `OBSERVED`, `INFERENCE`, `RECOMMENDATION`, or `UNKNOWN`. Commit messages are leads, not proof; separate training/experiment hypotheses from measured results. Preserve failed attempts and constraints when they explain later choices. Do not force the project into a generic maturity ladder.

## Turn history into a learning path

Order lessons from system overview and prerequisites to concrete code paths, then to historical decisions and independent exercises. For each lesson give the one question it answers, minimum prerequisite, exact code/commit evidence to read, a short explanation, and a small exercise with a way to check understanding. Prefer a few high-yield checkpoints over exhaustive chronological reading; preserve an appendix or index for omitted scoped commits if completeness was requested.

Read [references/learning-output.md](references/learning-output.md) when producing a substantial learning guide or report. Match the user's requested format and language; do not create a file unless requested or needed for the deliverable.

## Finish with a coverage check

Confirm that key claims have locators, important alternatives/reversions are represented, current behavior is distinguished from historical experiments, and the learner can identify the next file, commit, or experiment to inspect. Record unresolved questions and what evidence would answer them.
