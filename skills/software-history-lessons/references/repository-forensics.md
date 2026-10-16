# Repository Forensics

Read this reference only for Mode A or when the user explicitly requests Git verification.

## Safety boundary

Use the repository as immutable evidence. Do not edit files, install dependencies, run formatters, create or amend commits, reset, rebase, merge, cherry-pick, stash, push, pull, clean, delete branches or worktrees, change Git configuration, or switch history in a way that changes the working tree. Prefer Git object-database inspection such as `git show <commit>:<path>`.

At both start and finish capture, as applicable:

- current branch, `HEAD`, and upstream/ahead-behind state;
- working-tree and index status, including untracked files;
- worktree inventory;
- relevant branches, tags, releases, roots, and remotes by name;
- any pre-existing anomalies that affect confidence.

Compare the two snapshots and state whether the repository changed. Do not expose credential-bearing remote URLs.

## Establish the evidence graph

1. Identify repository roots, object reachability, date range, commit count, branch topology, merge bases, tags/releases, and worktrees.
2. Define the **canonical history in scope**: all commits that contribute to the product line, release line, or explicitly requested branch set. Explain the boundary. Keep unmerged or abandoned experiments separate unless they are relevant evidence.
3. Traverse the canonical set chronologically/topologically without sampling. Deduplicate commits by object ID.
4. Do not assume first-parent history is complete. For each merge, inspect the merge result, all parents, the commits introduced by the merged side, and any merge-resolution delta. Handle octopus merges explicitly when present.
5. Follow renames and copies with tree/diff evidence. `--follow` is a single-path aid, not a complete repository-history strategy.
6. Map tags and releases to commits and distinguish source evolution from release packaging.

Useful read-only operations include `status`, `rev-parse`, `branch -a`, `worktree list`, `log`, `rev-list`, `show`, `diff`, `diff-tree`, `cat-file`, `ls-tree`, `blame`, `merge-base`, `tag`, `describe`, and `shortlog`. Adapt commands to the repository; never let a command mutate it.

## Complete inventory before narrative

For every relevant canonical commit, inspect the actual patch or tree delta and record:

- hash, date, message, parents, and author only when useful;
- files added, deleted, renamed, copied, or modified;
- approximate change size as context, never as a productivity metric;
- important source, test, documentation, configuration, runtime, packaging, and evaluation changes;
- architectural and user-visible impact supported by the patch;
- related defect, risk, validation, release, and category;
- whether the change is source-of-truth, generated output, or both.

For significant commits, add `BEFORE`, `CHANGE`, `AFTER`, `MOTIVATION` (only if supported), `VALIDATION`, `CONSEQUENCES`, and `FOLLOW-UP`. Decompose mixed commits by concern. Tiny coherent commits may be narrated together, but each still appears in the inventory.

Common inspection patterns:

```text
git show --stat --summary <commit>
git show --find-renames --find-copies <commit>
git diff <parent> <commit> -- <path>
git diff-tree --no-commit-id --name-status -r -M -C <commit>
git show --cc <merge>
git show <commit>:<path>
```

Use commands as patterns, not a fixed script. Root commits, binary assets, submodules, shallow clones, replace/graft objects, and missing LFS content require explicit handling or an `UNKNOWN` limitation.

## Separate source from artifacts

Identify authoritative source paths and generated/build/runtime artifacts through build configuration, ignore rules, manifests, file headers, duplicated content, and historical context. Examples include `dist`, `build`, bundled assets, installers, generated clients, vendored runtimes/models, logs, screenshots, benchmarks, and evaluation output.

Do not double-count generated copies as architecture work. Still inspect them when they reveal shipping behavior, reproducibility, deployment, packaging, release, or platform evolution.

## Analysis passes

Perform these passes in order so the story emerges from evidence:

1. **Topology:** roots, branches, merges, tags/releases, scope, and repository state.
2. **Inventory:** every canonical commit in chronological/topological order.
3. **Patch inspection:** actual deltas for every canonical commit; deep analysis for significant ones.
4. **Subsystem and module lineage:** introduction, responsibility, rewrites, renames/moves, dependencies, fixes, removals, and current role.
5. **Bug to root-cause to fix chains:** symptom, introduction/exposure, code-level cause, fix mechanism, regression protection, and lesson.
6. **Phase reconstruction:** cluster phases only after patch inspection. Give dates and boundary commits, starting state, objective, implementation, data-flow/architecture change, failures, validation, ending state, and lesson.
7. **Current-architecture cross-check:** explain the present design as the endpoint of the verified history.
8. **Synthesis:** distill transferable experience using the separate reference.

## Required lenses where applicable

- Architecture evolution by discovered subsystem and its turning points.
- Important module lineage, including removed and superseded implementations.
- Testing maturity: unit, integration, end-to-end, smoke, regression, fixtures, CI, runtime/platform, and release validation.
- Evaluation methodology: datasets, versions/configurations, metrics, provenance, reproducibility, manifests, hashes, resumability, no-overwrite safeguards, and what results do and do not prove.
- AI/model/RAG: providers and runtimes, prompts/configuration, lifecycle/orchestration, ingestion, indexing, chunking, retrieval, ranking, grounding, citations, validation, fallback, and provenance.
- Meaningful UI/workflow evolution tied to backend capabilities rather than cosmetic churn.
- Deployment, packaging, runtime, local/cloud, cross-platform, native dependencies, installers, provisioning, startup/shutdown, paths, ports, fallbacks, and incidents.
- Reliability: state integrity, concurrency, resource management, cancellation, timeouts, errors, observability, privacy, and security.

## Evidence ledger

Maintain claim-level provenance. A useful row contains: claim ID, label, claim, commit/release, path and symbol, corroborating test/config/doc, confidence limit, and downstream lessons. If the repository shows what changed but not why, say so. If a proposed root cause is only suggested, mark it `INFERENCE`.

## Scale and stopping condition

Large histories may be processed in batches or with machine-readable inventories, but do not sample. Keep scratch work outside the repository unless the user authorized a repository file. If response limits require multiple parts, preserve the complete inventory and announce what remains.

Mode A is complete only when every canonical commit in scope has been inventoried and patch-inspected, significant commits have deep analysis, merges and rename lineage are handled, the relevant lenses are covered, uncertainties are explicit, and the ending state matches the starting repository state.
