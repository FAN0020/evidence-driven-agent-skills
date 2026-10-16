# DOCX report specification

The final artifact is one professional DOCX. Choose section breaks and table layouts based on actual volume; do not squeeze dense evidence into unreadable columns. Preserve technical detail in the conversation archive while keeping cross-project summaries concise.

## Required reading order

1. **Cover and document control:** project name, repository/path, covered period, generated/as-of date and timezone, branches/worktrees as known, evidence sources, discovered/full/partial/inaccessible counts, limitations, and count definitions.
2. **Table of contents:** actual heading styles (Heading 1–3) and a Word-compatible TOC field. Include automatic page numbers in the footer, a meaningful running header, and bookmarks for index targets. If field results are stale in a headless render, set fields to update on open and disclose that page references require Word refresh; do not type invented numbers.
3. **Executive project summary and timeline:** project purpose, real phases, architecture evolution, major implemented features, bugs, current status, unresolved issues. Timeline columns may cover date/time, conversation, goal, work, result, and Git/file evidence. Derive phases from evidence, not a stock lifecycle.
4. **Conversation-by-conversation archive:** one dedicated section for every relevant conversation in chronological order. Keep conversation ID/title, start/last activity, branch/worktree/commit context, and primary objective. Include a substantive summary, every substantive user prompt in sequence (original text and timestamp when available), substantive Codex replies and progress/actions, inspected versus changed files, commands/tests with observed results, decisions, problems/failed attempts, outcome, and remaining work. Mark absent timestamps or missing spans `UNKNOWN`. Use evidence locators for claims.
5. **Cross-conversation analysis:** feature evolution matrix; file/module evolution; architecture (initial, implemented, modified, abandoned/reverted, current); issue-resolution chains; decision log; testing history; and Git/branch/worktree correlation. Keep continued, repeated, superseded, and reverted work distinct.
6. **Current project state:** separately classify implemented, partially implemented, known problems, superseded/reverted work, current architecture, latest verified test status, and recommendations that follow from unfinished work. Do not present historical behavior as current. State as-of revision/time and evidence limits.
7. **Appendices:** conversation index, file index, commit index when commits exist, test/command index, and unresolved retrieval gaps. Indices should link/bookmark entries and use real field-based page references where possible. Omit a commit index only when no commits were available and say why.

## Conversation section pattern

Use a heading such as `Conversation 17 — [actual title]`, then a compact metadata block. For each prompt, identify its ordinal and actual timestamp or `Time unknown`; reproduce its substantive original text. For each corresponding Codex segment, preserve technical conclusions, progress, implementation, failures, command/test outcomes, and final status. A compact table can list `Path | Action | Purpose | Evidence`; action values distinguish `Created`, `Modified`, `Deleted`, `Renamed`, and `Inspected only`. A separate table can list `Command or test | Result | Evidence`. Avoid sprawling narrative in narrow cells.

## Format and verification

Use professional typography, consistent dates/timezones, reasonable margins and line spacing, keep-with-next headings, repeating table headers, sensible widths, and selective landscape pages for genuinely wide matrices. Use monospaced text for paths, commands, hashes, IDs, and symbols. Keep section/page breaks deliberate without large blank areas. Add hyperlinks and cross-references when useful. Ensure no placeholder text remains.

Render every page to an image and inspect at readable zoom. Check clipping, overflow, wrapping, table splits, missing glyphs, header/footer placement, and density. Validate the DOCX opens and contains TOC, page number, heading, and index structures. Compare high-impact report claims against ledger and repository evidence after composition. Include a visible retrieval-coverage statement and exact unresolved gaps; never make missing information look complete.
