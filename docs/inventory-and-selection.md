# Personal skill inventory and publication selection

Inventory date: **2026-10-16**. Scope: the owner's personal installed skills directory and directly maintained skill repositories under the local Developer workspace. Bundled system/plugin caches and dependency/vendor trees are excluded. This is not a claim to have found every skill on every device or remote platform.

## Ownership and scope

- **18** non-system installed skill directories were inspected.
- **5** match identifiable upstream skills exactly or very closely and are excluded from the custom collection.
- **13** remaining installed skills are treated as the owner's custom or locally tailored candidates; one additional maintained, uninstalled Windows VM skill brings the inventory to **14**.
- This classification uses local content, repository context, and upstream comparison. It is not an exhaustive authorship or legal-provenance certification. A locally tailored workflow can use widely shared engineering principles.

The selection favors a distinct use case, an explicit mechanism visible in the instructions, useful supporting resources, standalone portability, and suitability for public release. No popularity score or invented performance ranking was used.

## All custom or locally tailored candidates

| Skill | Main function | Reviewed comparator | Relative task fit / differentiator | Decision |
| --- | --- | --- | --- | --- |
| adaptive-academic-note-architect | Comprehensive academic notes; bilingual explanations and document helpers | [lecture-to-study-guide](https://github.com/Jellypod-Inc/school-skills/blob/cd484795e924e454caafd13ddc25c1ec76c48718/skills/lecture-to-study-guide/SKILL.md); [lecture-to-summary-skills](https://github.com/GraceLiao77/lecture-to-summary-skills/blob/843284cc45336f2159af3f396a5a8130c994ebab/SKILL.md) | Stronger fit for full source reconstruction and DOCX navigation than short exam review | Already public; comparison added and featured |
| product-ui-qa | Product UI implementation and quality review | [web-design-guidelines](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/web-design-guidelines/SKILL.md); [webapp-testing](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/webapp-testing/SKILL.md) | Explicit component necessity, state coverage, and adversarial completion pass | Publish in this collection |
| visual-convergence | Refine an existing UI against approved preferences | [frontend-design](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/frontend-design/SKILL.md) | Separates correct tokens from perceptual composition; records preference confidence | Publish in this collection |
| project-history-archivist | Conversation and development-history archive | [codex-chat-export](https://github.com/wimi321/codex-chat-export/blob/988f58148422fb186df2d5893740f8d3669a7330/SKILL.md); [session-synthesis](https://github.com/gfouillet/session-synthesis-skill/blob/83c0f1d1566255b2b668806373c73497f4c9f277/SKILL.md) | Project inventory reconciliation and Git corroboration leading to a rendered DOCX | Publish in this collection |
| software-history-lessons | Extract and transfer engineering lessons | [game-postmortem](https://github.com/NVlabs/Skill2Env/blob/507eab4d9952968de2be98f8729d3c66d487285a/SkillHub/skills/game-postmortem/SKILL.md) | Patch-level reconstruction plus explicit target-fit and validation chain | Publish in this collection |
| ai-pipeline-evaluation | Frozen-case evaluation across learned pipelines | [llm-evaluation](https://github.com/wshobson/agents/blob/044b4b21f083948e69ec878a7b07c8d0951a6ffa/plugins/llm-application-dev/skills/llm-evaluation/SKILL.md) | Broad modality scope and strict real-versus-mocked evidence; overlaps mature evaluation practice | Defer: needs runnable example cases and a demonstrated harness |
| deployment-verification | Fresh build, runtime, persistence, and release checks | [deployment-pipeline-design](https://github.com/wshobson/agents/blob/044b4b21f083948e69ec878a7b07c8d0951a6ffa/plugins/cicd-automation/skills/deployment-pipeline-design/SKILL.md) | Separates build, runtime, deployment, and device evidence; provider-neutral verification | Defer: useful complement; fewer packaged execution tools |
| e2e-product-verification | Verify the real critical journey across system boundaries | [e2e-testing-patterns](https://github.com/wshobson/agents/blob/044b4b21f083948e69ec878a7b07c8d0951a6ffa/plugins/developer-essentials/skills/e2e-testing-patterns/SKILL.md); [webapp-testing](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/webapp-testing/SKILL.md) | Explicit provider, artifact, worker, restart, and persistence evidence | Defer: needs a portable worked system example |
| frontend-ui-qa | Frontend hierarchy, tokens, accessibility, and rendered states | [web-design-guidelines](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/skills/web-design-guidelines/SKILL.md) | Combines design-system judgment with runtime inspection | Defer: substantial overlap with the selected product-ui-qa |
| full-cycle-product-development | Coordinate requirements through implementation and release evidence | [Superpowers workflow](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/README.md) | Adds AI, provider, runtime, and product evidence boundaries to a composed workflow | Defer: many companion-skill dependencies reduce standalone portability |
| platform-api-integration | Provider contracts, adapters, auth, retries, and real smoke checks | [api-design-principles](https://github.com/wshobson/agents/blob/044b4b21f083948e69ec878a7b07c8d0951a6ffa/plugins/backend-development/skills/api-design-principles/SKILL.md) (adjacent: API design) | Focuses on consuming external providers and proving real-provider compatibility | Defer: needs a runnable provider-neutral adapter example |
| repo-development | Repository authority, concurrent work, scoped edits, and commits | [Superpowers workflow](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/README.md) | Concise local coordination around authority and evidence | Defer: overlaps established upstream workflow skills |
| singapore-career-ops | Evidence-based role assessment and application operations | [job-search-skill](https://github.com/Julien-ser/job-search-skill/blob/4463e2d2997b89db0235bf547ebef8a40996c925/SKILL.md) | Singapore-oriented feasibility gates and workspace evidence discipline | Keep local: personal workspace contract and authorization conventions |
| windows-vm-simulation | Validate a macOS source snapshot in a Windows ARM VM | [PowerToys ui-tests-local-vm](https://github.com/microsoft/PowerToys/blob/0b305162b77fa1f2e05b347d7c00cb5d8c3e0d4f/.github/skills/ui-tests-local-vm/SKILL.md) (adjacent: Windows/Hyper-V) | macOS/UTM/SSH transport with source manifests and returned-result binding | Defer: strong niche candidate; needs portable setup and fresh guest validation |

## Installed upstream skills — not presented as original work

| Installed name | Source reviewed | Classification |
| --- | --- | --- |
| `systematic-debugging` | [obra/superpowers](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/systematic-debugging/SKILL.md) | Very close line match with local differences; retain upstream attribution |
| `test-driven-development` | [obra/superpowers](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/test-driven-development/SKILL.md) | Very close line match with local differences; retain upstream attribution |
| `using-git-worktrees` | [obra/superpowers](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/using-git-worktrees/SKILL.md) | Exact line match; retain upstream attribution |
| `verification-before-completion` | [obra/superpowers](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/verification-before-completion/SKILL.md) | Exact line match; retain upstream attribution |
| `playwright` | [openai/skills](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/playwright/SKILL.md) | Exact line match; upstream package also includes its license/notice |

## Publication outcome and tradeoffs

The four new packages cover two coherent pairs: product quality / visual alignment, and historical reconstruction / knowledge transfer. Each ships with its original workflow and reference resources, a dedicated README, usage examples, and explicit limits. The already published academic skill remains in its own repository and is featured alongside them.

The deferred entries remain useful. Deferral means that this release prioritizes differentiation and public packaging readiness; it does not establish that another skill is ineffective. In particular, the Windows VM bridge is a promising follow-up after environment setup and source/result checks can be demonstrated on a fresh guest.

No private repository URL, personal job-search record, conversation export, credential, or VM connection setting is included in this public inventory. The complete source list is [comparison-sources.json](comparison-sources.json).
