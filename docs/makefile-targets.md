# Makefile Targets Reference

Complete reference for all available make targets in merge-pdf.

## Quick Reference

```bash
make help           # Show all available targets
make all            # Full pipeline: clean-validate → publish-test → publish
make clean-validate # Full validation from clean slate
make validate       # Quick validation (no clean)
make package        # Prepare package for release
```

## Target Categories

### 🚀 Pipeline Targets

#### `all-test` - TestPyPI Pipeline
**Command:** `make all-test`

**Pipeline:**
```
version-bump → clean → build → lint-fix → lint → coverage → publish-test
```

**Steps:**
1. **version-bump** - Automatically bump version (YYYY.MM.DD.x)
2. **clean** - Remove all build artifacts
3. **build** - Build distribution packages with new version
4. **lint-fix** - Auto-fix linting issues
5. **lint** - Verify code quality
6. **coverage** - Run tests with coverage
7. **publish-test** - Publish to TestPyPI

**Use case:** Test complete release pipeline on TestPyPI before production

**✅ Safe:** Only publishes to TestPyPI (test environment)

---

#### `all` - Full Release Pipeline
**Command:** `make all`

**Pipeline:**
```
version-bump → clean → build → lint-fix → lint → coverage → publish-test → publish
```

**Steps:**
1. **version-bump** - Automatically bump version (YYYY.MM.DD.x)
2. **clean** - Remove all build artifacts
3. **build** - Build distribution packages with new version
4. **lint-fix** - Auto-fix linting issues
5. **lint** - Verify code quality
6. **coverage** - Run tests with coverage
7. **publish-test** - Publish to TestPyPI
8. **publish** - Publish to PyPI (production)

**Use case:** Complete release pipeline from clean state to production

**⚠️ Warning:** This will publish to PyPI! Use with caution.

---

### ✅ Validation Targets

#### `clean-validate` - Full Validation
**Command:** `make clean-validate`

**Pipeline:**
```
clean → build → lint-fix → lint → coverage
```

**Use case:** Full validation from clean slate (recommended before releases)

#### `validate` - Quick Validation
**Command:** `make validate`

**Pipeline:**
```
build → lint-fix → lint → coverage
```

**Use case:** Fast validation during development (no clean)

#### `verify` - Basic Verification
**Command:** `make verify`

**Pipeline:**
```
clean → lint → test
```

**Use case:** Quick verification without building

---

### 📦 Build Targets

#### `build` - Build Distribution
**Command:** `make build`

**Actions:**
- Cleans build artifacts
- Creates wheel and source distribution
- Outputs to `dist/` directory

#### `package` - Prepare for Release
**Command:** `make package`

**Pipeline:**
```
version-bump → lint → test → build
```

**Use case:** Prepare package with version bump

---

### 🧹 Cleanup Targets

#### `clean` - Remove Build Artifacts
**Command:** `make clean`

**Removes:**
- `build/`, `dist/`, `*.egg-info/`
- `.pytest_cache/`, `.ruff_cache/`
- `htmlcov/`, `.coverage`
- `__pycache__/` directories
- `*.pyc`, `*.pyo` files

---

### 🔍 Code Quality Targets

#### `lint` - Run Linter
**Command:** `make lint`

**Checks:**
- Code style (ruff)
- Best practices
- Potential bugs

#### `lint-fix` - Auto-fix Issues
**Command:** `make lint-fix`

**Fixes:**
- Import sorting
- Code formatting
- Simple style issues

#### `format` - Format Code
**Command:** `make format`

**Formats:**
- Python files with ruff
- Consistent style

#### `check-format` - Check Formatting
**Command:** `make check-format`

**Verifies:**
- Code formatting without changes

---

### 🧪 Testing Targets

#### `test` - Run Tests
**Command:** `make test`

**Runs:**
- Creates test fixtures
- Runs all 84 tests
- Shows coverage report

#### `test-quick` - Fast Tests
**Command:** `make test-quick`

**Runs:**
- Creates test fixtures
- Runs tests without coverage
- Faster execution

#### `coverage` - Coverage Report
**Command:** `make coverage`

**Generates:**
- Terminal coverage report
- HTML coverage report (`htmlcov/`)

#### `test-fixtures` - Create Test PDFs
**Command:** `make test-fixtures`

**Creates:**
- Test PDF files in `tests/fixtures/`
- Used by integration tests

---

### 📝 Version Management Targets

#### `version` - Show Version
**Command:** `make version`

**Displays:**
- Current version
- Date and build number

#### `version-show` - Show Version (alias)
**Command:** `make version-show`

**Same as:** `make version`

#### `version-bump` - Bump Version
**Command:** `make version-bump`

**Actions:**
- Increments version (YYYY.MM.DD.x)
- Updates `pyproject.toml`
- Updates `merge_pdf/__init__.py`

---

### 📤 Publishing Targets

#### `publish-test` - Publish to TestPyPI
**Command:** `make publish-test`

**Pipeline:**
```
package → check-dist → upload to TestPyPI
```

**Use case:** Test release before production

