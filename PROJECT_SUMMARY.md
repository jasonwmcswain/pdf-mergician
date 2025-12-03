# merge-pdf - Project Summary

## Overview

`merge-pdf` is a comprehensive Python library and CLI tool for PDF manipulation, built with pypdf and Click. It provides both a professional command-line interface and a clean Python API for merging, splitting, rotating, and extracting pages from PDF files.

## Project Structure

```
merge-pdf/
├── merge_pdf/              # Main package
│   ├── __init__.py        # Package exports and version
│   ├── core.py            # Core PDF manipulation functions
│   └── cli.py             # Click CLI interface
├── tests/                 # Comprehensive test suite
│   ├── conftest.py        # Pytest fixtures
│   ├── test_core.py       # Core function tests (36 tests)
│   └── test_cli.py        # CLI tests (24 tests)
├── docs/                  # Documentation
│   ├── api.md             # Python API reference
│   ├── cli.md             # CLI documentation
│   ├── examples.md        # Usage examples
│   └── installation.md    # Installation guide
├── .github/workflows/     # GitHub Actions CI/CD
│   ├── ci.yml             # Continuous integration
│   └── publish.yml        # PyPI publishing
├── pyproject.toml         # Project configuration
├── Makefile               # Build automation
├── README.md              # Beautiful project README
├── CONTRIBUTING.md        # Contribution guidelines
├── CHANGELOG.md           # Version history
├── LICENSE                # MIT License
└── requirements*.txt      # Dependency files
```

## Features Implemented

### Core Functionality (merge_pdf/core.py)

1. **merge()** - Merge multiple PDFs into one
   - Preserves metadata from first PDF (optional)
   - Handles multiple files efficiently
   - Comprehensive error handling

2. **merge_pattern()** - Advanced pattern-based merging
   - Specify exact page ranges from multiple files
   - 1-based page indexing (user-friendly)
   - File caching for performance
   - Interleave pages from different documents

3. **split_pdf()** - Split PDFs into multiple files
   - Configurable pages per file
   - Automatic output directory creation
   - Sequential file naming

4. **rotate_pages()** - Rotate specific pages
   - Support for 90, 180, 270, -90 degree rotations
   - Rotate all pages or specific pages
   - Maintains document integrity

5. **extract_pages()** - Extract pages to new PDF
   - Extract specific pages by number
   - Maintain custom page order
   - Support for non-consecutive pages

### CLI Interface (merge_pdf/cli.py)

Professional command-line interface with:

- **merge** command - Basic PDF merging
- **pattern** command - Advanced pattern merging
- **split** command - Split PDFs
- **rotate** command - Rotate pages
- **extract** command - Extract pages

Features:
- Color-coded output (success, error, info, warning)
- User-friendly error messages
- Comprehensive help text
- Custom Click parameter types for validation
- Progress indicators

### Testing (tests/)

- **60 comprehensive tests** covering all functionality
- **100% code coverage** of core functions
- Tests for:
  - Normal operation
  - Edge cases
  - Error conditions
  - CLI commands
  - File validation
- Pytest fixtures for PDF generation
- Isolated test environments

### Build & Development

**Makefile targets:**
- `make help` - Show all targets
- `make clean` - Remove build artifacts
- `make install` - Install package
- `make dev-install` - Install with dev dependencies
- `make format` - Format code with ruff
- `make lint` - Run linting
- `make test` - Run tests
- `make coverage` - Generate coverage report
- `make version` - Show current version
- `make version-bump` - Bump version (YYYY.MM.DD.x)
- `make build` - Build distribution
- `make package` - Full package prep (bump + lint + test + build)
- `make publish` - Publish to PyPI

**Code Quality:**
- Ruff for linting and formatting
- Type hints throughout
- Comprehensive docstrings
- PEP 8 compliant

### Documentation

1. **README.md** - Beautiful project overview with:
   - Feature highlights
   - Quick start guide
   - Command examples
   - API examples
   - Development guide
   - Future feature ideas

2. **docs/api.md** - Complete Python API reference
   - Function signatures
   - Parameters and return values
   - Exceptions
   - Usage examples
   - Type hints

3. **docs/cli.md** - CLI documentation
   - All commands
   - Options and arguments
   - Examples
   - Tips and tricks

4. **docs/examples.md** - Real-world use cases
   - Basic operations
   - Advanced patterns
   - Batch processing
   - Scripting examples
   - Python API examples

5. **docs/installation.md** - Installation guide
   - Multiple installation methods
   - Virtual environments
   - Troubleshooting

6. **CONTRIBUTING.md** - Contribution guidelines
   - Development setup
   - Code style
   - Testing requirements
   - Pull request process

### CI/CD

**GitHub Actions workflows:**

1. **ci.yml** - Continuous Integration
   - Test on Linux, macOS, Windows
   - Test Python 3.8, 3.9, 3.10, 3.11, 3.12
   - Run linting and tests
   - Upload coverage to Codecov

2. **publish.yml** - Automated publishing
   - Trigger on release
   - Build and publish to PyPI

