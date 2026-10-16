# Accessibility Checklist

Apply this checklist proportionally to the product, supported platforms, and risk. Use the project's stated accessibility target when one exists. Do not claim compliance from this checklist or automated scans alone.

## Automated checks

- Run the project's accessibility analyzer (for example axe or a platform equivalent) on important rendered states, not only the happy path.
- Check accessible names, roles, states, relationships, duplicate IDs, color contrast, landmarks, headings, labels, error associations, and hidden content.
- Treat zero automated violations as evidence for machine-detectable rules only.

## Keyboard and focus

- Complete each critical journey without a pointer.
- Verify logical focus order, visible focus, no traps, usable skip/navigation mechanisms, and predictable focus after route changes, dialogs, errors, deletion, and async completion.
- Ensure all interactive elements are reachable and operable; static elements are not inserted into the tab order without purpose.
- Confirm shortcuts do not conflict with text entry or platform/assistive-technology conventions.

## Semantics and communication

- Controls expose accurate names, roles, values, expanded/selected/pressed states, and descriptions.
- Headings, landmarks, lists, tables, forms, dialogs, alerts, progress, and status use appropriate semantics.
- Errors identify the affected field or action in text, explain recovery, and are programmatically associated where applicable.
- Dynamic changes are announced when needed without producing repetitive or disruptive output.
- Status does not rely on color, position, icon, motion, or sound alone.

## Visual and motor access

- Text and essential controls remain usable at 200% zoom or the platform-equivalent text-scaling target.
- Reflow avoids hidden actions, two-dimensional scrolling for ordinary content, overlap, clipping, and lost context where the platform supports reflow.
- Targets are practically sized and spaced; drag, hover, gesture, or fine-motor actions have accessible alternatives where applicable.
- Contrast remains sufficient in default, hover, focus, selected, disabled, error, and high-contrast/forced-color states when supported.
- Motion respects reduced-motion settings and never blocks core work.

## Media and platform mechanics

- Images and icons have appropriate alternatives; decorative media is ignored by assistive technology.
- Audio/video has the required captions, transcripts, descriptions, and controls for the product context.
- Native desktop/mobile controls follow platform accessibility APIs and conventions.
- Browser history, deep links, zoom, text scaling, orientation, virtual keyboard, and assistive-technology modes do not destroy state or hide essential actions.

## Evidence and claims

Record tools, versions when material, states/routes checked, manual workflows completed, assistive technologies used, defects found/fixed, and untested areas. Say “automated checks passed for these states” rather than “the product is accessible” unless a broader, appropriately qualified assessment supports that claim.
