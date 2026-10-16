# Component Necessity and Minimum Sufficient UI

Use this framework for every new screen or substantial redesign across web, desktop, mobile, SaaS, enterprise, consumer, local-first, internal, workflow, and AI-enabled products. Apply it proportionally when reviewing or extending an existing screen.

The governing principle is **minimum sufficient UI**: every visible component must earn its place through concrete user value. Sparse UI is not an end in itself. Preserve anything genuinely necessary for task completion, comprehension, safety, trust, accessibility, navigation, or efficiency.

## Before implementation: Component Necessity Gate

Derive the interface in this order:

`USER + IMMEDIATE GOAL -> REQUIRED DECISIONS -> REQUIRED INFORMATION -> REQUIRED ACTIONS -> REQUIRED SYSTEM STATE -> UI COMPONENTS`

1. Identify the specific user and their immediate goal in this decision context.
2. Identify only the decisions the user must make now.
3. Identify the information needed to make those decisions.
4. Identify the actions needed to advance or complete the goal.
5. Identify system state that must be visible for truthful feedback, safety, recovery, or trust.
6. Only then choose UI components that provide those inputs, actions, and state.

Do not start from familiar page patterns, a component library, available backend fields, or the shape of the data model and then invent user-facing purposes for them. The gate passes when the proposed component set is traceable to the chain above, sufficient for the task, and free of known unjustified elements.

Keep the decision trace proportionate. A compact list or annotation is enough when it makes the reasoning inspectable; do not create process documentation that adds no value.

## Zero-Component Pass

Conceptually begin with an empty screen. Add components one by one only when they are necessary or materially useful for the user's task. Stop when the interface is sufficiently usable.

For each major component ask:

> Why must this be visible here, at this moment, for this user?

Classify it as one of:

- **Essential:** Required to accomplish the task.
- **Supporting:** Materially improves comprehension, efficiency, safety, or trust.
- **Contextual:** Useful only in particular states; reveal it conditionally.
- **Secondary:** Useful but not primary; move it to details, settings, or another secondary surface.
- **Redundant:** Duplicates an action, concept, navigation destination, status, or information; merge or remove it.
- **Implementation-driven:** Visible because the architecture or data model contains it; hide it unless users genuinely need it.
- **Decorative:** Provides no meaningful recognition or task value; normally remove it.
- **Unjustified:** Has no concrete user value; remove it.

Apply the removal test:

> Would removing this materially reduce task success, comprehension, safety, trust, navigation, or efficiency?

If not, remove, combine, demote, or conditionally reveal it. A component is not justified merely because it might be useful someday.

## Rules that govern the component set

### Screen space has a cost

Permanent UI needs stronger justification than conditional or secondary UI. Do not add an element merely because a plausible benefit can be imagined; establish a concrete benefit in the current user context.

### Data-model richness is not UI richness

Do not automatically expose IDs, versions, schemas, provenance, renderer or model details, internal states, or other implementation metadata. Preserve needed data internally while disclosing it at the appropriate level:

`Primary workflow -> Secondary/details -> Manager/admin -> Audit/debug -> Full backend data`

Hiding irrelevant information is not deleting it. Surface technical or administrative data in the primary workflow only when the current user needs it for a decision, action, safety, trust, or recovery.

### Prevent AI dashboardification

Do not automatically generate cards, text boxes, labels, badges, statistics, icon containers, navigation, side panels, explanatory or helper text, status indicators, metadata blocks, or multiple headings to make a screen look designed. Do not turn a workflow screen into a dashboard unless monitoring multiple independent dimensions is genuinely part of the user's task.

### One concept, one representation

Audit by user intent rather than literal labels. `New`, `Create`, `Add`, `+`, and `Create first...` may be the same action. Likewise, do not represent the same status, destination, information, or concept multiple times without a concrete benefit. Use the detailed action, navigation, information, and status checks in [semantic UI audit](semantic-ui-audit.md) rather than creating a second duplication inventory.

### Design for scale, not fixture size

Evaluate important selection, catalog, and list screens at approximately `0 -> 1 -> typical -> many -> extreme`. Check whether a design that works for eight objects still works for 50–100 or more. Use the data and viewport combinations in [state matrix](state-matrix.md) for verification; do not optimize only for demo-sized fixtures.

### Use progressive disclosure without harmful over-minimalism

Move secondary, technical, provenance, administrative, and audit information to appropriate secondary surfaces. Do not hide or remove content or controls when doing so would materially harm task completion, comprehension, safety, trust, accessibility, navigation, recovery, or efficiency. Contextual and secondary placement must remain discoverable when users need it.

## After rendering: Component Necessity Audit

Inspect the actual rendered product with browser, screenshot, or native-UI tools when available. Source code, DOM structure, and passing tests do not establish that the component set is appropriate.

For every major component and each important rendered state:

1. Reconnect it to the actual user and immediate goal.
2. Reapply its necessity classification and removal test.
3. Check whether visual hierarchy matches its importance.
4. Detect duplicate actions, information, navigation, status, or concepts by intent.
5. Detect implementation details or data-model structure leaking into the primary workflow.
6. Judge total information density and whether permanent elements deserve their screen cost.
7. Inspect `0`, `1`, typical, many, and extreme data where applicable.
8. Confirm accessibility and relevant loading, empty, partial, error, success, permission, and responsive states do not make essential UI unavailable or contextual UI permanent.

Resolve findings by removing, combining, demoting, conditionally revealing, or—when the screen is insufficient—adding what the task genuinely requires. Then run the existing Remove-One-Thing Pass in [semantic UI audit](semantic-ui-audit.md) as a distinct final challenge. The audit is complete only when the rendered component set is both necessary enough to avoid clutter and sufficient enough to support the user safely and effectively.
