# Documentation Index

Welcome to the `merge-pdf` documentation! This index will help you find the information you need.

## 📚 Quick Navigation

### Getting Started
- 🚀 [Installation Guide](installation.md) - Install and set up merge-pdf
- ⚡ [Quick Start](../QUICKSTART.md) - Get started in 5 minutes
- 📖 [Usage Guide](usage.md) - CLI commands and options
- 💡 [Examples](examples.md) - Real-world use cases

### Core Documentation
- 🎯 [CLI Reference](cli.md) - Complete command-line interface documentation
- 🐍 [Python API Reference](api.md) - Use merge-pdf as a Python library
- 📋 [Project Summary](../PROJECT_SUMMARY.md) - Technical overview

### Publishing & Deployment

#### GitHub Actions (Recommended) ⭐
- 🚀 **[Quick Start: GitHub Publishing](../GITHUB_PUBLISHING_QUICKSTART.md)** - 5-minute setup
- 📖 **[Complete Guide: Trusted Publishers](github-trusted-publisher.md)** - Detailed OIDC setup
- 📊 **[Publishing Summary](../GITHUB_PUBLISHING_SUMMARY.md)** - Overview & cheat sheets
- 🎨 **[Visual Publishing Guide](publishing-visual-guide.md)** - Step-by-step with diagrams
- ⚖️ **[Publishing Comparison](publishing-comparison.md)** - OIDC vs API tokens

#### Traditional Publishing
- 🔑 **[PyPI Credentials Setup](pypi-setup.md)** - API token configuration
- 📋 **[PyPI Quick Reference](../PYPI_QUICKSTART.md)** - Quick reference card

### Development
- 🤝 [Contributing Guide](../CONTRIBUTING.md) - How to contribute
- 🐍 [Virtual Environment Guide](virtual-environment.md) - Setup and usage
- 🔧 [Makefile Targets](makefile-targets.md) - Build automation
- 📅 [Versioning System](versioning.md) - Date-based versioning (YYYY.MM.DD.x)
- 📝 [Changelog](../CHANGELOG.md) - Version history
- 🧪 [Testing Summary](../TESTING_SUMMARY.md) - Test infrastructure

### GitHub Actions
- 🔄 [Workflows Documentation](../.github/README.md) - CI/CD workflows
- ✅ [CI Workflow](../.github/workflows/ci.yml) - Continuous integration
- 🚀 [Publish Workflow](../.github/workflows/publish.yml) - Production publishing
- 🧪 [Test Publish Workflow](../.github/workflows/publish-test.yml) - TestPyPI publishing

## 📖 Documentation by Topic

### For Users

| What do you want to do? | Read this |
|-------------------------|-----------|
| Install merge-pdf | [Installation Guide](installation.md) |
| Learn basic commands | [Quick Start](../QUICKSTART.md) |
| See command examples | [Examples](examples.md) |
| Use as Python library | [API Reference](api.md) |
| Understand all CLI options | [CLI Reference](cli.md) |

### For Contributors

| What do you want to do? | Read this |
|-------------------------|-----------|
| Set up dev environment | [Contributing Guide](../CONTRIBUTING.md) |
| Understand virtual environments | [Virtual Environment Guide](virtual-environment.md) |
| Run tests | [Testing Summary](../TESTING_SUMMARY.md) |
| Understand build process | [Makefile Targets](makefile-targets.md) |
| Submit a pull request | [Contributing Guide](../CONTRIBUTING.md) |

### For Maintainers

