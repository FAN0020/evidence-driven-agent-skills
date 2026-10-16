# Risk-Based State Matrix

Use this method for important screens, routes, dialogs, panels, and decision contexts. A page name alone is not coverage evidence.

## 1. Enumerate applicable dimensions

- **Lifecycle:** first use, existing data, completed, archived.
- **Async:** idle, queued, processing, slow, partial, succeeded, failed, retrying, cancelled.
- **Data:** none, one, normal, maximum realistic, malformed, stale.
- **Connectivity:** online, degraded, offline, dependency unavailable.
- **Authorization:** allowed, read-only, forbidden, expired session.
- **Input:** pristine, partial, valid, invalid, corrected, unsaved.
- **Viewport:** each supported class, constrained height, resize/orientation, and 200% zoom or equivalent text scaling.
- **Language:** default, each supported locale where risk warrants, content expansion, and mixed-language content.

Add domain-specific dimensions when they affect behavior, such as plan/tier, workflow status, device capability, sync conflict, ownership, or feature flag.

## 2. Select combinations by risk

Do not build a full Cartesian product. Select combinations that expose distinct failure modes:

- Cover every P0/P1 transition and terminal state strongly.
- Pair failure states with unsaved or valuable work.
- Pair restrictive roles with direct routes and hidden-control bypass attempts.
- Pair slow/offline states with repeated actions, refresh, navigation, and retries.
- Pair maximum data with compact viewports, zoom, localization expansion, and long labels.
- Pair stale or conflicting state with multiple tabs or actors when applicable.
- Include ordinary happy paths so failures can be compared with expected behavior.

For each chosen case, record: entry conditions, user action, expected UI, authoritative-state expectation, recovery path, evidence, and result.

## 3. Use ugly data

Exercise applicable values and shapes:

- Empty values, null, zero, false, unknown, not applicable, not yet collected
- Very long and very short strings
- Unicode, multilingual content, right-to-left text when supported, and emoji
- Large lists, 0/1/few/many/very-many items, duplicate names, and near-identical records
- Long filenames, many attachments, large files, and mixed file types
- Malformed, stale, partial, contradictory, or delayed data
- Negative numbers, large magnitudes, boundary dates/times, long units, and locale-specific formats

Do not collapse these domain meanings unless the product explicitly does so:

- **UNKNOWN:** A value exists conceptually but is not known.
- **ABSENT:** No value or entity exists.
- **ZERO:** A known numeric value equals zero.
- **FALSE:** A known boolean value is false.
- **NOT APPLICABLE:** The concept does not apply in this context.
- **NOT YET COLLECTED:** The value may exist but has not been requested, received, or computed.

Verify display, filtering, sorting, validation, analytics, persistence, export, and assistive semantics preserve these distinctions where relevant.

## 4. Collect rendered evidence

For substantial UI work, retain screenshots or visual-regression artifacts for important states and viewports. Include enough surrounding context to judge hierarchy, identity, status, and action placement. A DOM snapshot or test log is not visual evidence unless the rendered result was inspected.
