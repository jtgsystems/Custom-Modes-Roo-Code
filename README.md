# Roo Code Agents (Newest) + custom_modes.yaml

This repo is streamlined to include only:
- agents/ — the newest curated Roo Code agents
- agents/custom_modes.yaml — a consolidated modes file for quick import

How to use
- Global: copy relevant modes into your Roo Code global settings file `settings/custom_modes.yaml`.
- Project: use a `.roomodes` file at your project root for project‑specific modes.
- Validation: Roo Code validates against the official schema automatically. For extra safety, add this as the first line of your global file:
  `# yaml-language-server: $schema=https://json.schemastore.org/roomodes.json`

Marketplace submission (JTGSYSTEMS)
- Prepared 5 large, unique modes suitable for the Roo Marketplace (see prior submission artifacts if needed).
- Credit: JTGSYSTEMS.COM (author / authorUrl).

Notes
- Removed legacy folders (agents-json, backup-original, indexes, combined files) to keep the repo clean and current.
- Keep modes strictly compliant: required keys are `slug`, `name`, `roleDefinition`; optional `whenToUse`, `customInstructions`, `groups`.

