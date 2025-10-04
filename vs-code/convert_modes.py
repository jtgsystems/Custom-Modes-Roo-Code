#!/usr/bin/env python3
"""
Convert Roo Code CLI custom modes to VS Code format.

This script provides tools for converting, searching, and managing custom modes
for the Roo Code VS Code extension.
"""

from __future__ import annotations

import argparse
import fnmatch
import logging
import os
import platform
import re
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

import yaml

# Constants
VSCODE_SETTINGS_SUBPATH = "data/User/globalStorage/rooveterinaryinc.roo-cline/settings"
DEFAULT_SOURCE = "../custom_modes.yaml"
DEFAULT_OUTPUT = "converted_modes"
MAX_FILENAME_LENGTH = 50
ROLE_DEFINITION_PREVIEW_LENGTH = 100
SEPARATOR_WIDTH = 80

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s"
)
logger = logging.getLogger(__name__)


def sanitize_filename(name: str, max_length: int = MAX_FILENAME_LENGTH) -> str:
    """
    Sanitize a string to be used as a filename.
    
    Args:
        name: The string to sanitize
        max_length: Maximum length of the resulting filename
        
    Returns:
        Sanitized filename string
    """
    name = name.strip().lower()
    name = re.sub(r'[^a-z0-9\s-]', '', name)
    name = re.sub(r'[\s-]+', '_', name)
    return name[:max_length] if len(name) > max_length else name


