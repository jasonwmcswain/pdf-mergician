# Date-Based Versioning Implementation Summary

## Overview

The merge-pdf project now uses **date-based versioning** with the format: **YYYY.MM.DD.x**

This provides transparency, simplicity, and automatic chronological ordering of releases.

## Format

```
YYYY.MM.DD.x
```

- **YYYY** - Four-digit year (e.g., 2025)
- **MM** - Two-digit month (01-12)
- **DD** - Two-digit day (01-31)
- **x** - Build number (starts at 1, increments for each build on the same day)

### Examples

- `2025.12.03.1` - First build on December 3, 2025
- `2025.12.03.2` - Second build on December 3, 2025
- `2025.12.04.1` - First build on December 4, 2025

## Implementation

### Files Created

1. **version.py** - Version management script
   - Generates date-based versions
   - Tracks build numbers per day
   - Updates version in all necessary files
   - Provides CLI for version management

2. **.version_state.json** - Version state tracking (gitignored)
   - Stores current date and build number
   - Automatically managed by version.py

3. **docs/versioning.md** - Complete versioning documentation

### Files Modified

1. **pyproject.toml** - Updated to use date-based version
2. **merge_pdf/__init__.py** - Updated `__version__` variable
3. **Makefile** - Added version management targets
4. **.gitignore** - Added `.version_state.json`
5. **README.md** - Added version management section
6. **CONTRIBUTING.md** - Updated release process
7. **CHANGELOG.md** - Updated versioning scheme documentation
8. **PROJECT_SUMMARY.md** - Added version management info
9. **tests/test_cli.py** - Updated version test to check format

## Usage

### Show Current Version

```bash
make version
# or
make version-show
# or
python version.py show
```

Output:
```
Current version: 2025.12.03.3
  Date: 2025.12.03
  Build: 3
```

### Bump Version

```bash
make version-bump
# or
python version.py bump
```

Output:
```
✓ Version bumped to 2025.12.03.4
  • Updated pyproject.toml
  • Updated merge_pdf/__init__.py
```

### Automated Bumping

The `make package` command now automatically bumps the version:

```bash
make package
```

This runs:
1. `version-bump` - Increment version
2. `lint` - Run linting
3. `test` - Run tests
4. `build` - Create distribution

## How It Works

### Version State Management

The system maintains state in `.version_state.json`:

```json
{
  "date": "2025.12.03",
  "build": 3
}
```

### Version Bumping Logic

```python
current_date = get_current_date_version()  # e.g., "2025.12.03"
state = load_version_state()

if state["date"] == current_date:
    # Same day: increment build number
    build_number = state["build"] + 1  # 3 -> 4
else:
    # New day: reset to build 1
    build_number = 1

save_version_state(current_date, build_number)
return f"{current_date}.{build_number}"  # "2025.12.03.4"
```

### File Updates

When bumping, the script updates:

1. **pyproject.toml**
```toml
[project]
version = "2025.12.03.4"
```

2. **merge_pdf/__init__.py**
```python
__version__ = "2025.12.03.4"
```

The script uses regex to find and replace only the project version, not other version fields (like `target-version` in ruff config).

## Benefits

### 1. Transparency
Anyone can immediately see when a version was released just by looking at the version number.

### 2. Simplicity
No need to decide between major/minor/patch changes - just bump and go.

### 3. Chronological Ordering
Versions naturally sort by date:
```
2025.12.01.1
2025.12.01.2
2025.12.03.1
2025.12.03.2
```

### 4. Multiple Builds Per Day
Support for hotfixes and multiple releases on the same day.

### 5. No Version Conflicts
Each developer/environment maintains their own version state, preventing conflicts.

## Integration with Workflow

### Development Workflow

```bash
# 1. Make changes
git checkout -b feature/new-feature

# 2. Test locally
make test

# 3. Commit changes
git commit -m "Add new feature"

# 4. Before merging to main
make package  # Auto-bumps version, tests, builds

# 5. Merge and publish
git push origin feature/new-feature
# After merge to main, CI/CD can auto-publish
```

### Release Workflow

```bash
# 1. Update CHANGELOG.md
vim CHANGELOG.md

# 2. Package (auto-bumps version)
make package

# 3. Verify build
ls dist/

# 4. Publish to PyPI
make publish

# 5. Create GitHub release
git tag v$(python version.py show)
git push --tags
```

## Testing

The versioning system includes:

1. **Unit tests** - Test version format in CLI
2. **Linting** - All code passes ruff checks
3. **Integration** - Works with make commands
4. **Manual testing** - Verified bump and show commands

## Comparison with Semantic Versioning

| Feature | Date-Based | Semantic |
|---------|------------|----------|
| Format | YYYY.MM.DD.x | X.Y.Z |
| Indicates release date | ✅ Yes | ❌ No |
| Indicates breaking changes | ❌ No | ✅ Yes |
| Simplicity | ✅ Very simple | ⚠️ Requires interpretation |
| Sorting | ✅ Chronological | ✅ Numerical |
| Best for | Rapid releases, continuous deployment | Traditional versioning |

## Migration Notes

### From Semantic Versioning

Previous versions used semantic versioning (0.1.0). The migration was straightforward:

1. Implemented version.py script
2. Updated pyproject.toml and __init__.py
3. Updated documentation
4. First date-based version: 2025.12.03.1

### Backward Compatibility

PyPI and pip handle date-based versions correctly. Users can still:
- Install specific versions: `pip install merge-pdf==2025.12.03.1`
- Upgrade to latest: `pip install --upgrade merge-pdf`
- Specify version ranges: `merge-pdf>=2025.12.01`

## Troubleshooting

### Version not incrementing

**Problem:** Build number stays the same

**Solution:**
```bash
# Check version state
cat .version_state.json

# Reset if needed
python version.py reset
python version.py bump
```

### Wrong version in files

**Problem:** Version in pyproject.toml doesn't match __init__.py

**Solution:**
```bash
# Re-run bump to sync
python version.py bump
```

### Regex update issues

**Problem:** version.py updated wrong field

**Solution:** The script now uses a more specific regex that only matches the version in the `[project]` section of pyproject.toml.

## Future Enhancements

Potential improvements to the versioning system:

1. **Git integration** - Auto-tag releases
2. **Changelog automation** - Auto-update CHANGELOG.md
3. **Pre-release versions** - Support alpha/beta/rc suffixes
4. **Version validation** - Verify version format before publishing
5. **Rollback support** - Ability to revert to previous version

## Documentation

Complete documentation available in:
- [docs/versioning.md](docs/versioning.md) - Detailed versioning guide
- [README.md](README.md) - Quick start and overview
- [CONTRIBUTING.md](CONTRIBUTING.md) - Release process
- [CHANGELOG.md](CHANGELOG.md) - Version history

## Summary

The date-based versioning system is:
- ✅ Fully implemented and tested
- ✅ Integrated with build system
- ✅ Documented comprehensively
- ✅ Ready for production use

Current version: **2025.12.03.3**

---

**Implementation Date:** December 3, 2025
**Status:** Complete ✅

