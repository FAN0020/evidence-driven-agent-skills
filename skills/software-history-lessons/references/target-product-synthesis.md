# Target Product Synthesis

Use this reference for Mode C after distilling the source-project experience.

## Reasoning chain

For every historical lesson used in a target-product decision, make the chain traceable:

```text
historical evidence
→ engineering lesson
→ relevance or mismatch to target requirements
→ recommended architecture or implementation
→ risks and trade-offs
→ validation strategy
```

Do not reproduce the old architecture by default. First identify the target product's users, boundaries, workflows, constraints, scale, data sensitivity, deployment context, platform needs, operational model, and success criteria. Missing target facts become explicit assumptions or `UNKNOWN`, not invented requirements.

## Decision classes

Label each material target decision:

- `DIRECT REUSE` — source code or a module can reasonably transfer. Require compatible responsibilities, interfaces, data semantics, dependencies, security posture, operating environment, ownership/licensing, and testability. State adaptation work.
- `PATTERN REUSE` — the architectural or design pattern fits, but the old code should not be copied.
- `EXPERIENCE REUSE` — the historical lesson informs a decision, validation gate, sequencing choice, or risk control without reusing code or architecture.
- `AVOID` — a historical approach should not be repeated under the target's comparable conditions. State the evidence and conditions.
- `NEW REQUIREMENT` — the target needs something the historical project did not cover; design it from current requirements and do not imply historical validation.

Historical similarity is not enough for direct reuse. Evaluate fit at the technical boundary.

## Build recommendation

Cover only relevant topics, with concrete decisions and alternatives where uncertainty matters:

- product scope, non-goals, and system boundaries;
- architecture and subsystem ownership;
- key data flows, contracts, state, persistence, and migration;
- AI/model/provider and RAG/retrieval boundaries;
- deterministic responsibilities versus AI responsibilities;
- validation, grounding, provenance, privacy, and safety boundaries;
- concurrency, backpressure, resource management, cancellation, and lifecycle;
- error handling, retries, fallbacks, and recovery;
- UI/workflow and client/server boundaries;
- local versus cloud execution, deployment, runtime, packaging, and cross-platform concerns;
- testing layers, evaluation cases/metrics, and release gates;
- observability and debugging affordances;
- direct-reuse and migration plan;
- implementation phases, dependencies, and exit criteria;
- major risks, mitigations, and validation gates.

Do not include a topic merely because it existed in the previous project.

## Traceability table

For each proposed decision, retain:

1. decision ID and class;
2. target requirement or constraint;
3. source evidence and distilled lesson IDs;
4. fit analysis, including mismatches;
5. recommendation and rejected alternative when useful;
6. risks and trade-offs;
7. validation method and pass/fail gate;
8. confidence and open question.

Recommendations based only on target requirements should cite those requirements and use `NEW REQUIREMENT`, not force a historical link.

## Implementation phases

Sequence work to retire the largest uncertainties early. A phase should state objective, included subsystems, historical lessons used, deliverable, tests/evaluation, risk retired, and an observable exit gate. Keep proof-of-concept code separate from production architecture unless it meets the production boundary.

## Synthesis quality gate

The recommendation is complete when a reader can distinguish historical fact from generalized lesson and proposed design, see why each relevant old lesson does or does not fit, understand what is genuinely reusable, identify uncovered requirements, and validate each phase before expanding scope.
