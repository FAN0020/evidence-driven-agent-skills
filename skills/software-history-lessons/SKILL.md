---
name: software-history-lessons
description: Turn software repository history or an existing project audit into evidence-backed engineering lessons, then apply relevant lessons to future product architecture and implementation. Use for Git-history reconstruction, engineering retrospectives, experience documentation, or history-informed build recommendations; not for ordinary code review or generic architecture advice without historical evidence.
---

# Software History Lessons

Turn software-project history into durable engineering knowledge, then use only the relevant knowledge to inform future products.

## Route the request

Choose one or more modes before doing expensive work:

- **Mode A — Repository to Experience:** A Git repository is the primary evidence and the user wants the development journey reconstructed. Read [repository-forensics.md](references/repository-forensics.md), then [experience-distillation.md](references/experience-distillation.md).
- **Mode B — Audit to Experience:** The user supplies an audit, retrospective, architecture reconstruction, or history report. Read [experience-distillation.md](references/experience-distillation.md). Do not repeat Git reconstruction when the supplied evidence is sufficient unless verification is explicitly requested or a material claim cannot otherwise be supported.
- **Mode C — Experience to New Product:** Historical evidence and a target product, requirements set, design, architecture, or repository are both in scope. Read [experience-distillation.md](references/experience-distillation.md), then [target-product-synthesis.md](references/target-product-synthesis.md).

Modes compose. A repository plus a target product is A + C; a supplied audit plus target requirements is B + C.

At the start, decide:

1. Which evidence inputs are present?
2. Is Git reconstruction requested or needed?
3. Is a supplied audit sufficiently detailed for the requested conclusions?
4. Is reusable-experience distillation requested or implied?
5. Is a target-product recommendation requested?
6. Does the user request durable documentation or a file?

Ask only for missing inputs that prevent a material decision. Otherwise proceed and record gaps as `UNKNOWN`.

## Evidence discipline

Use these labels consistently:

- `OBSERVED` — directly supported by Git objects, source, tests, configuration, documentation, or supplied audit evidence.
- `INFERENCE` — a conclusion strongly suggested by evidence but not explicitly established.
- `RECOMMENDATION` — a proposed approach for the target product.
- `UNKNOWN` — the available evidence does not establish the point.

Attach useful locators to substantive claims: commit hash, path, symbol, test, configuration, release, audit section, or source page. Commit messages are leads, not proof. Never invent motivations, authorship, ownership, results, or validation. Do not turn a recommendation into a historical claim.

## Operating rules

- Discover the project's actual architecture, subsystems, phases, and important events. Do not impose a stock project structure or a prior project's architecture.
- Treat deleted, renamed, and superseded code as evidence. Separate authoritative source from generated, bundled, build, runtime, and evaluation artifacts.
- Keep repository investigation read-only unless the user separately authorizes a mutation. Capture repository state before and after Mode A and verify it is unchanged.
- Distill transfer conditions and failure boundaries, not merely a summary of events.
- Do not force an old solution onto unrelated target requirements. State historical relevance and mismatches explicitly.
- Scale work without sampling away canonical history. If the deliverable must be split, retain a complete inventory and clearly mark continuation boundaries.

## Durable output

Read [durable-document.md](references/durable-document.md) when the user asks to document, package, preserve, learn from, or reuse the experience; asks how another product should be built from it; or requests a file/DOCX. Prefer a structured DOCX for durable experience work. When the user explicitly asks for a DOCX or says to generate a file instead of a full answer, create the file, visually verify every rendered page with the available document workflow, and keep chat to a short description plus the file link.

For chat-only work, use the same evidence model and adaptive structure without reproducing irrelevant sections.

## Completion criteria

- **Mode A:** the scoped canonical history is completely inventoried and patch-inspected; merges, branches, renames, releases, generated artifacts, lineages, turning points, fix chains, tests/evaluation, removed approaches, and final repository state are handled where applicable.
- **Mode B:** transferable knowledge is separated into reusable code, patterns, experience, and approaches to avoid, with provenance and limits.
- **Mode C:** every historical lesson used is traced through target relevance to a recommendation, risk, and validation strategy; uncovered target needs are labeled `NEW REQUIREMENT`.
- **DOCX output:** the artifact is self-contained enough for later retrieval and has passed render-and-inspect QA.

## Invocation examples

- “Use software-history-lessons to reconstruct this project's engineering journey and package the experience into a DOCX.”
- “Use software-history-lessons on this repository and extract the most reusable engineering experience.”
- “This is the audit result. Use software-history-lessons to learn from it and generate a DOCX for future reference.”
- “Here is a previous audit and my new product requirements. Use software-history-lessons to recommend how the new product should be built.”
- “Use software-history-lessons to compare my current architecture with lessons from this previous project.”
