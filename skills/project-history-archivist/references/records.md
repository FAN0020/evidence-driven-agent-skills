# Durable records and evidence

Use JSON, JSONL, or a small database in a task-local directory. This schema is a guide, not a mandate to lose fields supplied by a richer source. Preserve a source snapshot or locator for auditability, but avoid copying unrelated secrets or attachments into the archive.

## Inventory and conversation record

Each relevant or candidate conversation should carry:

- `id`, `title`, `project_id`/repository association and its basis, discovery source(s), and inclusion decision;
- creation/start/last-activity time when exposed, timezone, and time confidence;
- source coverage: discovered, opened, first/last turn confirmed, prompt history, response history, progress/folded content, timestamp availability, files extracted, Git correlated;
- status: `full`, `partial`, `inaccessible`, or `excluded`, with explicit gap/reason for non-full status;
- ordered `turns[]`: role, content or source-preserving reference, timestamp, source locator, truncation/attachment state;
- ordered `events[]`: type, claimed action, proposed/implemented/verified state, affected path(s), command/result, decision/problem relation, evidence IDs;
- branch/worktree/commit context, continuation/supersession relations, outcomes, and unresolved items.

One conversation can contain many user prompts and many Codex responses. Preserve their sequence rather than forcing one prompt to one response. Keep original prompt text in the record and report. If response material is prohibitively long, the report may present a faithful detailed account plus locators, but the source or raw snapshot must remain available and the report must clearly say what was condensed. Retain actual substantive Codex replies where feasible, especially final answers and technical conclusions.

## Evidence objects

Every material claim should point to one or more locators such as conversation ID/turn, local session path plus event offset, commit hash, diff path, source path/line, test log path/line, artifact, or UI state. Record `source_kind`, retrieval time, claim, and classification:

- `OBSERVED`: a directly retrieved statement or state. When the observed item is a conversation assertion, identify it as a **claim by the speaker**, not independently proven implementation.
- `CORROBORATED`: independently supported by two or more sources, typically conversation plus Git diff, source, or test output.
- `INFERRED`: reasoned from surrounding evidence; explain the inference.
- `UNKNOWN`: unavailable or unresolved. Do not fill with plausible details.

Use separate fields for `actor` (user/Codex/Git/other), `action_status` (`requested`, `proposed`, `attempted`, `implemented`, `verified`, `failed`, `reverted`, `unknown`), and `verification_status`. A file may be `inspected_only` in one conversation and modified in another; scope change labels to the event. Maintain both historical and as-of-current file states. Preserve conflicts as parallel evidence with a contradiction note, not a silent choice.

## Count definitions

`discovered`: unique relevant conversation IDs in scope, including inaccessible ones. `full`: beginning-to-end turn history and available progress inspected. `partial`: some content retrieved but at least one span/section unavailable. `inaccessible`: membership established but no substantive turn history. `prompt count`: substantive user prompts actually captured, not inferred. `changed-file count`: unique paths with evidence of create/modify/delete/rename in the covered history; exclude inspected-only paths. `correlated commits`: unique hashes connected to at least one conversation with explicit evidence. Maintain these definitions in document control so the completion report is interpretable.

For large histories, create one persisted record per conversation and a ledger manifest. Checkpoint after each retrieval. Use source hashes/offsets where feasible to detect accidental changes or duplicate imports. Assemble the DOCX only after inventory reconciliation.

`scripts/check_archive.py` accepts a JSON object with a `conversations` array. Each entry needs `id`, `title`, `status`, `turns`, `events`, `gaps`, and a `coverage` object with Boolean `first_turn_confirmed`, `last_turn_confirmed`, `prompts_inspected`, `responses_inspected`, `progress_inspected`, and `timestamps_checked`. Each turn uses `role`, `content` or `source_ref`, and preferably both. Each file-change event uses `action` (`created`, `modified`, `deleted`, `renamed`, or `inspected_only`), `path`, and `evidence_ref`; a correlated commit additionally uses `commit`. The script checks reconciliation and prints counts, but it cannot determine whether a source was actually read or a claim is true. Run `python3 scripts/check_archive.py path/to/ledger.json` from the skill directory or use the script's absolute path.
