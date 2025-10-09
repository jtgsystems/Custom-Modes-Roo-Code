# VS Code Custom Modes Conversion

This directory contains tools and output for converting CLI-format custom modes to VS Code-compatible format.

## Overview

The Roo Code custom modes exist in two versions:

- **CLI Version**: Designed for command-line Roo Code
- **VS Code Version**: Designed for the Roo Code VS Code extension

This conversion tool transforms CLI modes into VS Code-compatible format.

## Directory Structure

```
vs-code/
├── convert_modes.py           # Conversion script
├── converted_modes/           # Output directory
│   ├── custom_modes.yaml      # VS Code-compatible mode definitions (186 modes)
│   ├── .roo/                  # Rules directory
│   │   ├── rules-{slug}/      # One directory per mode
│   │   │   └── 1_instructions.xml
│   │   └── ... (186 mode directories)
│   └── README.md              # Detailed usage guide
└── README.md                  # This file
```

## Quick Start

### List Available Modes

```bash
cd Custom-Modes-Roo-Code/vs-code
python3 convert_modes.py list
```

This displays all available modes organized alphabetically.

### Search for Modes

```bash
# Search with wildcards
python3 convert_modes.py search code*
python3 convert_modes.py search *python* *architect*

# Search multiple patterns
python3 convert_modes.py search golang* rust* *developer*
```

### Convert Modes

**Convert all modes (merges with existing):**

```bash
python3 convert_modes.py convert all
```

**Convert specific modes (adds or updates):**

```bash
python3 convert_modes.py convert code-skeptic architect python-pro
```

**Custom output directory:**

```bash
python3 convert_modes.py convert all --output my_custom_modes
```

### Manage Output Directory

**Purge the output directory:**

```bash
python3 convert_modes.py purge
```

### Copy to VS Code

**Copy to remote environment (WSL/SSH):**

```bash
python3 convert_modes.py copy remote
```

**Copy to local environment:**

```bash
python3 convert_modes.py copy local
```

### Command-Line Options

```
Usage: python3 convert_modes.py {list|search|convert|purge|copy} [args...] [options]

Commands:
  list                List all available modes
  search              Search for modes by pattern (supports wildcards)
  convert             Convert modes to VS Code format (merges with existing)
  purge               Empty the output directory
  copy                Copy converted modes to VS Code settings

Arguments:
  For search:         One or more search patterns (supports * wildcard)
  For convert:        Mode slugs to convert (use "all" for all modes)
  For copy:           Destination: 'remote' or 'local'

Options:
  --source PATH       Source custom_modes.yaml file (default: ../custom_modes.yaml)
  --output DIR        Output directory (default: converted_modes)
  --help              Show help message

Examples:
  # List and search
  python3 convert_modes.py list
  python3 convert_modes.py search code* *python*

  # Convert (merges with existing output)
  python3 convert_modes.py convert all
  python3 convert_modes.py convert code-skeptic architect
  python3 convert_modes.py convert python-pro --output my_modes

  # Manage output
  python3 convert_modes.py purge

  # Copy to VS Code
  python3 convert_modes.py copy remote
  python3 convert_modes.py copy local
```

### Conversion Behavior

**Smart Merge (Default):**
The convert command now intelligently merges modes:

- **Updates** existing modes with new data
- **Adds** new modes that don't exist
- **Preserves** existing modes not being converted

Example output:

```
Conversion complete!
Output directory: 'converted_modes'
Total modes in output: 15
  Updated: 3 mode(s)
  Added: 2 new mode(s)
  Kept: 10 existing mode(s)
```

This means you can:

1. Convert a few modes initially
2. Add more modes later without losing the first ones
3. Update specific modes without affecting others
4. Run `convert all` multiple times safely

### Installation

After conversion, use the `copy` command to install:

**Remote Environment (WSL/SSH):**

```bash
python3 convert_modes.py copy remote
```

**Local Environment:**

```bash
python3 convert_modes.py copy local
```

**Manual Installation (if needed):**

Remote (WSL/SSH):

