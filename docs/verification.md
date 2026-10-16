# Publication verification

Checked **2026-10-16** on macOS with Python **3.14.7**. These results concern this distribution's structure, installation instructions, and archive helper. They do not establish the quality of an agent's UI judgment, historical analysis, or writing.

## Completed checks

| Check | Result | What it establishes |
| --- | --- | --- |
| Skill frontmatter and layout | 4/4 passed the local Codex `skill-creator` validator | Valid skill names, descriptions, and required entrypoints |
| Codex display metadata | 4/4 passed | Valid short-description lengths and explicit skill names in default prompts |
| Source-file preservation | Passed | All snapshotted files retain their recorded bytes except the documented archivist default-prompt addition and trailing blank-line cleanup in three UI references |
| Relative Markdown links and anchors | 89 resolved across collection documentation and the two README updates | Referenced local files and checked heading targets exist |
| Exact README installation snippet | Passed in a temporary `CODEX_HOME` | All four skill folders copy with byte-identical content |
| Existing-install protection | Passed | A second installation refuses existing destinations without overwriting them |
| Valid synthetic archive ledger | Exit 0 | One fully inspected and one explicitly inaccessible record reconcile structurally |
| False full-coverage flag | Exit 1 | A `full` record with an uninspected coverage field is rejected |
| Duplicate conversation ID | Exit 1 | Duplicate identifiers are rejected |
| Inaccessible record without a gap | Exit 1 | Missing retrieval-gap explanations are rejected |
| Malformed JSON | Exit 2 | Invalid input is reported separately from ledger errors |

The archive fixtures describe synthetic records, not a real project. An exit of zero permits explicitly documented partial/inaccessible coverage; it does not mean the archive is complete.

The public files were also reviewed for personal absolute paths, credential patterns, private project identifiers, and accidentally bundled source exports. Only skill instructions, supporting references, the checker, a synthetic example, metadata, and publication documentation are included. This was a bounded publication review, not a security certification.

## Reproduce the available checks

After cloning the collection, run its included synthetic example:

```sh
python3 skills/project-history-archivist/scripts/check_archive.py \
  skills/project-history-archivist/examples/ledger.json
git diff --check
```

For schema checks, use your host's `skill-creator` validator if available. The publication validator and temporary negative fixtures were run outside the distribution; they are not an additional runtime dependency. The helper uses the Python standard library. Its annotations require Python 3.10 or newer; the lower bound was not separately runtime-tested.

## Changes made for public packaging

- Added the collection README, four skill READMEs, inventory, comparison records, and this verification record.
- Added Codex UI metadata for Visual Convergence and a default prompt for Project History Archivist.
- Added a synthetic archive-ledger example and MIT license.
- Retained all four original `SKILL.md` files and the archive checker byte-for-byte; removed one trailing blank line from each of three UI references without changing their instructions.
- Updated the existing academic-skill README with sourced comparison and the profile README with five skill entries; neither update changes executable behavior.

## Not verified

- Controlled same-input, same-model comparisons with any other skill.
- Real-user usability outcomes, aesthetic superiority, or accessibility compliance.
- End-to-end archive generation and page rendering for a real project in this release.
- Availability or completeness of another user's conversation history.
- Runtime compatibility with every agent host or Python version.
- Re-execution of the separate academic repository's helper suite; this publication changes its README only.

The comparison documents therefore describe supported instruction-level mechanisms and task fit, not benchmark results.
