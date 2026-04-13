# AGENTS.md

## Repo Snapshot
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
- `agents/`
- `assets/`
- `custom_modes.d/`
- `schemas/`
- `vs-code/`

## Working Rules
- Keep changes focused on the task and match the existing file layout and naming patterns.
- Update tests and docs when behavior changes or public interfaces move.
- Do not commit secrets, credentials, ad-hoc exports, or large generated artifacts unless the repository already tracks them intentionally.
- Prefer the existing automation and CI workflow over one-off commands when both paths exist.
- Legacy agent guidance exists in `CLAUDE.md`; keep it aligned with `AGENTS.md` if those files remain in use.
- Avoid archive-style folders unless the task explicitly targets them: `.retired/`.

## Verified Commands
- No reliable build or test command was detected from the repo root manifests.
- Check the files in `Read First` and `.github/workflows/` before changing code or release logic.

## Change Checklist
- Run the relevant tests or static checks for the files you changed before finishing.
- Keep human-facing docs aligned with behavior changes.
- If the repo has specialized areas later, add nested `AGENTS.md` files close to that code instead of overloading the root file.

## Notes
- CI source of truth lives in `.github/workflows/`.

This file should stay short, specific, and current. Update it whenever the repo's real setup or verification steps change.