```bash
cp converted_modes/custom_modes.yaml ~/.vscode-server/data/User/globalStorage/rooveterinaryinc.roo-cline/settings/
cp -r converted_modes/.roo ~/.vscode-server/data/User/globalStorage/rooveterinaryinc.roo-cline/settings/
```

Local Linux:

```bash
cp converted_modes/custom_modes.yaml ~/.config/Code/User/globalStorage/rooveterinaryinc.roo-cline/settings/
cp -r converted_modes/.roo ~/.config/Code/User/globalStorage/rooveterinaryinc.roo-cline/settings/
```

Local macOS:

```bash
cp converted_modes/custom_modes.yaml ~/Library/Application\ Support/Code/User/globalStorage/rooveterinaryinc.roo-cline/settings/
cp -r converted_modes/.roo ~/Library/Application\ Support/Code/User/globalStorage/rooveterinaryinc.roo-cline/settings/
```

Local Windows:

```cmd
copy converted_modes\custom_modes.yaml %APPDATA%\Code\User\globalStorage\rooveterinaryinc.roo-cline\settings\
xcopy /E /I converted_modes\.roo %APPDATA%\Code\User\globalStorage\rooveterinaryinc.roo-cline\settings\.roo
```

## Conversion Script Details

### What It Does

The `convert_modes.py` script:

- **Lists** all available modes organized alphabetically
- **Searches** for modes using wildcard patterns (\* matches any characters)
- **Converts** modes from CLI to VS Code format with smart merging
- **Merges** new conversions with existing output (updates/adds/preserves)
- **Purges** output directory when needed
- **Copies** converted modes to VS Code settings (remote or local)
- Parses the CLI `custom_modes.yaml` format
- Extracts mode metadata (slug, name, roleDefinition, groups)
- Creates VS Code-compatible YAML structure
- Generates XML instruction files from `customInstructions`
- Handles long filenames (truncates to 50 characters)
- Provides default `whenToUse` text if not specified

### Format Differences

**CLI Format:**

```yaml
customModes:
  - slug: code-skeptic
    name: 🧐 Code Skeptic
    roleDefinition: You are a SKEPTICAL...
    customInstructions: "You will: 1. NEVER ACCEPT..."
    groups: [read, edit, browser, command, mcp]
```

**VS Code Format:**

```yaml
customModes:
  - slug: code-skeptic
    name: 🧐 Code Skeptic
    roleDefinition: You are a SKEPTICAL...
    whenToUse: Use when you need to act as a 🧐 Code Skeptic...
    groups: [read, edit, browser, command, mcp]
```

The `customInstructions` content is extracted to:

```
.roo/rules-code-skeptic/1_instructions.xml
```

### Limitations

**What the script CAN do:**

- ✅ List all available modes
- ✅ Search modes with wildcard patterns
- ✅ Convert mode metadata to VS Code format
- ✅ Smart merge: update existing, add new, preserve others
- ✅ Create proper directory structure
- ✅ Generate basic XML instruction files
- ✅ Purge output directory
- ✅ Copy to VS Code settings (remote/local)
- ✅ Handle all modes automatically

**What the script CANNOT do:**

- ❌ Create semantic XML structure (like `<workflow>`, `<step>`, `<actions>`)
- ❌ Split instructions into multiple logical XML files
- ❌ Infer meaningful structure from plain text

The CLI modes contain unstructured text instructions. Hand-crafted VS Code modes use rich, semantic XML. The conversion preserves the content but cannot automatically create semantic structure.

## Source Files

The script converts from `../custom_modes.yaml` (the consolidated CLI file).

**Note:** The repository also contains individual YAML files in `../agents/` organized by category. These files have the same `customInstructions` content but include additional metadata:

- `category` and `subcategory` fields
- `version` and `lastUpdated` timestamps

The consolidated file was chosen for simplicity since the instruction content is identical.

## Features

### Smart Merge

- Converts modes incrementally without losing existing work
- Updates existing modes with new data
- Adds new modes without affecting others
- Preserves modes not being converted