def parse_instructions_to_xml(instructions: str, output_dir: Path, slug: str) -> None:
    """
    Parse customInstructions string and create XML rule files.
    
    Args:
        instructions: The instruction content to write
        output_dir: Directory to write the XML file to
        slug: Mode slug for reference
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if instructions:
        xml_file = output_dir / "1_instructions.xml"
        try:
            # Replace literal \n with actual newlines for better readability
            formatted_instructions = instructions.replace('\\n', '\n')
            xml_file.write_text(formatted_instructions, encoding='utf-8')
        except IOError as e:
            logger.error(f"Failed to write instructions for {slug}: {e}")
            raise


def load_modes(source_file: Path) -> List[Dict[str, Any]]:
    """
    Load modes from the source YAML file.
    
    Args:
        source_file: Path to the source YAML file
        
    Returns:
        List of mode dictionaries
        
    Raises:
        SystemExit: If file not found or YAML parsing fails
    """
    try:
        with source_file.open('r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data.get('customModes', [])
    except FileNotFoundError:
        logger.error(f"Error: Source file not found at '{source_file}'")
        sys.exit(1)
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML file: {e}")
        sys.exit(1)
    except IOError as e:
        logger.error(f"Error reading file: {e}")
        sys.exit(1)


def list_modes(source_file: Path) -> None:
    """
    List all available modes organized alphabetically.
    
    Args:
        source_file: Path to the source YAML file
    """
    modes = load_modes(source_file)
    
    print(f"\n{'=' * SEPARATOR_WIDTH}")
    print(f"Available Modes ({len(modes)} total)")
    print(f"{'=' * SEPARATOR_WIDTH}\n")
    
    # Group by first letter for easier browsing
    modes_by_letter: Dict[str, List[Dict[str, str]]] = {}
    for mode in modes:
        slug = mode.get('slug', '')
        if slug:
            first_letter = slug[0].upper()
            if first_letter not in modes_by_letter:
                modes_by_letter[first_letter] = []
            modes_by_letter[first_letter].append({
                'slug': slug,
                'name': mode.get('name', 'N/A')
            })
    
    # Print organized by letter
    for letter in sorted(modes_by_letter.keys()):
        print(f"\n{letter}")
        print("-" * 40)
        for mode in sorted(modes_by_letter[letter], key=lambda x: x['slug']):
            print(f"  {mode['slug']:<30} {mode['name']}")
    
    print(f"\n{'=' * SEPARATOR_WIDTH}")
    print(f"Total: {len(modes)} modes")
    print(f"{'=' * SEPARATOR_WIDTH}\n")


def search_modes(source_file: Path, patterns: List[str]) -> None:
    """
    Search for modes matching the given patterns.
    
    Args:
        source_file: Path to the source YAML file
        patterns: List of search patterns (supports wildcards)
    """
    if not patterns:
        logger.error("Error: Please provide at least one search pattern")
        sys.exit(1)
    
    modes = load_modes(source_file)
    matched_modes: List[Dict[str, str]] = []
    
    for mode in modes:
        slug = mode.get('slug', '').lower()
        name = mode.get('name', '').lower()
        
        # Check if any pattern matches slug or name
        for pattern in patterns:
            pattern_lower = pattern.lower()
            if fnmatch.fnmatch(slug, pattern_lower) or fnmatch.fnmatch(name, pattern_lower):
                role_def = mode.get('roleDefinition', '')
                truncated_role = (
                    role_def[:ROLE_DEFINITION_PREVIEW_LENGTH] + '...'
                    if len(role_def) > ROLE_DEFINITION_PREVIEW_LENGTH
                    else role_def
                )
                matched_modes.append({
                    'slug': mode.get('slug', ''),
                    'name': mode.get('name', 'N/A'),
                    'roleDefinition': truncated_role
                })
                break  # Don't add the same mode multiple times
    
    print(f"\n{'=' * SEPARATOR_WIDTH}")
    print(f"Search Results for: {', '.join(patterns)}")
    print(f"{'=' * SEPARATOR_WIDTH}\n")
    
    if not matched_modes:
        print("No modes found matching the search patterns.")
    else:
        print(f"Found {len(matched_modes)} mode(s):\n")
        for mode in sorted(matched_modes, key=lambda x: x['slug']):
            print(f"  {mode['slug']:<30} {mode['name']}")
            if mode['roleDefinition']:
                print(f"    → {mode['roleDefinition']}")
            print()
    
    print(f"{'=' * SEPARATOR_WIDTH}\n")


def get_vscode_settings_path(environment: str) -> Path:
    """
    Get the VS Code settings directory path based on environment.
    
    Args:
        environment: Either 'remote' or 'local'
        
    Returns:
        Path to VS Code settings directory
    """
    home = Path.home()
    
    if environment == 'remote':
        return home / ".vscode-server" / VSCODE_SETTINGS_SUBPATH
    
    # Local environment
    system = platform.system()
    if system == "Windows":
        appdata = os.environ.get('APPDATA', str(home / 'AppData' / 'Roaming'))
        return Path(appdata) / "Code" / "User" / "globalStorage" / "rooveterinaryinc.roo-cline" / "settings"
    elif system == "Darwin":
        return home / "Library" / "Application Support" / "Code" / "User" / "globalStorage" / "rooveterinaryinc.roo-cline" / "settings"
    else:
        return home / ".config" / "Code" / "User" / "globalStorage" / "rooveterinaryinc.roo-cline" / "settings"


def purge_converted_modes(output_base_dir: Path) -> None:
    """
    Remove all files from the converted modes directory.
    
    Args:
        output_base_dir: Directory to purge
    """
    if output_base_dir.exists():
        try:
            shutil.rmtree(output_base_dir)
            output_base_dir.mkdir(parents=True)
            logger.info(f"✓ Purged directory: {output_base_dir}")
        except (OSError, IOError) as e:
            logger.error(f"Error purging directory: {e}")
            sys.exit(1)
    else:
        output_base_dir.mkdir(parents=True)
        logger.info(f"✓ Created directory: {output_base_dir}")


def copy_to_vscode(source_dir: Path, environment: str) -> None:
    """
    Copy converted modes to VS Code settings directory.
    
    Args:
        source_dir: Source directory containing converted modes
        environment: Either 'remote' or 'local'
    """
    if not environment:
        logger.error("Error: Please specify the destination environment (remote or local)")
        logger.info("Usage: python3 convert_modes.py copy remote")
        logger.info("       python3 convert_modes.py copy local")
        sys.exit(1)
    
    if environment not in ['remote', 'local']:
        logger.error(f"Error: Invalid environment '{environment}'. Must be 'remote' or 'local'")
        sys.exit(1)
    
    vscode_dir = get_vscode_settings_path(environment)
    
    if not vscode_dir.exists():
        logger.info(f"Creating VS Code settings directory: {vscode_dir}")
        vscode_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy custom_modes.yaml
    source_yaml = source_dir / 'custom_modes.yaml'
    dest_yaml = vscode_dir / 'custom_modes.yaml'
    
    if not source_yaml.exists():
        logger.error(f"Error: Source file not found: {source_yaml}")
        sys.exit(1)
    
    try:
        shutil.copy2(source_yaml, dest_yaml)
        logger.info(f"✓ Copied custom_modes.yaml to {dest_yaml}")
        
        # Copy .roo directory if it exists
        source_roo = source_dir / '.roo'
        dest_roo = vscode_dir / '.roo'
        
        if source_roo.exists():
            if dest_roo.exists():
                shutil.rmtree(dest_roo)
            shutil.copytree(source_roo, dest_roo)
            logger.info(f"✓ Copied .roo directory to {dest_roo}")
        
        logger.info(f"\n✓ Successfully copied modes to VS Code ({environment} environment)")
        logger.info(f"  Location: {vscode_dir}")
    except (OSError, IOError) as e:
        logger.error(f"Error copying files: {e}")
        sys.exit(1)


def convert_modes(source_file: Path, output_base_dir: Path, mode_slugs: Optional[List[str]] = None) -> None:
    """
    Convert CLI custom modes to VS Code compatible format.
    
    Args:
        source_file: Path to source YAML file
        output_base_dir: Output directory for converted modes
        mode_slugs: Optional list of specific mode slugs to convert
    """
    output_yaml_file = output_base_dir / 'custom_modes.yaml'
    rules_base_dir = output_base_dir / '.roo'
    rules_base_dir.mkdir(parents=True, exist_ok=True)

    all_modes = load_modes(source_file)
    
    # Filter modes if specific slugs were requested
    if mode_slugs and 'all' not in mode_slugs:
        modes_to_convert = [m for m in all_modes if m.get('slug') in mode_slugs]
        
        # Check for invalid slugs
        found_slugs = {m.get('slug') for m in modes_to_convert}
        invalid_slugs = set(mode_slugs) - found_slugs
        if invalid_slugs:
            logger.warning("\nWarning: The following mode slugs were not found:")
            for slug in invalid_slugs:
                logger.warning(f"  - {slug}")
            print()
        
        if not modes_to_convert:
            logger.error("Error: No valid modes found to convert")
            sys.exit(1)
    else:
        modes_to_convert = all_modes

    # Load existing modes from output file if it exists
    existing_modes: List[Dict[str, Any]] = []
    existing_slugs: Set[str] = set()
    
    if output_yaml_file.exists():
        try:
            with output_yaml_file.open('r', encoding='utf-8') as f:
                existing_data = yaml.safe_load(f)
                if existing_data and 'customModes' in existing_data:
                    existing_modes = existing_data['customModes']
                    existing_slugs = {m.get('slug') for m in existing_modes if m.get('slug')}
                    logger.info(f"\nFound {len(existing_modes)} existing mode(s) in output file")
        except (IOError, yaml.YAMLError) as e:
            logger.warning(f"Warning: Could not read existing output file: {e}")

    new_modes: List[Dict[str, Any]] = []
    updated_count = 0
    added_count = 0
    
    for mode in modes_to_convert:
        slug = mode.get('slug')
        if not slug:
            continue

        rules_dir_name = f"rules-{slug}"
        rules_output_dir = rules_base_dir / rules_dir_name
        
        instructions = mode.get('customInstructions', '')
        if instructions:
            parse_instructions_to_xml(instructions, rules_output_dir, slug)

        new_mode = {
            'slug': slug,
            'name': mode.get('name'),
            'roleDefinition': mode.get('roleDefinition'),
            'whenToUse': mode.get('whenToUse', f"Use when you need to act as a {mode.get('name')}. This mode is specialized for its defined role."),
            'groups': mode.get('groups', ['read', 'edit'])
        }
        
        if slug in existing_slugs:
            updated_count += 1
        else:
            added_count += 1
        
        new_modes.append(new_mode)

    # Merge: Update existing modes and add new ones
    merged_modes: List[Dict[str, Any]] = []
    new_modes_dict = {m['slug']: m for m in new_modes}
    
    # First, add/update modes from conversion
    for mode in existing_modes:
        slug = mode.get('slug')
        if slug in new_modes_dict:
            # Update existing mode with new data
            merged_modes.append(new_modes_dict[slug])
            del new_modes_dict[slug]
        else:
            # Keep existing mode that wasn't converted
            merged_modes.append(mode)
    
    # Add any remaining new modes
    merged_modes.extend(new_modes_dict.values())

    final_output = {'customModes': merged_modes}

    # Dump to string first, then fix indentation
    yaml_content = yaml.dump(
        final_output,
        default_flow_style=False,
        sort_keys=False,
        width=1000,
        allow_unicode=True,
        indent=2
    )
    
    # Fix the indentation: PyYAML doesn't indent list items at the root level properly
    lines = yaml_content.split('\n')
    fixed_lines: List[str] = []
    in_mode_item = False
    
    for line in lines:
        if line.startswith('customModes:'):
            fixed_lines.append(line)
            in_mode_item = False
        elif line.startswith('- slug:'):
            # Mode list item - add 2 spaces
            fixed_lines.append('  ' + line)
            in_mode_item = True
        elif in_mode_item and line and not line.startswith(' '):
            # Properties of mode item - add 4 spaces
            fixed_lines.append('    ' + line)
        elif in_mode_item and line.startswith('  '):
            # Already has some indentation, add 2 more spaces
            fixed_lines.append('  ' + line)
        else:
            fixed_lines.append(line)
    
    yaml_content = '\n'.join(fixed_lines)
    
    try:
        output_yaml_file.write_text(yaml_content, encoding='utf-8')
    except IOError as e:
        logger.error(f"Error writing output file: {e}")
        sys.exit(1)

    logger.info("\nConversion complete!")
    logger.info(f"Output directory: '{output_base_dir}'")
    logger.info(f"Total modes in output: {len(merged_modes)}")
    if updated_count > 0:
        logger.info(f"  Updated: {updated_count} mode(s)")
    if added_count > 0:
        logger.info(f"  Added: {added_count} new mode(s)")
    if len(existing_modes) > len(new_modes):
        kept_count = len(existing_modes) - updated_count
        logger.info(f"  Kept: {kept_count} existing mode(s)")
    
    if mode_slugs and 'all' not in mode_slugs:
        logger.info("\nProcessed modes:")
        for mode in new_modes:
            status = "updated" if mode['slug'] in existing_slugs else "added"
            logger.info(f"  - {mode['slug']}: {mode['name']} ({status})")


def main() -> None:
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description='Convert Roo Code CLI custom modes to VS Code format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # List all available modes
  python3 convert_modes.py list

  # Search for modes (supports wildcards)
  python3 convert_modes.py search code*
  python3 convert_modes.py search *python* *architect*

  # Convert all modes
  python3 convert_modes.py convert all

  # Convert specific modes
  python3 convert_modes.py convert code-skeptic architect python-pro

  # Convert with custom output directory
  python3 convert_modes.py convert all --output my_modes

  # Purge converted modes directory
  python3 convert_modes.py purge

  # Copy converted modes to VS Code
  python3 convert_modes.py copy remote
  python3 convert_modes.py copy local
        '''
    )
    
    parser.add_argument(
        'command',
        choices=['list', 'search', 'convert', 'purge', 'copy'],
        help='Command to execute: list (show all modes), search (find modes), convert (convert modes), purge (empty output dir), copy (copy to VS Code)'
    )
    
    parser.add_argument(
        'modes',
        nargs='*',
        help='Mode slugs to convert, search patterns (supports wildcards), or destination for copy (remote/local)'
    )
    
    parser.add_argument(
        '--source',
        default=DEFAULT_SOURCE,
        help=f'Path to source custom_modes.yaml file (default: {DEFAULT_SOURCE})'
    )
    
    parser.add_argument(
        '--output',
        default=DEFAULT_OUTPUT,
        help=f'Output directory for converted modes (default: {DEFAULT_OUTPUT})'
    )
    
    args = parser.parse_args()
    
    # Convert paths to Path objects
    source_path = Path(args.source)
    output_path = Path(args.output)
    
    # Handle list command
    if args.command == 'list':
        list_modes(source_path)
        return
    
    # Handle search command
    if args.command == 'search':
        search_modes(source_path, args.modes)
        return
    
    # Handle purge command
    if args.command == 'purge':
        purge_converted_modes(output_path)
        return
    
    # Handle copy command
    if args.command == 'copy':
        if not args.modes:
            logger.error("Error: Please specify destination: 'remote' or 'local'")
            logger.info("Example: python3 convert_modes.py copy remote")
            logger.info("Example: python3 convert_modes.py copy local")
            sys.exit(1)
        destination = args.modes[0]
        if destination not in ['remote', 'local']:
            logger.error(f"Error: Invalid destination '{destination}'. Must be 'remote' or 'local'")
            sys.exit(1)
        copy_to_vscode(output_path, destination)
        return
    
    # Handle convert command
    if args.command == 'convert':
        if not args.modes:
            logger.error("Error: Please specify mode slugs to convert or use 'all'")
            logger.info("Example: python3 convert_modes.py convert all")
            logger.info("Example: python3 convert_modes.py convert code-skeptic architect")
            sys.exit(1)
        
        convert_modes(source_path, output_path, args.modes)


if __name__ == '__main__':
    main()