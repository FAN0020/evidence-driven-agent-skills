# Durable Experience Document

Use this reference when project experience should be preserved for retrieval, future project work, interviews, or a target-product build decision.

## Artifact choice

Prefer a structured DOCX when the user asks to document, package, preserve, learn from, or turn history into reusable knowledge; asks how another product should be built from accumulated experience; or asks for a document/file. An explicit DOCX request overrides chat-first output.

Use the available document-generation workflow. Create the DOCX outside a repository unless the user authorized a repository path. Render it to page images, inspect every page at normal reading size, correct layout defects, and rerender before delivery. Do not provide QA images unless requested.

When DOCX creation is unavailable, provide the same structure in chat and state the limitation. When a DOCX is created, keep chat concise and link the artifact instead of duplicating its full content.

## Design for future retrieval

The document is a durable knowledge artifact, not a conversation transcript. Include enough project identity, date/scope, evidence basis, terminology, assumptions, provenance, and target context to remain useful months later without the original conversation.

Use stable identifiers for important lessons, evidence items, decisions, and risks when cross-references improve retrieval. Keep `OBSERVED`, `INFERENCE`, `RECOMMENDATION`, and `UNKNOWN` visually and semantically distinct. Historical claims retain evidence locators; target recommendations retain lesson/requirement traceability.

## Adaptive structure

Select relevant sections rather than mechanically including all of them:

1. Project and audit context
2. Executive engineering summary
3. Development journey
4. Architecture evolution
5. Major architectural turning points
6. Important bug to root-cause to fix chains
7. Testing evolution
8. Evaluation evolution
9. AI, model, provider, and RAG lessons
10. UI and UX lessons
11. Deployment, runtime, packaging, and platform lessons
12. Failed or superseded approaches
13. Reusable code
14. Reusable architectural patterns
15. Reusable engineering lessons
16. Approaches to avoid
17. Interview-ready engineering stories
18. Implications for the target product
19. Recommended target architecture and data flow
20. Recommended implementation phases and validation gates
21. Risks, trade-offs, unknowns, and validation strategy
22. Concise experience cheat sheet

For Mode A, include or append a complete scoped commit inventory and repository-state verification. For Mode B, avoid repeating a long audit when concise provenance plus distilled lessons is sufficient. For Mode C, emphasize the evidence-to-lesson-to-target decision chain and the five decision classes.

## High-value compact views

Use tables only where comparison benefits from a repeated schema. Useful views include:

- phase → problem → implementation → issue → response → validation → product gain → lesson;
- evidence → lesson → transfer conditions → reuse class;
- bug/symptom → root cause → fix → regression protection → lesson;
- target requirement → decision class → recommendation → evidence/lesson → risk → validation gate;
- implementation phase → deliverable → dependency → risk retired → exit gate.

Keep long reasoning in prose. Avoid dense tables that merely place paragraphs into cells.

## Content rules

- Adapt coverage to the actual project and target; omit irrelevant AI, UI, deployment, or cross-platform sections.
- Explain what evaluations and tests do **not** prove.
- Distinguish line counts and churn as context, not productivity measures.
- Preserve removed approaches and negative knowledge.
- Do not fabricate motivation, personal authorship, business outcomes, or validation.
- End with a concise cheat sheet and unresolved questions; include interview material only when useful to the request.

## Delivery

Name the file descriptively, for example `<project>-engineering-experience.docx` or `<source>-to-<target>-build-recommendation.docx`. Deliver the final verified DOCX only, unless the user asks for working files or alternate formats.
