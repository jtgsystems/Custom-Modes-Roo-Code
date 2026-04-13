# AGENTS.md

## Senior Maintainer Contract
- Purpose: keep this repository stable, secure, well-tested, and aligned with existing patterns.
- Default mode: smallest safe change that solves the verified problem.
- Do not guess conventions.
- Do not disable tests, lint, type checks, or security controls to make a change pass.
- Do not introduce major-version dependency upgrades without a migration plan and a dedicated PR.

## Repository Snapshot
- Repository: `jtgsystems/Custom-Modes-Roo-Code`
- Default branch: `main`
- Visibility: `public`
- Summary: Custom modes for Roo Code VS Code extension - Enhanced AI coding assistance configurations
- Detected stack: mixed or uncategorized source repo

## Read First
- `README.md`
- `CONTRIBUTING.md`
- `CLAUDE.md`
- `.github/workflows/`

## Key Paths
- `scripts/`
- `assets/`
- `agents/`
- `custom_modes.d/`
- `schemas/`
- `vs-code/`

## Directory Guidance
- `scripts/`: keep maintenance scripts idempotent and document environment assumptions.

## Repository Rules
- Keep changes focused on the task and match the existing file layout and naming patterns.
- Update tests and docs when behavior changes or public interfaces move.
- Do not commit secrets, credentials, ad-hoc exports, or large generated artifacts unless the repository already tracks them intentionally.
- Prefer the existing automation and CI workflow over one-off commands when both paths exist.

## Global Best Practices
- Understand the repo before editing: read the local guidance, README, docs, and relevant tests first.
- Follow existing architecture, conventions, and tooling; do not guess stack-specific patterns when the repo already defines them.
- Make the smallest safe change that solves the real problem, and prefer focused diffs over broad rewrites.
- Verify changes with the repo's actual checks, and add or update regression tests for behavior changes when practical.
- Keep public APIs and backward compatibility stable unless the task explicitly allows a breaking change.
- Do not overwrite user work, unrelated changes, or existing security controls just to make a check pass.
- Update docs when commands, config, setup, architecture, or user-visible behavior changes.
- If the change is ambiguous or high-risk, stop and produce a safe partial fix or a clear plan instead of guessing.
- Leave clear notes on what changed, why it changed, what checks ran, and any remaining risk.
- Legacy agent guidance exists in `CLAUDE.md`; keep it aligned with `AGENTS.md` if those files remain in use.
- Avoid archive-style folders unless the task explicitly targets them: `.retired/`.

## High-Risk Focus Areas
- Treat packaged `.vsix` or other binary extension artifacts as outputs, not edit targets; prefer the unpacked source tree when one exists.
- Permission or manifest changes are security-sensitive and should be reviewed as behavior changes, not cosmetic edits.
- Ops/config changes should be idempotent, explicit about host or shell assumptions, and careful about secrets, service restarts, and rollback safety.

## Command Map
- Install: No dedicated install command detected from root manifests.
- Lint: No dedicated lint command detected.
- Typecheck: No dedicated typecheck command detected.
- Unit tests: No dedicated unit-test command detected.
- Integration tests: No dedicated integration-test command detected.
- E2E tests: No dedicated end-to-end test command detected.
- Build: No dedicated build command detected.
- Security scan: No dedicated security scan command detected; inspect `.github/workflows/` or add one before relying on automated maintenance.

## Maintenance Workflow
- Start by reading this `AGENTS.md` and any closer `AGENTS.md` files in impacted directories.
- Map the repo before editing: structure, package manager, lockfiles, scripts, tests, CI, and docs.
- For larger maintenance sweeps, parallelize independent review lanes for correctness, security, dependency/tooling health, and test/CI reliability when the agent runtime supports it.
- Prioritize work as P1 critical/security/production risk, P2 bugs/regressions/performance cliffs, P3 cleanup/readability.
- When fixing behavior, add or update a regression test where practical.
- Keep diffs small and reviewable; split unrelated fixes into separate PRs.

## Done Definition
- Run all relevant checks for the area you changed: lint, typecheck, unit, integration, e2e, security, and build when the repo defines them.
- Verify results and ensure there is no obvious regression.
- Summarize changes, checks run, risks, and next steps.

## Code Review Standard
- Correctness: does the change solve the problem, handle edge cases, and cover null/empty/error states?
- Regression risk: could it break existing contracts, schemas, or shared-module assumptions?
- Security: check auth, validation, injection, XSS, SSRF, CSRF, traversal, shell execution, secrets, and unsafe defaults.
- Data integrity: check migrations, partial writes, duplicate writes, stale caches, destructive updates, and rollback safety.
- Testing: ensure tests are sufficient, deterministic, and include a regression test for behavior fixes.
- Performance: look for N+1 queries, repeated computation, render loops, blocking I/O, and hot-path regressions.
- Maintainability: keep code understandable, aligned with existing abstractions, and free of dead code.
- Observability: preserve useful errors, logs, traces, and debugging context.

## Review Output Format
- severity: `P1`, `P2`, or `P3`
- category
- finding
- evidence
- recommended fix
- whether a test is missing

## Notes
- CI source of truth lives in `.github/workflows/`.

Update this file whenever the repo's actual commands, structure, or maintenance rules change.
Generated by `scripts/github/agentsmd_rollout.py`.
