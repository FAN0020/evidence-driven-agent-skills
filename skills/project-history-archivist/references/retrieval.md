# Conversation and repository retrieval

## Establish membership

Use a saved project ID, repository root/remote, worktree origin, task project metadata, and explicit user scope as membership evidence. A title or summary match alone is insufficient. Keep possible matches in the ledger with `candidate` status until resolved. Include archived tasks and project chats where exposed. Deduplicate by stable conversation ID, retaining every discovery source. Do not assume a single list response is exhaustive: inspect pagination/cursors, limits, archived listings, and local index coverage. If an API provides only a bounded recency window, say so and seek another legitimate source.

Do not inspect unrelated private conversations merely to find a possible match. Use project metadata to narrow candidates first. Read-only access to local Codex session files may help when legitimately available; keep source paths, schema/version, and retrieval time. Do not alter local history storage.

## Retrieve complete conversations

Prefer a structured full-turn export or native history API. For every conversation, seek the first and last turn, then verify continuity of turn ordering and any pagination cursor. Capture role, original text, timestamp if exposed, attachment reference, tool/action result, progress/commentary, and source locator. Treat tool output truncation as a gap and recover from another source when possible. A concise `read_thread` response is useful for discovery but does not prove all user prompts or folded progress were retrieved.

When structured records omit information visible in the app, open the conversation and expand progress, tool, and collapsed sections. Scroll through the entire thread, including older content loaded on demand. Compare the UI against the structured record for representative turns and every identified truncation; use the UI to fill differences. If hundreds of records have reliable complete structured data, avoid redundant manual clicking.

Classify each segment's retrieval as `full`, `partial`, or `unavailable`. For a `full` conversation, verify all turns from first to last, not merely a nonempty result. Mark whether folded/progress material was available and inspected. If timestamps are absent in the underlying source, record that fact rather than estimating from a task's last-updated time.

## Repository corroboration

Capture current branch/worktree, `git status`, remotes, and relevant refs without mutating the checkout. Inspect full commit history needed for the covered period, including merges/branches and renames when relevant. Use diffs/file contents to establish what changed, when, and whether it remains present. Treat commit messages and conversation claims as leads; a verified diff or source file supports implementation, while test output supports verification. A current file proves current presence, not the original time of introduction. Capture exact commands and exit/results where accessible. If Git history is shallow, inaccessible, or incomplete, record that boundary.

For issues, keep the chain: symptom → diagnosis → proposed fix → implemented fix → verification → final status. Failed tests, retries, blockers, and abandoned approaches belong in the record. Never state that a command passed merely because a Codex response said it would be run.

## Recovery and stop condition

Persist each fetched conversation and its ledger update before moving on. On failure, retry with a bounded approach, inspect another authorized source, and continue other conversations. Record the failed source, attempted alternatives, and exact missing span. A report can be produced with partial coverage only if every gap is named in document control and the unresolved-gaps appendix; it must not claim a complete archive.