### Search Capabilities

- Wildcard pattern matching (\* matches any characters)
- Search by slug or name
- Multiple patterns in single search
- Case-insensitive matching

### Flexible Deployment

- Copy to remote environment (WSL/SSH)
- Copy to local environment (native VS Code)
- Auto-detects correct paths for each platform
- Supports Windows, macOS, and Linux

## Recommendations

### Option 1: Use As-Is (Quick Start)

The converted modes work immediately in VS Code with basic functionality.

**Pros:**

- Immediate availability of 186 modes
- No additional work required

**Cons:**

- Less structured than hand-crafted modes
- Plain text instructions vs. semantic XML

### Option 2: Manual Enhancement (Recommended for Favorites)

For frequently-used modes, manually restructure the XML:

1. Read the plain text in `1_instructions.xml`
2. Identify logical sections (workflow, best practices, examples)
3. Create separate XML files with semantic structure
4. Use meaningful tags like `<workflow>`, `<step>`, `<checklist>`

**Example Enhancement:**

```bash
# Before (auto-converted)
rules-code-skeptic/
└── 1_instructions.xml  # All content in one file

# After (manually enhanced)
rules-code-skeptic/
├── 1_workflow.xml       # Structured workflow steps
├── 2_quality_gates.xml  # Quality checklist
├── 3_verification.xml   # Verification procedures
└── 4_examples.xml       # Concrete examples
```

### Option 3: Hybrid Approach (Practical)

1. Use converted modes immediately
2. Gradually enhance your most-used modes
3. Share enhanced versions with the community

## Troubleshooting

### Script Errors

**"File name too long" error:**

- Already fixed in current version (filenames truncated to 50 chars)

**"AttributeError: 'list' object has no attribute 'strip'":**

- Already fixed in current version (proper list indexing)

### Installation Issues

**Modes not appearing in VS Code:**

- Verify files are in correct location (`~/.roo/` or `./.roo/`)
- Restart VS Code or reload Roo Code extension
- Check file permissions

**Modes appear but don't work correctly:**

- Verify XML files are present in `.roo/rules-{slug}/` directories
- Check for syntax errors in `custom_modes.yaml`
- Review VS Code console for errors

## Contributing

If you enhance any modes with better XML structure:

1. Document your improvements
2. Consider sharing with the community
3. Create templates for similar modes

## Technical Details

### Script Requirements

- Python 3.6+
- PyYAML library (`pip install pyyaml`)

### Script Logic

1. Parse CLI YAML file
2. Extract mode metadata
3. Create VS Code YAML structure
4. Generate XML files from `customInstructions`
5. Handle filename length limits
6. Provide default `whenToUse` if missing

### File Naming

- Mode directories: `rules-{slug}`
- XML files: `{number}_{sanitized_title}.xml`
- Sanitization: lowercase, alphanumeric + underscores, max 50 chars

## Version History

- **v2.0** (2025-01-04): Enhanced conversion script
  - Added search command with wildcard support
  - Smart merge: updates/adds/preserves modes
  - Added purge command
  - Added copy command with remote/local support
  - Fixed customModes key (was incorrectly "modes")
  - Multiple pattern search support
- **v1.0** (2025-01-04): Initial conversion script
  - Converts modes from CLI to VS Code format
  - Handles filename length limits
  - Generates basic XML structure

## Support

For issues or questions:

- Check the detailed README in `converted_modes/README.md`
- Review Roo Code documentation
- Consult the community forums

---

**Last Updated:** 2025-01-04
**Script Version:** 2.0
**Source:** Custom-Modes-Roo-Code/custom_modes.yaml (CLI format)
**Target:** VS Code Roo Code Extension

## Quick Reference

```bash
# Workflow example
python3 convert_modes.py list                    # See all modes
python3 convert_modes.py search *python*         # Find Python modes
python3 convert_modes.py convert python-pro      # Convert one mode
python3 convert_modes.py convert all             # Convert all (merges)
python3 convert_modes.py copy remote             # Install to VS Code
```
