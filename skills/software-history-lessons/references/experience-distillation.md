# Experience Distillation

Use this reference after Mode A or directly for Mode B. The goal is transferable engineering knowledge, not a shorter audit.

## Check audit sufficiency

A supplied audit is sufficient when it supports the requested conclusions with identifiable evidence and gives enough context about chronology, architecture changes, important failures/fixes, validation, and current state. It need not follow a particular template.

Do not rerun expensive Git reconstruction merely to restate a sufficient audit. Verify Git only when the user asks, the audit conflicts internally, a high-impact claim lacks support, or the requested conclusion depends on missing patch-level facts. Otherwise mark gaps `UNKNOWN` and scope conclusions accordingly.

## Transform evidence into knowledge

For each important event or cluster, reason through:

```text
historical evidence
→ observed behavior or change
→ engineering lesson
→ transfer conditions and limits
→ reusable asset, pattern, experience, or warning
```

Extract only applicable categories:

- architecture and subsystem boundaries;
- implementation patterns and reusable components;
- debugging methods and bug/root-cause lessons;
- testing strategy and regression protection;
- evaluation methodology and limits of proof;
- AI/model/provider/RAG orchestration and safeguards;
- UI/UX and workflow lessons;
- deployment, packaging, local/cloud, runtime, and cross-platform lessons;
- concurrency, resource, cancellation, state, error-handling, and observability lessons;
- product iteration and sequencing lessons;
- approaches that worked, failed, or were superseded.

## Classify transferability

Keep these distinct:

- **Reusable code:** an identifiable module or implementation with a portable boundary. Record dependencies, assumptions, licensing/ownership constraints when known, required adaptation, and tests needed before reuse.
- **Reusable pattern:** a design or workflow that transfers even if the code does not.
- **Reusable experience:** a lesson, diagnostic technique, sequencing choice, or risk signal that informs decisions without copying design or code.
- **Avoid:** an approach whose demonstrated failure mode should not be repeated under similar conditions. State the conditions; do not universalize a local failure.

For each distilled item record:

1. evidence locator and evidence label;
2. historical context and observed outcome;
3. lesson stated at the right level of generality;
4. applicability conditions and counterconditions;
5. reuse class;
6. confidence and unresolved questions;
7. recommended validation before future adoption.

## Recover negative knowledge

Deleted or superseded code may preserve the most valuable lessons. Explain what the old approach did, its supported limitation, what replaced it, whether the replacement addressed the limitation, which trade-offs it introduced, and whether any useful idea was lost. Do not assume “newer” means “better” without validation evidence.

## Interview-ready stories

Create stories only when the evidence supports them. Avoid fabricating personal ownership, leadership, motivation, or results. Prefer neutral evidence-grounded framing such as “The repository history shows…”

A useful story contains: context, problem, initial approach, limitation, investigation evidence, technical solution, validation, result, lesson, interview framing, and evidence locators. Select the strongest stories rather than turning every commit into a story.

## Distillation quality gate

The result should let a future engineer answer:

- What should we reuse directly, and under what constraints?
- Which patterns are valuable even when the code is not?
- Which lessons change design, sequencing, debugging, or validation decisions?
- Which failures should be avoided in comparable conditions?
- What does the evidence not establish?

If it only retells the chronology, it is not yet an experience distillation.
