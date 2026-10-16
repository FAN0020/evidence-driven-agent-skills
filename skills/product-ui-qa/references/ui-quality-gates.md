# UI Quality Gates

Use these gates to plan implementation, prioritize defects, and decide whether user-facing work is complete. Apply only checks relevant to the product and change, but never waive a relevant P0 or P1 gate without reporting that completion is blocked.

## P0 — Release blockers

- **Outcome integrity:** The UI must not cause or conceal an incorrect irreversible result. Verify critical journeys against persisted authoritative state.
- **Data preservation:** Valid work survives navigation, refresh, retry, restart/resume, and recoverable failure.
- **Destructive-action safety:** Delete, overwrite, discard, send, pay, publish, confirm, revoke, and similar actions are deliberate, unambiguous, and resistant to rapid or duplicate submission. Test cancel, undo, confirmation, and idempotency where applicable.
- **Security and privacy:** Roles, direct routes, hidden-control bypass, errors, logs, and client state expose no unauthorized data, actions, or secrets.
- **Truthful system state:** Ready, saved, sent, confirmed, and success states reflect authoritative reality rather than optimistic animation. Force dependency failures.
- **Critical accessibility:** The core job is keyboard-operable, visibly focused, semantically exposed, and practically usable.
- **Failure recovery:** Timeouts, offline states, invalid responses, and dependency restarts do not strand users or silently corrupt work.

## P1 — Core product quality

- **Component necessity and sufficiency:** Every major visible component traces to the user's immediate goal, required decisions, information, actions, or system state. The screen contains neither unjustified UI nor harmful omissions caused by over-minimalism.
- **Identity boundaries:** Product/brand, organization/tenant, user, workspace/project, domain entity/content, environment, and demo/fixture data remain distinct.
- **Primary-action hierarchy:** Each material state has one visually dominant immediate action unless a deliberate peer choice is required.
- **Duplication:** Equivalent user intents, navigation, information, status, identity, and settings entry points are not repeated without a user benefit.
- **Semantic correctness:** Loading is not empty; partial is not success; retrying is not idle; offline is not ready. Status labels have testable meanings.
- **No fake affordances:** Everything that looks interactive works, and static content does not misleadingly look interactive.
- **Cross-screen consistency:** Equivalent controls, concepts, placement, and terminology are consistent across the product.
- **Journey coherence:** An unfamiliar user can identify where they are, what happened, what is required, what comes next, and whether they can safely go back.
- **Error prevention and recovery:** Invalid choices are constrained, errors are specific and plain, valid input is preserved, and reversible actions support undo where appropriate.

## P2 — Robustness

- Cover empty, first-use, populated, loading, slow, partial, error, retry, offline, disabled, filtered-no-result, success, and completed/archived states as applicable.
- Exercise realistic and extreme data rather than clean fixtures only.
- Check supported widths/heights, resize/orientation, overflow, sticky UI, virtual keyboard, zoom, and text scaling.
- Verify localization, date/number/unit formatting, content expansion, validation, and state preservation during language changes.
- Exercise refresh, history, deep links, duplicate tabs, copy/paste, repeated clicks, slow operations, and lost connections.
- Test double submit, repeated save/generate, stale state, conflicting tabs, and retry after uncertain outcomes.
- Verify immediate acknowledgement, useful progress, and resistance to frozen-looking operations or disruptive layout shifts.
- Verify visibility and operability by role, including direct routes; authorization must not be client-side only.
- Check labels, required/optional distinction, defaults, validation timing, error association, and preserved form input.
- Check 0/1/few/many/very-many density, pagination or virtualization, and hierarchy under real content.

## P3 — Polish and optimization

- Use canonical vocabulary, concise verbs, consistent capitalization, and no internal engineering jargon.
- Preserve one dominant purpose, intentional grouping, and clear primary/secondary/destructive distinctions.
- Support shortcuts, bulk actions, sensible defaults, and accelerators when repeated use warrants them.
- Use motion to communicate change, respect reduced-motion preferences, and never delay core work.
- Add branding or delight only after correctness, clarity, accessibility, and resilience.

## Reusable invariants

- Exactly one current route, view, or context is represented as active.
- Equivalent actions do not accidentally appear multiple times in one decision context.
- Status claims correspond to authoritative state.
- Recoverable failures preserve previously valid work.
- Destructive actions cannot be triggered accidentally through ambiguity or duplicate submission.
- Unknown, absent, zero, false, not applicable, and not yet collected remain distinct when the domain requires it.
- Language, viewport, route, or transient-state changes do not silently destroy work.
- Test, demo, and fixture content does not leak into production-facing UI.
- No control exists only because the backend exposes an operation; every control serves a user need.
- No screen is verified until its rendered result is inspected when the environment permits.

## Definition of done

- For every new screen or substantial redesign, the Component Necessity Gate ran before implementation and the rendered Component Necessity Audit ran afterward.
- All applicable P0 gates pass.
- All applicable P1 gates pass; no P1 defect is hidden behind green functional tests.
- Required P2 coverage ran, or each exception is explicitly documented.
- Relevant automated accessibility checks pass and manual critical-flow review is complete.
- Important rendered states and supported viewports have visual evidence or reviewed visual regression.
- Primary journeys ran end to end with production-like data.
- Semantic duplication, identity, terminology, and fixture-leakage audits are complete.
- A fresh adversarial review ran after implementation.
- Known limitations and deferred P2/P3 items are recorded.
- Completion is supported by evidence, not implementation intent.
