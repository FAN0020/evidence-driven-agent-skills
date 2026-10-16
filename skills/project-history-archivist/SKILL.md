---
name: project-history-archivist
description: Reconstruct a repository's complete accessible Codex conversation and development history into an evidence-traceable, professionally validated DOCX. Use for project history archives and engineering audit trails, not ordinary chat summaries or Git-only retrospectives.
---

# Project History Archivist

Produce **one DOCX** that lets a reader who did not participate in the project trace requests, investigations, changes, decisions, failures, verification, reversions, and current state. Completeness, chronology, and source traceability take priority over brevity. An archive is not complete because a DOCX exists; coverage and the rendered document must both pass review.

## Establish scope and inventory

1. Identify the current repository/project, its saved-project identity when exposed, its worktrees, and the report's as-of time. Preserve the starting Git state. Use the user's stated scope if supplied; otherwise include **every accessible Codex conversation associated with this project**, including archived tasks, related worktrees, renamed tasks, and relevant ChatGPT project conversations if exposed. Do not mix in unrelated conversations merely because they mention the project.
2. Enumerate the complete accessible set before writing the narrative. Use native Codex thread/project tools and pagination where available; inspect archived and active sets. Cross-check against legitimately accessible local session metadata and project identifiers. Treat UI summaries as discovery leads, not full conversation content. Read [retrieval.md](references/retrieval.md) for source selection, full-turn retrieval, folded progress, and recovery.
3. Start a durable ledger in a task-local workspace. Give each discovered conversation an ID, title, project-association reason, source locator, and retrieval state. Include inaccessible or ambiguous candidates with explicit dispositions. Keep raw export/source pointers and normalized records so work can resume after context loss. Read [records.md](references/records.md) before processing many conversations.
4. For **each** relevant conversation, retrieve all accessible turns from beginning to end, including every substantive user prompt, substantive Codex reply, progress/commentary, tool/action summary, error, and final response. Page backward until the beginning is confirmed. Expand folded UI sections when structured sources do not expose their contents. Do not assume a `read_thread` summary or the latest turns are complete. Record timestamp availability per turn and what progress content was checked.
5. Reconcile the inventory after retrieval: discovered = fully inspected + partially inspected + inaccessible, with stated reasons. If totals differ, continue retrieval. A partial conversation remains in the archive with its gap named; it is never silently dropped.

## Reconstruct the development record

- Preserve original substantive user prompts verbatim in the detailed archive whenever retrievable. For unusually long prompts, retain the full text there and add a short synopsis only as an aid. Preserve substantive Codex replies and intermediate progress in chronological order; clearly distinguish quotation/transcription from analysis.
- Extract concrete actions with evidence locators: files **inspected**, created, modified, deleted, or renamed; code and architecture changes; commands and actual results; tests and counts; branches, worktrees, commits, diffs, merges, rebases, and reversions; decisions with reasons; bugs and failed attempts; generated artifacts; remaining work. Never promote a proposal to implementation, an edit to verification, or an inspected file to a changed file.
- Correlate conversation claims with repository files, Git objects, logs, and artifacts. Git corroborates or contradicts conversations but cannot replace missing turns. Record contradictions explicitly. Distinguish `OBSERVED`, `CORROBORATED`, `INFERRED`, and `UNKNOWN`, with locators and the as-of state. See [records.md](references/records.md).
- Order events by exposed timestamps, preserving their original timezone and a consistently normalized time. When exact times are unavailable, use dated or relative ordering and mark uncertainty; never invent a timestamp. Track later work that continues, modifies, confirms, supersedes, or reverts earlier work. Separate historical state from current state.
- Work incrementally: discover → retrieve → normalize → extract → correlate → persist → reconcile → synthesize. Do not solve context limits by sampling away old conversations. On retrieval failure, retry reasonably, try another legitimate source, save the gap, and continue.

## Compose the report

Read [report.md](references/report.md) for required sections, per-conversation template, indices, and document rules. The report must contain a dedicated section for **every relevant conversation**, a chronological timeline, cross-conversation synthesis, and a separately evidenced current-state reconstruction. Summaries may remove repetition, but the chronological record must preserve each occurrence and its relation to later work.

Create the DOCX with the available document workflow (use the `documents` skill when installed). Use real Word heading styles, a Word-compatible TOC field, automatic footer page numbers, bookmarks/field-based page references rather than invented page numbers, readable tables, and clear monospaced paths/commands/identifiers. Render the finished DOCX to page images and visually inspect **every page**, then repair and re-render until it is readable. Validate the package and fields structurally as well as visually. Never label a report fully verified if any required check failed.

## Completion gate

- Reconcile ledger counts and check that each accessible conversation has its full prompt, response, progress, and timestamp availability recorded. The optional `scripts/check_archive.py` checks normalized-record invariants; inspect warnings rather than treating it as a substitute for source review.
- Cross-check high-impact file, commit, test, and current-state claims against repository/Git evidence. Document contradictions and unresolved retrieval gaps.
- Verify the DOCX opens, TOC and page-number fields exist, heading hierarchy and indices work, and every rendered page has acceptable layout. The TOC may require an update in Word; state this if its displayed numbers were not materialized. Never fabricate page references.
- Report the output DOCX path; discovered, fully and partially inspected conversation counts; covered date range; prompt count; changed-file count; correlated-commit count; retrieval gaps; and final validation status. Give truthful partial status if sources remain unavailable.

The archive must remain evidence-led even if that produces an explicit `UNKNOWN` or incomplete coverage.
