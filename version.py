#!/usr/bin/env python3
"""
Version management script for pdf-mergician.

Generates and manages versions in YYYY.MM.DD.x format where:
- YYYY.MM.DD is the current date
- x is an incremental build number (starting at 1) for multiple builds on the same day
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

VERSION_FILE = Path(__file__).parent / ".version_state.json"
PYPROJECT_FILE = Path(__file__).parent / "pyproject.toml"
INIT_FILE = Path(__file__).parent / "merge_pdf" / "__init__.py"


def get_current_date_version():
    """Get the date portion of the version (YYYY.MM.DD)."""
    now = datetime.now()
    return f"{now.year}.{now.month:02d}.{now.day:02d}"


def load_version_state():
    """Load the version state from file."""
    if VERSION_FILE.exists():
        with VERSION_FILE.open("r") as f:
            return json.load(f)
    return {"date": None, "build": 0}


def save_version_state(date_version, build_number):
    """Save the version state to file."""
    state = {"date": date_version, "build": build_number}
    with VERSION_FILE.open("w") as f:
        json.dump(state, f, indent=2)


def get_next_version():
    """
    Get the next version number.

    Returns:
        str: Version in YYYY.MM.DD.x format
    """
    current_date = get_current_date_version()
    state = load_version_state()

    # Same day: increment build number, new day: reset to 1
    build_number = state["build"] + 1 if state["date"] == current_date else 1

    save_version_state(current_date, build_number)
    return f"{current_date}.{build_number}"


def get_current_version():
    """
    Get the current version without incrementing.

    Returns:
        str: Current version in YYYY.MM.DD.x format
    """
    state = load_version_state()
    if state["date"] is None:
        # No version yet, return today's first version
        current_date = get_current_date_version()
        return f"{current_date}.1"
    return f"{state['date']}.{state['build']}"


def update_version_in_file(file_path, version, pattern, replacement):
    """Update version in a file using regex."""
    content = file_path.read_text()
    new_content = re.sub(pattern, replacement.format(version=version), content)

    if content != new_content:
        file_path.write_text(new_content)
        return True
    return False


def bump_version():
    """
    Bump the version and update all files.

    Returns:
        str: The new version number
    """
    new_version = get_next_version()

    # Update pyproject.toml (only in [project] section)
    pyproject_updated = update_version_in_file(
        PYPROJECT_FILE, new_version, r'(\[project\][^\[]*version\s*=\s*)"[^"]+"', r'\1"{version}"'
    )

    # Update __init__.py
    init_updated = update_version_in_file(
        INIT_FILE, new_version, r'__version__\s*=\s*"[^"]+"', '__version__ = "{version}"'
    )

    print(f"✓ Version bumped to {new_version}")
    if pyproject_updated:
        print(f"  • Updated {PYPROJECT_FILE.name}")
    if init_updated:
        print(f"  • Updated {INIT_FILE.relative_to(Path(__file__).parent)}")

    return new_version


def show_version():
    """Display the current version."""
    version = get_current_version()
    print(f"Current version: {version}")

    state = load_version_state()
    if state["date"]:
        print(f"  Date: {state['date']}")
        print(f"  Build: {state['build']}")

    return version


def reset_version():
    """Reset version state (useful for testing)."""
    if VERSION_FILE.exists():
        VERSION_FILE.unlink()
    print("✓ Version state reset")


def main():
    """Main entry point for version management."""
    min_args = 2
    if len(sys.argv) < min_args:
        print("Usage: python version.py [bump|show|reset]")
        print()
        print("Commands:")
        print("  bump   - Increment version and update files")
        print("  show   - Display current version")
        print("  reset  - Reset version state")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "bump":
        bump_version()
    elif command == "show":
        show_version()
    elif command == "reset":
        reset_version()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