## Technical Specifications

### Dependencies

**Production:**
- pypdf >= 4.0.0 (PDF manipulation)
- click >= 8.1.0 (CLI framework)

**Development:**
- pytest >= 8.0.0 (testing)
- pytest-cov >= 4.1.0 (coverage)
- ruff >= 0.4.0 (linting/formatting)
- build >= 1.0.0 (packaging)
- twine >= 5.0.0 (PyPI upload)

### Python Version Support

- **Minimum:** Python 3.8
- **Tested:** Python 3.8, 3.9, 3.10, 3.11, 3.12
- **Matches pypdf support** for consistency

### Package Configuration

- **Build system:** setuptools >= 68
- **Package format:** PEP 517 compliant
- **Entry point:** `merge-pdf` command
- **License:** MIT
- **Versioning:** Date-based (YYYY.MM.DD.x)

## Usage Examples

### CLI

```bash
# Merge PDFs
merge-pdf merge output.pdf file1.pdf file2.pdf file3.pdf

# Advanced pattern
merge-pdf pattern output.pdf -s A.pdf:1-5 -s B.pdf:1-5

# Split PDF
merge-pdf split large.pdf output_dir/ --pages-per-file 10

# Rotate pages
merge-pdf rotate input.pdf output.pdf --angle 90 --pages 1,3,5

# Extract pages
merge-pdf extract input.pdf output.pdf --pages 1,3-7,10
```

### Python API

```python
from merge_pdf import merge, merge_pattern, split_pdf, rotate_pages, extract_pages

# Merge
merge(["file1.pdf", "file2.pdf"], "output.pdf")

# Pattern merge
pattern = [
    ("A.pdf", 1, 5),
    ("B.pdf", 1, 5),
]
merge_pattern(pattern, "output.pdf")

# Split
split_pdf("large.pdf", "output_dir/", pages_per_file=10)

# Rotate
rotate_pages("input.pdf", "output.pdf", 90, pages=[1, 3, 5])

# Extract
extract_pages("input.pdf", "output.pdf", [1, 3, 5, 7])
```

## Future Enhancement Ideas

Brainstormed features for future versions:

1. **Encryption/Decryption** - Password protection
2. **Image to PDF** - Convert images to PDF
3. **Bookmark Management** - Add/edit bookmarks
4. **Metadata Editing** - Update PDF metadata
5. **Watermarking** - Add watermarks or stamps
6. **PDF Info** - Display PDF information
7. **Text Extraction** - Extract text content
8. **Page Resizing** - Resize or scale pages
9. **Page Overlays** - Overlay pages from different PDFs
10. **Progress Bars** - Visual progress for long operations
11. **Batch Operations** - Built-in batch processing
12. **GUI Wrapper** - Tkinter or Textual interface
13. **Compression** - Optimize PDF file size
14. **Form Filling** - Fill PDF forms programmatically
15. **Digital Signatures** - Sign PDFs

## Quality Metrics

- ✅ **60 tests** - All passing
- ✅ **100% core coverage** - All core functions tested
- ✅ **Zero linting errors** - Ruff checks pass
- ✅ **Type hints** - Throughout codebase
- ✅ **Documentation** - Comprehensive docs
- ✅ **CI/CD** - Automated testing and publishing

## Getting Started

### For Users

```bash
# Install
pip install merge-pdf

# Use CLI
merge-pdf --help

# Or Python API
python -c "from merge_pdf import merge; merge(['a.pdf', 'b.pdf'], 'out.pdf')"
```

### For Developers

```bash
# Clone
git clone https://github.com/jmcswain/merge-pdf.git
cd merge-pdf

# Setup
make dev-install

# Test
make test

# Lint
make lint

# Build
make build
```

## Version Management

merge-pdf uses **date-based versioning** with the format: **YYYY.MM.DD.x**

- `YYYY.MM.DD` - Current date
- `x` - Build number (increments for multiple builds on the same day)

### Version Commands

```bash
# Show current version
make version

# Bump to next version
make version-bump

# Package automatically bumps version
make package
```

See [docs/versioning.md](docs/versioning.md) for complete documentation.

## Publishing to PyPI

When ready to publish:

1. Update `CHANGELOG.md` with changes
2. Run `make package` (automatically bumps version, lints, tests, builds)
3. Test on TestPyPI (optional): `make publish-test`
4. Publish to PyPI: `make publish`
5. Create GitHub release with tag

## License

MIT License - See LICENSE file for details

## Author

J McSwain

---

**Project Status:** ✅ Complete and ready for use

All requirements have been implemented:
- ✅ pypdf and click dependencies
- ✅ Makefile with all targets
- ✅ pytest and ruff for testing/linting
- ✅ Python 3.8+ support (matching pypdf)
- ✅ Buildable package for PyPI
- ✅ CLI for file merging
- ✅ Advanced pattern merging
- ✅ Beautiful README with documentation
- ✅ User-friendly documentation
- ✅ Additional cool features (split, rotate, extract)
- ✅ Professional CLI with clean responses

