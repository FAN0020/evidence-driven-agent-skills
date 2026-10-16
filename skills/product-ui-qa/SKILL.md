---
name: product-ui-qa
description: Implement, modify, review, test, or finalize user-facing product interfaces with risk-prioritized UI/UX quality gates and rendered-product evidence. Use for web, desktop, mobile, SaaS, local-first, enterprise, consumer, AI-enabled, internal-tool, and workflow products when work involves frontend implementation, UI refinement, UI/UX QA, demo or release readiness, post-architecture frontend validation, or deciding whether an interface is actually complete.
---

# Product UI QA

Treat functional correctness as necessary but insufficient. A user-facing implementation is complete only when the applicable quality gates pass, materially different rendered states and primary journeys have been exercised, and the result has survived a fresh adversarial review.

Use **minimum sufficient UI** as the governing principle: every visible component must earn its place through concrete user value. Minimalism is not the objective; preserve anything necessary for task completion, comprehension, safety, trust, accessibility, navigation, or efficiency.

## Select the operating mode

- **Implementation:** Apply the gates while building so defects are prevented. Verify at a level proportional to risk and scope.
- **Review only:** Do not modify the product unless the user authorizes changes. Return prioritized findings, evidence, and recommended corrections.
- **Implementation + verification:** Implement the scoped work, fix discovered P0/P1 defects that are within scope, rerun affected checks, and report residual P2/P3 items or limitations.

## Preserve traceability

Establish the applicable source of truth before judging the current UI. Use this chain:

`SOURCE OF TRUTH -> PRODUCT MODEL -> USER JOURNEY -> UI STATES -> IMPLEMENTATION -> VERIFICATION EVIDENCE`

Never reverse it into `CURRENT IMPLEMENTATION -> ASSUME THIS IS THE SPECIFICATION`. Record ambiguous or conflicting requirements instead of silently treating existing code as desired behavior.

## Derive components from user needs

For every new screen or substantial redesign, you must read [component necessity and minimum sufficient UI](references/component-necessity-and-minimal-ui.md) and run its Zero-Component Pass and Component Necessity Gate **before implementation**:

`USER + IMMEDIATE GOAL -> REQUIRED DECISIONS -> REQUIRED INFORMATION -> REQUIRED ACTIONS -> REQUIRED SYSTEM STATE -> UI COMPONENTS`

Do not begin with conventional components or the underlying data model and invent purposes for them afterward. Add components from an empty-screen baseline, classify their value, remove or demote unjustified elements, and stop when the interface is sufficiently usable. For review-only work, reconstruct this chain to test whether the existing component set is justified.

## Prioritize findings consistently

- **P0 — Release blocker:** Wrong outcome, data loss, security/privacy exposure, deceptive critical state, inaccessible core task, or inability to complete the core job. Must fix before release.
- **P1 — Core product quality:** Material comprehension, workflow, identity, hierarchy, consistency, recovery, or accessibility defect. Must fix before UI completion.
- **P2 — Robustness:** Edge states, responsive behavior, localization, realistic data, performance, permissions, concurrency, or cross-screen defect. Normally fix; document an explicit exception if deferred.
- **P3 — Polish and optimization:** Microcopy, density, motion, delight, minor visual refinement, or expert efficiency. May defer explicitly.

Read [UI quality gates](references/ui-quality-gates.md) before substantial implementation, release-readiness work, or a complete UI review.

## Build a risk-based state matrix

Do not verify only pages. For each important screen or decision context, select materially different combinations of lifecycle, async, data, connectivity, authorization, input, viewport, and language state. Strengthen coverage for P0/P1 behavior without testing a meaningless Cartesian product.

Read [state matrix](references/state-matrix.md) when planning fixtures, screenshots, interaction coverage, responsive/localized checks, or failure injection.

## Inspect the rendered product

When the environment permits, use browser or native-UI inspection tools and inspect the actual rendered application. Do not infer visual correctness solely from source code, DOM structure, passing tests, snapshots that were not reviewed, or implementation intent. For substantial UI work, capture or retain appropriate visual evidence for important states and viewports.

After implementation, rerun the framework as a **Component Necessity Audit** on the rendered product. Re-evaluate major components against the user goal, necessity, hierarchy, duplication, implementation leakage, information density, scale, accessibility, and relevant states. This post-render audit complements rather than replaces the existing Remove-One-Thing Pass.

If rendered inspection is impossible, say so, explain the resulting limitation, and do not claim visual verification or UI completion.

## Audit the interface as a coherent product

Evaluate applicable concerns across screens and journeys: outcome integrity, data preservation, destructive-action safety, security/privacy, truthful status, failure recovery, identity boundaries, primary-action hierarchy, duplicate intent, duplicate navigation/information/status, fake affordances, terminology, semantic correctness, cross-screen consistency, workflow coherence, empty/loading/partial/error/success states, realistic data, responsive/localized behavior, permissions, forms, density, perceived performance, visual hierarchy, microcopy, fixture leakage, specification drift, and AI-generated composition failures.

Read [semantic UI audit](references/semantic-ui-audit.md) for identity, action-intent, duplication, unnecessary-UI, journey, and AI-failure-mode review. Read [accessibility checklist](references/accessibility-checklist.md) for automated and manual accessibility coverage.

## Choose a proportional verification stack

Use the layers that materially reduce risk for the change:

1. Static checks
2. Unit/component tests
3. Interaction/E2E tests
4. Automated accessibility checks
5. Visual regression
6. Semantic UI audit
7. Manual accessibility and mechanics review
8. Adversarial product review
9. Real-user usability testing when consequential and appropriate

Do not mechanically require irrelevant layers. Do not call synthetic or agent review real-user research. Automated accessibility checks do not establish accessibility compliance by themselves.

## Coordinate without duplicating scope

Keep this skill focused on what should exist in the product UI, how it supports the user task, and whether the composed interface is product-quality. Use `frontend-ui-qa` for detailed frontend and design-system judgment, `playwright` for browser automation, `e2e-product-verification` for whole-system journeys, and `verification-before-completion` or `feature-verification-gate` for their broader verification responsibilities when applicable and available. Do not duplicate those workflows here.

## Finish with two passes

Run both passes after implementation:

1. **Pass A — Verification:** Check requirements, source-of-truth specifications, functional expectations, state coverage, accessibility expectations, and relevant automated tests.
2. **Pass B — Adversarial product review:** Approach the rendered product as a fresh reviewer who assumes unnecessary, duplicated, misleading, inconsistent, inaccessible, leaky, visually defective, or missing states may exist. Run the Component Necessity Audit, then the semantic audit and its separate Remove-One-Thing Pass. Try to disprove completion.

Read [adversarial review](references/adversarial-review.md) before the final pass. Complete its remove-one-thing review without sacrificing comprehension, safety, navigation, trust, or efficiency.

## Report only supported claims

Use [final QA report template](references/final-qa-report-template.md). Include scope, screens/routes, states, findings by priority, checks, accessibility, visual inspection, journeys, defects fixed, limitations, evidence, and final status.

Do not claim:

- UI completion merely because tests pass.
- Visual verification unless the rendered UI was inspected.
- Accessibility compliance solely from automated checks.
- Real-user usability validation unless representative users actually participated.
