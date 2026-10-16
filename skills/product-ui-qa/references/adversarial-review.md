# Final Two-Pass Review

Run this after implementation and relevant automated checks. The two passes have different goals; do not merge them into a single confirmatory review.

## Pass A — Verification

Confirm the implementation against external authority and observable behavior:

1. Freeze the applicable source-of-truth requirements, product model, supported platforms, roles, primary journeys, terminology, and known limitations.
2. Map requirements to user journeys, UI states, implementation locations, and evidence.
3. Run the selected static, unit/component, interaction/E2E, accessibility, and visual-regression checks.
4. Exercise the risk-based state matrix, including valuable unsaved work, failure recovery, roles, realistic data, and supported viewports/languages.
5. Inspect the rendered product for important states and confirm persisted or authoritative outcomes.
6. Record failures, fixes, reruns, deferred gates, residual risk, and evidence.

Pass A succeeds only when applicable P0/P1 gates pass and the reported completion status matches the evidence.

## Pass B — Adversarial product review

Act as a fresh reviewer who did not build the interface. Assume defects may exist and try to disprove completion. Review the composed product and full journeys rather than defending implementation choices.

First run the rendered [Component Necessity Audit](component-necessity-and-minimal-ui.md). Confirm that each major component still traces to the user's immediate goal and that the result is sufficient rather than merely sparse. Then continue with the semantic and journey challenges below.

Repeatedly ask:

1. What is the user's goal here?
2. What should they notice first?
3. What is the immediate primary action?
4. Are multiple controls serving the same intent?
5. Is every visible element necessary?
6. Does every element represent the correct concept and identity layer?
7. Does anything look interactive but is not?
8. Does anything work but communicate the wrong meaning?
9. What happens when data is empty, huge, missing, slow, stale, invalid, or unavailable?
10. What happens after refresh, retry, interruption, failure, cancellation, or duplicate submission?
11. Does this make sense to someone unfamiliar with the implementation?
12. Does the rendered product match the actual source of truth rather than merely the current code?

Actively hunt for unnecessary elements, duplicate actions/information/navigation/status, misleading labels, identity leakage, terminology drift, fake affordances, broken hierarchy, strange workflow decisions, inconsistent or missing states, visual defects, accessibility defects, fixture/demo leakage, and specification drift.

Perform the [semantic UI audit](semantic-ui-audit.md), including its distinct remove-one-thing pass after the Component Necessity Audit. Preserve elements that genuinely improve comprehension, safety, navigation, trust, recovery, or efficiency.

## Completion decision

- **Complete:** All applicable P0/P1 gates pass; required evidence exists; P2/P3 deferrals and limitations are explicit.
- **Conditionally complete:** No known P0/P1 issue remains, but explicitly accepted P2 coverage gaps or operational limitations remain.
- **Incomplete:** A relevant P0/P1 gate fails, rendered inspection required by the task was not performed, the core journey is not evidence-backed, or unresolved uncertainty prevents a truthful completion claim.
