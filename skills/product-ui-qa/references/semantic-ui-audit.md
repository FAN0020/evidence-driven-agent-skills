# Semantic UI Audit

Review the composed product, not isolated components. Compare related screens side by side and trace concepts back to the source of truth.

## Identity-boundary audit

Map every visible name, logo, avatar, badge, environment marker, and ownership label to exactly one layer:

1. Product / Brand
2. Organization / Tenant
3. User
4. Workspace / Project
5. Domain Entity / Content
6. Environment
7. Demo / Fixture Data

Check global chrome, titles, navigation, breadcrumbs, selectors, dialogs, exports, emails, notifications, and error text. Historical customer, demo, test, or fixture information must not become product-level identity unless intentional white-labeling is specified.

## Action-duplication audit

Inventory actions by **user intent**, target entity, scope, and effect—not by literal label. `New`, `Create`, `Add`, `+`, and `Create first…` may represent the same intent.

For each decision context:

- Identify the immediate user goal and one primary action unless a deliberate peer choice is required.
- Group controls that produce the same outcome, even when labels, icons, placement, or component implementations differ.
- Check headers, toolbars, empty states, menus, cards, floating controls, keyboard shortcuts, and context menus together.
- Remove or demote duplicates unless they materially improve reachability, efficiency, comprehension, or responsive access.
- Verify secondary and destructive actions have appropriate prominence and separation.

## Duplication and consistency audit

- **Navigation:** One current location; no competing route systems or redundant pathways presented as separate concepts.
- **Information:** Repeated summaries, headings, metadata, descriptions, or instructions add real value.
- **Status:** Multiple badges, banners, toasts, and labels agree and do not overstate certainty.
- **Terminology:** One canonical term per concept; labels and verbs remain consistent across screens.
- **Behavior:** Equivalent controls respond, validate, focus, and recover consistently.
- **Concept placement:** Identity, ownership, scope, and environment information appear where users expect them.

## Truth and affordance audit

- Every success, saved, ready, sent, confirmed, or completed claim maps to authoritative state.
- Loading, empty, partial, stale, retrying, offline, cancelled, and error are not collapsed into misleading equivalents.
- Everything that looks interactive works with pointer and keyboard where applicable.
- Disabled controls explain what blocks progress when the reason is not obvious.
- Decorative elements do not mimic controls, selection, progress, or status.
- Controls are not exposed merely because the backend provides an operation.

## Journey and cross-screen audit

Execute primary journeys from entry to persisted outcome as an unfamiliar user. At each step ask:

- Where am I, and which scope or entity am I acting on?
- What changed, and is that change authoritative?
- What must I do next?
- Can I safely go back, refresh, retry, or resume?
- Are terminology, hierarchy, status, and actions consistent with adjacent screens?
- Does the journey preserve valid work during interruption or failure?

## Remove-one-thing pass

For every major screen, ask what can be removed without reducing the user's ability to complete the task. Challenge repeated headings, unnecessary cards, duplicate CTAs, excessive badges, decorative status indicators, redundant helper text, duplicate navigation, unnecessary icons, and implementation-driven controls.

Do not remove an element merely for minimalism. Preserve anything that materially improves comprehension, safety, navigation, trust, recovery, or efficiency.

## AI-assisted implementation failure modes

- **Local correctness, global duplication:** Independently sensible components conflict or repeat when composed. Review at page, journey, and product levels.
- **Historical/demo leakage:** Old customer or fixture identity is treated as brand truth. Rebuild the identity map from authoritative sources.
- **Implementation as specification:** Current code is assumed to be desired behavior. Restore source-to-evidence traceability.
- **Happy-path fixation:** Generated tests cover intended paths but ignore state space. Add risk-based state matrices and failure injection.
- **Test-shaped UI:** Selectors and assertions pass while human comprehension is poor. Inspect the rendered product and walk it as an unfamiliar user.
- **Premature completion:** Green tests are mistaken for product verification. Run both final passes.
- **Synthetic confidence:** Agent review is represented as user research. State who or what actually participated.
- **Fixture blindness:** Clean short data hides density, truncation, and ambiguity. Maintain ugly-data fixtures.
- **Independent-component conflict:** Components use inconsistent terminology, state models, hierarchy, or interaction patterns when composed.
