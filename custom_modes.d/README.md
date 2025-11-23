# Per-mode configs

Each YAML here contains a single entry under `customModes:`. Add/edit one file per mode instead of modifying the monolithic `custom_modes.yaml`. The original file was backed up to `custom_modes.yaml.backup-20251123` in repo root.

To regenerate from a combined file, you can run:

```
node /home/ultron/workspace/roo-code/scripts/split-custom-modes.js \
  --source ./custom_modes.yaml.backup-20251123 \
  --outdir ./custom_modes.d
```
