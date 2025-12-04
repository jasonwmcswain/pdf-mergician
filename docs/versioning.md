# Version Management

pdf-mergician uses a date-based versioning system with the format: **YYYY.MM.DD.x**

## Version Format

- **YYYY** - Four-digit year
- **MM** - Two-digit month (01-12)
- **DD** - Two-digit day (01-31)
- **x** - Incremental build number (starts at 1, increments for each build on the same day)

### Examples

- `2024.12.03.1` - First build on December 3, 2024
- `2024.12.03.2` - Second build on December 3, 2024
- `2024.12.04.1` - First build on December 4, 2024

## Why Date-Based Versioning?

Date-based versioning provides several benefits:

1. **Transparency** - Anyone can immediately see when a version was released
2. **Simplicity** - No need to decide between major/minor/patch
3. **Chronological** - Versions naturally sort by date
4. **Predictable** - Easy to understand and remember
5. **Flexible** - Multiple builds per day supported

## Version Management Commands

### Show Current Version

```bash
# Using make
make version-show
# or
make version

# Using Python directly
python version.py show
```

Output:
```
Current version: 2024.12.03.1
  Date: 2024.12.03
  Build: 1
```

### Bump Version

Increment the version to the next build number:

```bash
# Using make
make version-bump

# Using Python directly
python version.py bump
```

Output:
```
✓ Version bumped to 2024.12.03.2
  • Updated pyproject.toml
  • Updated merge_pdf/__init__.py
```

**Behavior:**
- If it's the same day: increments build number (1 → 2 → 3...)
- If it's a new day: resets to build 1

### Reset Version State

Reset the version tracking (useful for testing):

```bash
python version.py reset
```

## Automated Version Bumping

The version is automatically bumped when you run:

```bash
make package
```

This command:
1. Bumps the version
2. Runs linting
3. Runs tests
4. Builds the package

## Version State File

Version state is tracked in `.version_state.json`:

```json
{
  "date": "2024.12.03",
  "build": 1
}
```

**Important:** This file is in `.gitignore` and should NOT be committed to version control. Each developer/environment maintains their own version state.

## Integration with Build Process

### Manual Build Workflow

```bash
# 1. Bump version
make version-bump

# 2. Build package
make build

# 3. Publish
make publish
```

### Automated Build Workflow

```bash
# All in one command
make package
```

## Version in Code

The version is stored in two places:

1. **pyproject.toml**
```toml
[project]
version = "2024.12.03.1"
```

2. **merge_pdf/__init__.py**
```python
__version__ = "2024.12.03.1"
```

Access the version in your code:

```python
import merge_pdf
print(merge_pdf.__version__)  # "2024.12.03.1"
```

## CI/CD Integration

### GitHub Actions

For automated builds, you can integrate version bumping into your workflow:

```yaml
- name: Bump version
  run: python version.py bump

- name: Build package
  run: python -m build

- name: Publish to PyPI
  run: twine upload dist/*
```

### Pre-commit Hook

Add to `.git/hooks/pre-commit`:

```bash
#!/bin/bash
# Auto-bump version on commit
python version.py bump
git add pyproject.toml merge_pdf/__init__.py
```

## Best Practices

1. **Bump before building** - Always bump version before creating a distribution
2. **One version per release** - Don't reuse version numbers
3. **Track in changelog** - Update CHANGELOG.md with each version
4. **Test before publishing** - Always test the build before publishing to PyPI

## Comparison with Semantic Versioning

| Aspect | Date-Based (YYYY.MM.DD.x) | Semantic (X.Y.Z) |
|--------|---------------------------|------------------|
| Clarity | Immediately shows release date | Shows compatibility info |
| Simplicity | Very simple | Requires interpretation |
| Sorting | Natural chronological | Natural numerical |
| Breaking changes | Not indicated | Major version bump |
| Use case | Rapid releases, continuous deployment | Traditional versioning |

## Migration from Semantic Versioning

If you were previously using semantic versioning (e.g., `1.0.0`), the migration is straightforward:

1. Run `python version.py bump` to generate first date-based version
2. Update CHANGELOG.md to note the versioning change
3. Continue with date-based versioning going forward

## Troubleshooting

### Version not updating

**Problem:** Running `version-bump` doesn't update files

**Solution:**
1. Check file permissions
2. Ensure `pyproject.toml` and `merge_pdf/__init__.py` exist
3. Run with verbose output: `python version.py bump`

### Build number not incrementing

**Problem:** Build number stays at 1

**Solution:**
1. Check if `.version_state.json` exists
2. Ensure the script has write permissions
3. Try `python version.py reset` then `python version.py bump`

### Wrong date in version

**Problem:** Version shows incorrect date

**Solution:**
- Check system date/time settings
- The version uses local system time

## Examples

### Daily Release Cycle

```bash
# Morning build
make version-bump  # 2024.12.03.1
make build

# Afternoon hotfix
make version-bump  # 2024.12.03.2
make build

# Next day
make version-bump  # 2024.12.04.1
make build
```

### Multiple Developers

Each developer maintains their own version state:

**Developer A:**
```bash
make version-bump  # 2024.12.03.1 (local)
```

**Developer B:**
```bash
make version-bump  # 2024.12.03.1 (local)
```

**CI/CD:**
```bash
make version-bump  # 2024.12.03.1 (CI environment)
```

The actual published version is determined by the CI/CD environment.

## See Also

- [Build Process](../README.md#development)
- [Publishing Guide](../CONTRIBUTING.md#release-process)
- [Changelog](../CHANGELOG.md)

