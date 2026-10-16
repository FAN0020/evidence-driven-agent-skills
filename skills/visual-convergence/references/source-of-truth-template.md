# Visual source-of-truth template

Use this outline only when a project lacks a maintained visual specification. Remove sections that do not help the product and replace obsolete decisions instead of keeping conflicting alternatives.

```markdown
# Product visual source of truth

Status: approved | in review
Effective date: YYYY-MM-DD
Approved references: names or local links
Latest explicit preference: one sentence

## Visual goals
- Three to six perceptual qualities and the intended hierarchy.

## Preference evidence
| Preference | Confidence | Evidence | Durable rule? |
| --- | --- | --- | --- |
| Describe the preference | explicit / strongly evidenced / tentative inference / reference-specific artifact | User statement, repeated feedback, or reference observation | yes / no / pending |

Only explicit or repeatedly confirmed preferences should become durable rules. Remove disproven inferences instead of retaining them as history.

## Reference interpretation

### Invariants to preserve
- Hierarchy, atmosphere, palette relationships, density, visual weight, component language, typography character, and interaction emphasis that should transfer.

### Context-dependent adaptations
- Geometry, content quantity, viewport proportions, platform conventions, navigation structure, and responsive layout that should adapt to this product.

## Visual distribution model
| Property | Dominates | Supports | Attracts attention | Intentionally rare |
| --- | --- | --- | --- | --- |
| Color / typography / shadow / gradient / border / spacing / imagery / effects | | | | |

Describe relative dominance unless explicit measurements or percentages have been approved.

## Semantic tokens
| Role | Value | Usage |
| --- | --- | --- |

## Typography
- Families, scale, weights, line heights, and usage.

## Spacing, shape, and elevation
- Grid, gutters, spacing, radii, borders, and shadows.

## Component styling
- Primary action, secondary action, cards, inputs, navigation, overlays, and states.

## Gradient and imagery rules
- Approved coverage, opacity, placement, crops, and patterns to avoid.

## Accessibility
- Contrast targets, focus treatment, motion, and non-color state cues.

## Approved patterns
- Patterns future changes should preserve.

## Patterns to avoid
- Explicitly rejected patterns and the perceptual problem each creates.

## Current convergence audit
| Priority | Expected | Actual | Perceptual difference | Root cause | Proposed fix | Status |
| --- | --- | --- | --- | --- | --- | --- |
| P0 / P1 / P2 / P3 | | | | | | open / intentional / resolved |
```

Keep the audit limited to the active comparison. Once a preference becomes stable, fold it into the relevant rule and remove stale diagnostic rows.