#### `publish` - Publish to PyPI
**Command:** `make publish`

**Pipeline:**
```
package → check-dist → upload to PyPI
```

**⚠️ Warning:** Publishes to production! Requires confirmation.

#### `check-dist` - Validate Distribution
**Command:** `make check-dist`

**Validates:**
- Package metadata
- File structure
- PyPI compatibility

---

### 💻 Installation Targets

#### `install` - Install Package
**Command:** `make install`

**Installs:**
- Package in current environment
- Production dependencies only

#### `dev-install` - Development Install
**Command:** `make dev-install`

**Installs:**
- Package in editable mode
- Development dependencies
- Testing tools

---

## Target Comparison

### Validation Targets

| Target | Clean | Build | Lint-Fix | Lint | Coverage | Time |
|--------|-------|-------|----------|------|----------|------|
| `validate` | ❌ | ✅ | ✅ | ✅ | ✅ | ~5s |
| `clean-validate` | ✅ | ✅ | ✅ | ✅ | ✅ | ~8s |
| `verify` | ✅ | ❌ | ❌ | ✅ | ❌ | ~3s |
| `package` | ❌ | ✅ | ❌ | ✅ | ❌ | ~5s |

### Pipeline Targets

| Target | Steps | Publishes | Use Case |
|--------|-------|-----------|----------|
| `all` | 7 | ✅ TestPyPI + PyPI | Full release |
| `clean-validate` | 5 | ❌ | Pre-release validation |
| `package` | 4 | ❌ | Package preparation |

---

## Common Workflows

### Development Workflow

```bash
# 1. Make changes
vim merge_pdf/core.py

# 2. Quick validation
make validate

# 3. If issues, auto-fix
make lint-fix

# 4. Run tests
make test
```

### Pre-Release Workflow

```bash
# 1. Full validation
make clean-validate

# 2. Test on TestPyPI
make publish-test

# 3. Verify installation
pip install -i https://test.pypi.org/simple/ merge-pdf

# 4. If good, publish
make publish
```

### Full Release Pipeline

```bash
# One command does it all!
make all
```

This runs:
1. ✅ Clean build artifacts
2. ✅ Build packages
3. ✅ Fix linting issues
4. ✅ Verify code quality
5. ✅ Run full test suite
6. ✅ Publish to TestPyPI
7. ✅ Publish to PyPI

### Quick Iteration

```bash
# Fast feedback loop
make validate  # No clean, faster
```

---

## Pipeline Visualization

### `make all` - Full Pipeline

```
┌─────────┐
│  clean  │ Remove artifacts
└────┬────┘
     │
┌────▼────┐
│  build  │ Create distributions
└────┬────┘
     │
┌────▼────┐
│lint-fix │ Auto-fix issues
└────┬────┘
     │
┌────▼────┐
│  lint   │ Verify quality
└────┬────┘
     │
┌────▼────┐
│coverage │ Run tests
└────┬────┘
     │
┌────▼────────┐
│publish-test │ Upload to TestPyPI
└────┬────────┘
     │
┌────▼────┐
│ publish │ Upload to PyPI ⚠️
└─────────┘
```

### `make clean-validate` - Validation Only

```
┌─────────┐
│  clean  │ Remove artifacts
└────┬────┘
     │
┌────▼────┐
│  build  │ Create distributions
└────┬────┘
     │
┌────▼────┐
│lint-fix │ Auto-fix issues
└────┬────┘
     │
┌────▼────┐
│  lint   │ Verify quality
└────┬────┘
     │
┌────▼────┐
│coverage │ Run tests
└─────────┘
```

---

## Tips & Best Practices

### 1. Use `validate` for Development
```bash
# Fast feedback during development
make validate
```

### 2. Use `clean-validate` Before Releases
```bash
# Ensure clean build before release
make clean-validate
```

### 3. Test Before Publishing
```bash
# Always test on TestPyPI first
make publish-test
```

### 4. Use `all` for Automated Releases
```bash
# Full pipeline for CI/CD
make all
```

### 5. Check Help When Unsure
```bash
# See all available targets
make help
```

---

## Environment Variables

### Colors

The Makefile uses colored output:
- 🔵 **Blue** - Info messages
- 🟢 **Green** - Success messages
- 🟡 **Yellow** - Progress messages
- 🔴 **Red** - Error/warning messages

### Python Interpreter

Default: `python3`

To use a different Python:
```bash
make test PYTHON=python3.11
```

---

## Troubleshooting

### Build Fails

```bash
# Clean and try again
make clean
make build
```

### Tests Fail

```bash
# Recreate fixtures
make test-fixtures
make test
```

### Linting Errors

```bash
# Auto-fix what's possible
make lint-fix
# Then check remaining issues
make lint
```

### Publishing Fails

```bash
# Verify distribution first
make check-dist
```

---

## See Also

- [README.md](../README.md) - Project overview
- [CONTRIBUTING.md](../CONTRIBUTING.md) - Contribution guidelines
- [docs/versioning.md](versioning.md) - Version management
- [tests/README.md](../tests/README.md) - Testing guide

