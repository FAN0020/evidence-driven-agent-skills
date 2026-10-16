# UI QA Summary Template

Keep the final report concise. Omit empty subsections only when the omission cannot hide an unperformed or failed gate.

## Scope reviewed

- Product area or feature:
- Operating mode: implementation / review only / implementation + verification
- Source of truth used:
- In scope:
- Out of scope:

## Coverage

- Screens, routes, views, or dialogs reviewed:
- Primary journeys executed:
- Important states and state-matrix combinations reviewed:
- Roles/permissions reviewed:
- Viewports/devices/browsers reviewed:
- Languages/locales reviewed:

## Findings

- **P0 — Release blockers:** None found / list each finding, evidence, disposition, and retest.
- **P1 — Core product quality:** None found / list each finding, evidence, disposition, and retest.
- **P2 — Robustness:** None found / list each finding, disposition, or explicit deferral.
- **P3 — Polish and optimization:** None found / list each finding or explicit deferral.

## Verification performed

- Pre-implementation Component Necessity Gate for new screens/substantial redesigns: Not applicable / decision trace and result.
- Post-render Component Necessity Audit: States inspected, findings, and disposition.
- Static checks:
- Unit/component tests:
- Interaction/E2E tests:
- Automated accessibility checks:
- Manual accessibility/mechanics review:
- Visual regression or screenshot review:
- Semantic/identity/duplication audit:
- Adversarial product review:
- Real-user usability testing: Not performed / participants and method. Never imply representative users participated when they did not.

## Results

- Defects found:
- Defects fixed:
- Relevant checks rerun:
- Remaining known limitations and residual risks:
- Evidence: commands/results, screenshots/artifacts, routes/states, or issue links.

## Final completion status

Choose one and explain briefly:

- **Complete:** Applicable P0/P1 gates pass; required evidence exists; deferrals are explicit.
- **Conditionally complete:** No known P0/P1 defect remains, but accepted P2 gaps or operational limitations remain.
- **Incomplete:** A P0/P1 gate fails, required rendered inspection or journey evidence is missing, or unresolved uncertainty prevents a truthful claim.

Use precise claims:

- Do not say “visually verified” unless the rendered UI was inspected.
- Do not say “accessible” or “compliant” solely because automation passed.
- Do not say “user validated” unless representative users actually participated.
- Do not say “complete” merely because functional tests passed.
