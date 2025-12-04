# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

**Note:** Starting with version 2025.12.03.1, this project uses date-based versioning (YYYY.MM.DD.x) instead of semantic versioning.

## [Unreleased]

### Added
- Date-based versioning system (YYYY.MM.DD.x format)
- Automatic version management with `version.py` script
- Version management integrated into Makefile
- Comprehensive versioning documentation

## [2025.12.03.1] - 2025-12-03

### Added
- Initial release of pdf-mergician
- Core PDF manipulation functions:
  - `merge()` - Merge multiple PDFs
  - `merge_pattern()` - Advanced pattern-based merging
  - `split_pdf()` - Split PDFs into multiple files
  - `rotate_pages()` - Rotate specific pages
  - `extract_pages()` - Extract pages to new PDF
- Professional CLI interface with Click:
  - `merge` command for basic merging
  - `pattern` command for advanced merging
  - `split` command for splitting PDFs
  - `rotate` command for rotating pages
  - `extract` command for extracting pages
- Comprehensive test suite with pytest
- Full documentation:
  - README with examples
  - API documentation
  - CLI documentation
  - Usage examples
- Development tooling:
  - Makefile with common tasks
  - Ruff for linting and formatting
  - pytest with coverage reporting
- Python 3.8+ support (matching pypdf)

---

## Version History

### Versioning Scheme (Current)

**Date-Based Versioning: YYYY.MM.DD.x**

- **YYYY.MM.DD**: Release date
- **x**: Build number (increments for multiple builds on the same day)

### Previous Versioning (Deprecated)

Versions prior to 2025.12.03.1 used semantic versioning (X.Y.Z)

### Upgrade Notes

When upgrading between versions, check this section for any breaking changes or migration steps.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for information on how to contribute to this project.

---

[Unreleased]: https://github.com/jmcswain/pdf-mergician/compare/v2025.12.03.1...HEAD
[2025.12.03.1]: https://github.com/jmcswain/pdf-mergician/releases/tag/v2025.12.03.1