| What do you want to do? | Read this |
|-------------------------|-----------|
| Publish to PyPI (GitHub) | [GitHub Publishing Quick Start](../GITHUB_PUBLISHING_QUICKSTART.md) |
| Publish to PyPI (Manual) | [PyPI Credentials Setup](pypi-setup.md) |
| Understand versioning | [Versioning System](versioning.md) |
| Configure workflows | [Workflows Documentation](../.github/README.md) |
| Troubleshoot publishing | [Trusted Publishers Guide](github-trusted-publisher.md#troubleshooting) |

## 🎯 Popular Topics

### Publishing to PyPI

We **strongly recommend** using **Trusted Publishers** (OpenID Connect) for secure, credential-free publishing:

1. **Quick Start**: [5-Minute Setup Guide](../GITHUB_PUBLISHING_QUICKSTART.md)
2. **Complete Guide**: [Trusted Publishers Documentation](github-trusted-publisher.md)
3. **Visual Guide**: [Step-by-Step with Diagrams](publishing-visual-guide.md)
4. **Comparison**: [OIDC vs API Tokens](publishing-comparison.md)

**Why Trusted Publishers?**
- ✅ No API tokens to manage
- ✅ Short-lived credentials (15 minutes)
- ✅ Enhanced security
- ✅ PyPI recommended approach

### CLI Examples

Common use cases with copy-paste examples:

```bash
# Merge multiple PDFs
merge-pdf merge output.pdf file1.pdf file2.pdf file3.pdf

# Interleave pages from two documents
merge-pdf pattern comparison.pdf -s doc1.pdf:1-5 -s doc2.pdf:1-5

# Split into individual pages
merge-pdf split large.pdf output_dir/

# Rotate pages
merge-pdf rotate input.pdf output.pdf --angle 90

# Extract specific pages
merge-pdf extract input.pdf output.pdf --pages 1,3,5-10
```

See [Examples](examples.md) for 50+ real-world use cases!

### Python API

Use merge-pdf programmatically:

```python
from merge_pdf import merge, merge_pattern, split_pdf, rotate_pages, extract_pages

# Merge PDFs
merge(["file1.pdf", "file2.pdf"], "output.pdf")

# Advanced pattern merging
pattern = [
    ("A.pdf", 1, 5),
    ("B.pdf", 1, 5),
]
merge_pattern(pattern, "output.pdf")
```

See [API Reference](api.md) for complete documentation.

## 📊 Documentation Statistics

- **Total Documentation Files**: 20+ files
- **Publishing Guides**: 5 comprehensive guides (1,255+ lines)
- **Code Examples**: 50+ real-world examples
- **Quick References**: 3 quick start guides
- **Visual Diagrams**: 10+ flowcharts and diagrams

## 🔍 Search Tips

- Use your browser's search (Ctrl/Cmd+F) within documents
- Check the [README](../README.md) for overview and examples
- See [Project Summary](../PROJECT_SUMMARY.md) for technical details
- Review [Contributing Guide](../CONTRIBUTING.md) for development workflow

## 🆘 Getting Help

### Common Issues

1. **Installation Problems**: See [Installation Guide](installation.md)
2. **CLI Errors**: Check [CLI Reference](cli.md) and [Examples](examples.md)
3. **Publishing Failures**: See [Troubleshooting Guide](github-trusted-publisher.md#troubleshooting)
4. **Build Issues**: Review [Makefile Targets](makefile-targets.md)

### Where to Ask Questions

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/YOUR_USERNAME/merge-pdf/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/YOUR_USERNAME/merge-pdf/discussions)
- 📖 **Documentation**: Check this index first!

## 📝 Documentation Contributions

Found a typo? Want to improve the docs? See [Contributing Guide](../CONTRIBUTING.md)!

We welcome:
- Typo fixes
- Clarifications
- Additional examples
- Translation improvements
- New tutorials

## 🔗 External Resources

- [PyPI Project Page](https://pypi.org/project/merge-pdf/)
- [PyPI Trusted Publishers Documentation](https://docs.pypi.org/trusted-publishers/)
- [pypdf Documentation](https://pypdf.readthedocs.io/)
- [Click Documentation](https://click.palletsprojects.com/)
- [Python Packaging Guide](https://packaging.python.org/)

---

**📚 Happy reading! If you can't find what you're looking for, please [open an issue](https://github.com/YOUR_USERNAME/merge-pdf/issues).**

