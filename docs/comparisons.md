# Comparison with related public skills

Reviewed **2026-10-16**. These are primary-source, workflow-level comparisons against the files linked below, pinned to the repository commits retrieved during review. Search results were used for discovery, not as proof of capabilities. The sample is intentionally bounded; it is not an exhaustive market survey.

We read the entrypoint instructions and relevant rule sources. A feature absent from the reviewed file is not proof that the entire competing ecosystem lacks it. The differences below explain task fit; they do not establish superior model output, lower cost, or a measured success rate. Competitor code is not redistributed.

## Product UI QA

- **Related sources:** [Vercel web-design-guidelines](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/web-design-guidelines/SKILL.md) and its [interface rules](https://github.com/vercel-labs/web-interface-guidelines/blob/434b7f91364665f2f733b310ec54809bf8f37937/command.md); [Anthropic webapp-testing](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/webapp-testing/SKILL.md).
- **Observed overlap:** Vercel reviews code for interface rules, including accessibility, state, copy, and interaction. Anthropic provides Playwright testing and server-lifecycle mechanics.
- **Local differentiation:** [component necessity](../skills/product-ui-qa/references/component-necessity-and-minimal-ui.md) starts with user decisions and derives the visible component set. The [state matrix](../skills/product-ui-qa/references/state-matrix.md) and [adversarial pass](../skills/product-ui-qa/references/adversarial-review.md) turn this into a product-completion workflow.
- **Advantage for a specific job:** useful when technical correctness conceals clutter, duplicated intent, implementation details, or missing recovery states.
- **Tradeoff:** substantially more judgment and runtime inspection than a terse file-level review; no bundled browser automation. The alternatives are useful complements.

## Visual Convergence

- **Related sources:** [Anthropic frontend-design](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design/SKILL.md); [Vercel web-design-guidelines](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/web-design-guidelines/SKILL.md).
- **Observed overlap:** frontend-design already addresses deliberate design, restraint, screenshots when available, and self-critique. It should not be described as lacking visual review.
- **Local differentiation:** [the workflow](../skills/visual-convergence/SKILL.md) explicitly separates preference confidence, project authority, token correctness, and perceptual correctness. It models the relative dominance of color, typography, surfaces, and decoration before changing values.
- **Advantage for a specific job:** well suited to an existing UI that follows nominal tokens but misses an approved reference's composition. Its project decision document keeps a local aesthetic out of the reusable skill.
- **Tradeoff:** assumes a direction worth converging toward. It does not provide a style catalog, image-diff engine, or proof of objective aesthetic superiority.

## Project History Archivist

- **Related sources:** [codex-chat-export](https://github.com/wimi321/codex-chat-export/blob/988f58148422fb186df2d5893740f8d3669a7330/SKILL.md); [session-synthesis](https://github.com/gfouillet/session-synthesis-skill/blob/83c0f1d1566255b2b668806373c73497f4c9f277/SKILL.md).
- **Observed overlap:** codex-chat-export produces Markdown/JSON transcripts with optional tool traces. Session-synthesis records session goals, results, and usage/cost telemetry, including retrospective reconstruction.
- **Local differentiation:** [the inventory and evidence model](../skills/project-history-archivist/references/records.md) accounts for every relevant discovered conversation, retains gaps, distinguishes historical claims from corroboration, and feeds a DOCX with current-state reconstruction.
- **Advantage for a specific job:** a project audit that needs to explain requests, failed attempts, changes, reversions, and verification across many conversations.
- **Tradeoff:** it relies on host retrieval and rendering tools; the exporter is more immediately executable for backup. A reconciled ledger can still contain unavailable history, and the helper cannot certify source truth.

## Software History Lessons

- **Related sources:** [Skill2Env game-postmortem](https://github.com/NVlabs/Skill2Env/blob/507eab4d9952968de2be98f8729d3c66d487285a/SkillHub/skills/game-postmortem/SKILL.md); [session-synthesis](https://github.com/gfouillet/session-synthesis-skill/blob/83c0f1d1566255b2b668806373c73497f4c9f277/SKILL.md).
- **Observed overlap:** game-postmortem already uses quantitative evidence, root-cause analysis, lessons, and future-project action items. Session-synthesis provides a durable session record.
- **Local differentiation:** [repository forensics](../skills/software-history-lessons/references/repository-forensics.md) asks for canonical patch inspection, merges, renames, and removed approaches. [Target synthesis](../skills/software-history-lessons/references/target-product-synthesis.md) maps each lesson through target relevance, reuse class, risk, and a validation gate; a sufficient supplied audit can skip reconstruction.
- **Advantage for a specific job:** moving from a previous project's evidence to a new product's architecture without copying assumptions blindly.
- **Tradeoff:** thorough history analysis can be costly. A milestone retrospective is more appropriate when the goal is immediate team actions rather than cross-product technical transfer.

## Adaptive Academic Note Architect — existing separate repository

- **Related sources:** [Jellypod lecture-to-study-guide](https://github.com/Jellypod-Inc/school-skills/blob/cd484795e924e454caafd13ddc25c1ec76c48718/skills/lecture-to-study-guide/SKILL.md); [GraceLiao77 lecture-to-summary-skills](https://github.com/GraceLiao77/lecture-to-summary-skills/blob/843284cc45336f2159af3f396a5a8130c994ebab/SKILL.md).
- **Observed overlap:** Jellypod organizes learning material into a study guide with a source-location glossary, examples, practice questions, and a cheat sheet. GraceLiao77 favors concise exam-oriented Markdown notes and delegated processing.
- **Local differentiation:** [the published skill](https://github.com/FAN0020/adaptive-academic-note-architect) targets recoverable source coverage, conceptual reconstruction, bilingual terminology, visible takeaways, incremental formatting protection, and final rendered pagination. Its extraction and DOCX helpers handle deterministic work separately from semantic judgment.
- **Advantage for a specific job:** comprehensive long-form lecture reconstruction with explicit corrections, source attribution, and navigable document output.
- **Tradeoff:** needs document/OCR/visual tools according to the inputs; it is heavier than exam revision and does not make practice-question generation a universal default.

## Evidence limits

No head-to-head task runs were performed. The collection has packaging checks and bounded helper checks, documented in [verification.md](verification.md). The comparison is a reasoned assessment of visible instruction design, not a benchmark or a claim that these methods are unique inventions.

All reviewed versions, including sources used for the broader inventory, appear in [comparison-sources.json](comparison-sources.json). Live repositories may change after this review.
