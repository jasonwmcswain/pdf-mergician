# Installation Guide

This guide covers various ways to install `pdf-mergician`.

---

## Quick Install

The simplest way to install pdf-mergician is via pip:

```bash
pip install pdf-mergician
```

---

## Installation Methods

### From PyPI (Recommended)

Install the latest stable release from PyPI:

```bash
pip install pdf-mergician
```

Upgrade to the latest version:

```bash
pip install --upgrade pdf-mergician
```

Install a specific version:

```bash
pip install pdf-mergician==0.1.0
```

### From Source

Install the latest development version from GitHub:

```bash
pip install git+https://github.com/jmcswain/pdf-mergician.git
```

Or clone and install:

```bash
git clone https://github.com/jmcswain/pdf-mergician.git
cd pdf-mergician
pip install .
```

### Development Installation

For contributing or development:

```bash
git clone https://github.com/jmcswain/pdf-mergician.git
cd pdf-mergician
pip install -e ".[dev]"
```

Or using make:

```bash
make dev-install
```

---

## Virtual Environments

It's recommended to use a virtual environment:

### Using venv

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install pdf-mergician
pip install pdf-mergician
```

### Using conda

```bash
# Create environment
conda create -n pdf-mergician python=3.11

# Activate
conda activate pdf-mergician

# Install
pip install pdf-mergician
```

---

## System Requirements

### Python Version

- **Python 3.8 or higher** is required
- Tested on Python 3.8, 3.9, 3.10, 3.11, and 3.12

Check your Python version:

```bash
python --version
```

### Operating Systems

pdf-mergician works on:
- **Linux** (Ubuntu, Debian, Fedora, etc.)
- **macOS** (10.15 Catalina and later)
- **Windows** (10 and later)

### Dependencies

pdf-mergician requires:
- [pypdf](https://github.com/py-pdf/pypdf) >= 4.0.0
- [click](https://click.palletsprojects.com/) >= 8.1.0

These are installed automatically when you install pdf-mergician.

---

## Verification

Verify the installation:

```bash
# Check version
pdf-mergician --version

# Run help
pdf-mergician --help

# Test basic functionality
pdf-mergician merge test.pdf file1.pdf file2.pdf
```

---

## Troubleshooting

### Permission Errors

If you get permission errors on Linux/Mac:

```bash
pip install --user pdf-mergician
```

Or use a virtual environment (recommended).

### Command Not Found

If `pdf-mergician` command is not found after installation:

1. Check if the script directory is in your PATH:
   ```bash
   python -m site --user-base
   ```

2. Add to PATH (Linux/Mac):
   ```bash
   export PATH="$PATH:$(python -m site --user-base)/bin"
   ```

3. Or run directly:
   ```bash
   python -m merge_pdf.cli --help
   ```

### Dependency Conflicts

If you have dependency conflicts:

```bash
# Create a fresh virtual environment
python -m venv fresh_env
source fresh_env/bin/activate  # or fresh_env\Scripts\activate on Windows
pip install pdf-mergician
```

### Old pip Version

Update pip if you have issues:

```bash
pip install --upgrade pip
pip install pdf-mergician
```

---

## Uninstallation

To uninstall pdf-mergician:

```bash
pip uninstall pdf-mergician
```

---

## Docker (Optional)

You can also use pdf-mergician in a Docker container:

```dockerfile
FROM python:3.11-slim

RUN pip install pdf-mergician

WORKDIR /pdfs

ENTRYPOINT ["pdf-mergician"]
```

Build and use:

```bash
docker build -t pdf-mergician .
docker run -v $(pwd):/pdfs pdf-mergician merge output.pdf file1.pdf file2.pdf
```

---

## Next Steps

After installation:

1. Read the [Quick Start](../README.md#quick-start) guide
2. Explore [CLI Documentation](cli.md)
3. Check out [Examples](examples.md)
4. Learn the [Python API](api.md)

---

## Getting Help

If you encounter issues:

1. Check [Troubleshooting](#troubleshooting) above
2. Search [GitHub Issues](https://github.com/jmcswain/pdf-mergician/issues)
3. Open a new issue with details about your problem

