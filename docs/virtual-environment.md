# Virtual Environment Guide

This project **requires** using a virtual environment to keep your system Python clean and ensure consistent dependencies.

## 🎯 Why Virtual Environments?

Virtual environments provide:

✅ **Isolation**: Keep project dependencies separate from system Python
✅ **Consistency**: Ensure all developers use the same package versions
✅ **Safety**: Prevent conflicts with other Python projects
✅ **Cleanliness**: Avoid polluting your system Python installation
✅ **Reproducibility**: Easy to recreate the exact development environment

---

## 🚀 Quick Start

### Using Make (Recommended)

The Makefile handles everything automatically:

```bash
# Create virtual environment
make venv

# Install development dependencies
make dev-install

# That's it! All other make commands use the venv automatically
make test
make lint
make build
```

### Manual Setup

If you prefer to manage the virtual environment manually:

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # Unix/macOS
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -e ".[dev]"

# When done, deactivate
deactivate
```

---

## 📁 Virtual Environment Location

This project uses `./venv/` as the virtual environment directory:

```
merge-pdf/
├── venv/              ← Virtual environment (not in git)
│   ├── bin/           ← Executables (python, pip, pytest, etc.)
│   ├── lib/           ← Installed packages
│   └── ...
├── merge_pdf/         ← Source code
├── tests/             ← Tests
├── Makefile           ← Build automation (uses venv/)
└── ...
```

The `venv/` directory is automatically excluded from git via `.gitignore`.

---

## 🔧 Makefile Integration

All Makefile commands automatically use the virtual environment:

### Virtual Environment Variables

```makefile
VENV := ./venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
PYTEST := $(VENV)/bin/pytest
RUFF := $(VENV)/bin/ruff
TWINE := $(VENV)/bin/twine
```

### Automatic venv Creation

Commands that need the virtual environment automatically create it:

```bash
make dev-install  # Creates venv if it doesn't exist, then installs
make test         # Ensures venv exists before running tests
make lint         # Ensures venv exists before linting
```

---

## 📋 Common Commands

### Virtual Environment Management

```bash
# Create virtual environment
make venv

# Remove virtual environment
make venv-clean

# Recreate virtual environment (fresh start)
make venv-clean venv dev-install
```

### Development Commands

```bash
# Install dependencies (creates venv if needed)
make dev-install

# Run tests (uses venv)
make test

# Run linting (uses venv)
make lint

# Build package (uses venv)
make build

# Clean build artifacts (keeps venv)
make clean

# Clean everything including venv
make clean-all
```

---

## 🔍 Verifying Your Setup

### Check if venv exists

```bash
ls -la venv/
# Should show bin/, lib/, etc.
```

### Check Python location

```bash
./venv/bin/python --version
# Should show Python 3.8+
```

### Check installed packages

```bash
./venv/bin/pip list
# Should show merge-pdf, pytest, ruff, etc.
```

### Verify Makefile uses venv

```bash
make version-show
# Should use ./venv/bin/python
```

---

## 🐛 Troubleshooting

### Problem: "Command not found" errors

**Cause**: Virtual environment not created or not activated

**Solution**:
```bash
make venv
make dev-install
```

### Problem: "No module named 'pytest'" (or other package)

**Cause**: Dependencies not installed in venv

**Solution**:
```bash
make dev-install
```

### Problem: Using wrong Python version

**Cause**: System Python being used instead of venv

**Solution**:
```bash
# Verify Makefile is using venv
make help  # Should show "Note: All commands use ./venv/"

# Recreate venv if needed
make venv-clean venv dev-install
```

### Problem: Corrupted virtual environment

**Cause**: Partial installation or interrupted setup

**Solution**:
```bash
# Complete clean and rebuild
make clean-all
make venv
make dev-install
```

### Problem: Different Python version than expected

**Cause**: System Python3 is not the desired version

**Solution**:
```bash
# Use specific Python version
python3.11 -m venv venv  # or python3.10, python3.12, etc.
make dev-install
```

---

## 🎓 Best Practices

### ✅ DO

- **Always use `make venv`** before starting development
- **Use Makefile commands** (they handle venv automatically)
- **Keep venv out of git** (already in `.gitignore`)
- **Recreate venv** if you encounter strange issues
- **Document any manual pip installs** in `pyproject.toml`

### ❌ DON'T

- **Don't commit `venv/`** to git (it's environment-specific)
- **Don't install packages globally** (use venv)
- **Don't mix pip and system package managers** (use pip in venv)
- **Don't share venv** across projects (each project gets its own)
- **Don't manually activate venv** when using Makefile (it's automatic)

---

## 🔄 Workflow Examples

### First-Time Setup

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/merge-pdf.git
cd merge-pdf

# Create venv and install dependencies
make venv
make dev-install

# Verify setup
make test
```

### Daily Development

```bash
# Make changes to code
vim merge_pdf/cli.py

# Run tests
make test

# Fix linting issues
make lint-fix

# Run full validation
make validate
```

### Clean Rebuild

```bash
# Remove everything
make clean-all

# Rebuild from scratch
make venv
make dev-install
make test
```

### Before Committing

```bash
# Full validation
make clean-validate

# Or step by step
make clean
make lint-fix
make lint
make test
make coverage
```

---

## 📊 Virtual Environment Contents

After running `make dev-install`, your venv should contain:

### Core Dependencies
- `pypdf` - PDF manipulation
- `click` - CLI framework

### Development Dependencies
- `pytest` - Testing framework
- `pytest-cov` - Coverage reporting
- `ruff` - Linting and formatting
- `build` - Package building
- `twine` - PyPI publishing

### Build Tools
- `pip` - Package installer
- `setuptools` - Package setup
- `wheel` - Wheel package format

---

## 🔐 Security Considerations

### Why venv is Important for Security

1. **Dependency Isolation**: Malicious packages can't affect system Python
2. **Version Control**: Lock specific versions to prevent supply chain attacks
3. **Audit Trail**: Easy to inspect what's installed (`pip list`)
4. **Clean Removal**: Delete venv to remove all project dependencies

### Best Practices

```bash
# Audit installed packages
./venv/bin/pip list

# Check for known vulnerabilities (requires pip-audit)
./venv/bin/pip install pip-audit
./venv/bin/pip-audit

# Verify package integrity
./venv/bin/pip check
```

---

## 📚 Additional Resources

- [Python venv Documentation](https://docs.python.org/3/library/venv.html)
- [Python Packaging Guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- [Real Python: Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)

---

## ✅ Quick Reference

| Task | Command |
|------|---------|
| Create venv | `make venv` |
| Install dependencies | `make dev-install` |
| Remove venv | `make venv-clean` |
| Rebuild venv | `make venv-clean venv dev-install` |
| Check venv exists | `ls -la venv/` |
| List installed packages | `./venv/bin/pip list` |
| Verify Python version | `./venv/bin/python --version` |

---

**Remember:** The Makefile handles the virtual environment automatically. Just run `make venv` once, then use `make` commands for everything else!

