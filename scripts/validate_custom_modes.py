#!/usr/bin/env python3
"""Validate custom_modes.yaml against Roo Code requirements.

This script performs schema-style validation that matches the documented
custom modes format at https://docs.roocode.com/features/custom-modes.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any, Dict, Sequence

import yaml

ALLOWED_PERMISSIONS = {"read", "edit", "browser", "command", "mcp"}
SLUG_PATTERN = re.compile(r"^[a-z0-9-]+$")


class ValidationError(Exception):
    """Raised when validation fails."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


def _ensure(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def validate_groups(slug: str, groups: Sequence[Any]) -> None:
    _ensure(isinstance(groups, Sequence) and not isinstance(groups, (str, bytes)),
            f"{slug}: groups must be a list")
    _ensure(groups, f"{slug}: groups must not be empty")

    for idx, entry in enumerate(groups, start=1):
        prefix = f"{slug}: groups[{idx}]"
        if isinstance(entry, str):
            _ensure(entry in ALLOWED_PERMISSIONS,
                    f"{prefix} must be one of {sorted(ALLOWED_PERMISSIONS)}; got {entry!r}")
            continue

        if isinstance(entry, Sequence) and not isinstance(entry, (str, bytes)):
            _ensure(len(entry) == 2,
                    f"{prefix} tuple must contain exactly two items: ['edit', {{options}}]")
            _ensure(entry[0] == "edit",
                    f"{prefix}[0] must be 'edit' when using tuple syntax")
            options = entry[1]
            _ensure(isinstance(options, dict),
                    f"{prefix}[1] must be a mapping of options")
            allowed_keys = {"fileRegex", "description"}
            extra = set(options) - allowed_keys
            _ensure(not extra,
                    f"{prefix}[1] contains unsupported keys: {sorted(extra)}")
            _ensure("fileRegex" in options,
                    f"{prefix}[1] must include 'fileRegex'")
            _ensure(isinstance(options["fileRegex"], str) and options["fileRegex"].strip(),
                    f"{prefix}[1].fileRegex must be a non-empty string")
            if "description" in options:
                _ensure(isinstance(options["description"], str) and options["description"].strip(),
                        f"{prefix}[1].description must be a non-empty string when provided")
            continue

        raise ValidationError(f"{prefix} must be a permission string or ['edit', {{options}}]")


def validate_rules_files(slug: str, rules_files: Sequence[Any]) -> None:
    _ensure(isinstance(rules_files, Sequence) and not isinstance(rules_files, (str, bytes)),
            f"{slug}: rulesFiles must be a list")
    _ensure(rules_files,
            f"{slug}: rulesFiles must not be empty when provided")

    for idx, entry in enumerate(rules_files, start=1):
        prefix = f"{slug}: rulesFiles[{idx}]"
        _ensure(isinstance(entry, dict), f"{prefix} must be a mapping")
        allowed_keys = {"relativePath", "content"}
        extra = set(entry) - allowed_keys
        _ensure(not extra, f"{prefix} contains unsupported keys: {sorted(extra)}")
        for key in allowed_keys:
            _ensure(key in entry, f"{prefix} missing required key '{key}'")
            _ensure(isinstance(entry[key], str) and entry[key].strip(),
                    f"{prefix}.{key} must be a non-empty string")


def validate_mode(mode: Dict[str, Any], seen_slugs: set[str]) -> None:
    _ensure(isinstance(mode, dict), "Each custom mode must be a mapping")
    slug = mode.get("slug")
    _ensure(isinstance(slug, str) and slug.strip(),
            "Mode is missing a non-empty 'slug'")
    _ensure(SLUG_PATTERN.fullmatch(slug),
            f"{slug}: slug must match {SLUG_PATTERN.pattern}")
    _ensure(slug not in seen_slugs, f"{slug}: duplicate slug detected")
    seen_slugs.add(slug)

    allowed_keys = {
        "slug",
        "name",
        "description",
        "roleDefinition",
        "whenToUse",
        "customInstructions",
        "groups",
        "rulesFiles",
    }
    extra = set(mode) - allowed_keys
    _ensure(not extra, f"{slug}: contains unsupported keys: {sorted(extra)}")

    missing = {"name", "roleDefinition", "groups"} - set(mode)
    _ensure(not missing, f"{slug}: missing required keys: {sorted(missing)}")

    name = mode["name"]
    _ensure(isinstance(name, str) and 1 <= len(name) <= 100,
            f"{slug}: name must be a non-empty string up to 100 characters")

    role_definition = mode["roleDefinition"]
    _ensure(isinstance(role_definition, str) and len(role_definition.strip()) >= 10,
            f"{slug}: roleDefinition must be at least 10 characters")

    if "description" in mode:
        _ensure(isinstance(mode["description"], str) and mode["description"].strip(),
                f"{slug}: description must be a non-empty string when provided")

    if "whenToUse" in mode:
        _ensure(isinstance(mode["whenToUse"], str) and mode["whenToUse"].strip(),
                f"{slug}: whenToUse must be a non-empty string when provided")

    if "customInstructions" in mode:
        _ensure(isinstance(mode["customInstructions"], str) and mode["customInstructions"].strip(),
                f"{slug}: customInstructions must be a non-empty string when provided")

    validate_groups(slug, mode["groups"])

    if "rulesFiles" in mode:
        validate_rules_files(slug, mode["rulesFiles"])


def validate_document(document: Any) -> None:
    _ensure(isinstance(document, dict), "Top-level document must be a mapping")
    allowed_keys = {"customModes"}
    extra = set(document) - allowed_keys
    _ensure(not extra, f"Top-level contains unsupported keys: {sorted(extra)}")
    _ensure("customModes" in document, "Document must include 'customModes'")

    modes = document["customModes"]
    _ensure(isinstance(modes, Sequence) and not isinstance(modes, (str, bytes)),
            "customModes must be a list")
    _ensure(modes, "customModes must not be empty")

    seen_slugs: set[str] = set()
    for mode in modes:
        validate_mode(mode, seen_slugs)


def run(path: Path) -> int:
    try:
        raw = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"error: {path} not found", file=sys.stderr)
        return 2

    try:
        document = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        print(f"YAML parse error in {path}: {exc}", file=sys.stderr)
        return 1

    try:
        validate_document(document)
    except ValidationError as exc:
        print(f"validation error: {exc.message}", file=sys.stderr)
        return 1

    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Roo Code custom modes file")
    parser.add_argument(
        "path",
        type=Path,
        nargs="?",
        default=Path("custom_modes.yaml"),
        help="Path to custom_modes.yaml (defaults to ./custom_modes.yaml)",
    )
    args = parser.parse_args(argv)
    return run(args.path)


if __name__ == "__main__":
    sys.exit(main())
