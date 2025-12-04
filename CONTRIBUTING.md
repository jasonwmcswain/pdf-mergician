# Contributing to pdf-mergician

Thank you for your interest in contributing to pdf-mergician! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and encourage diverse perspectives
- Focus on what is best for the community
- Show empathy towards other community members

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the behavior
- **Expected behavior**
- **Actual behavior**
- **Environment details** (OS, Python version, pdf-mergician version)
- **Sample files** if applicable (ensure no sensitive data)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title and description**
- **Use case** explaining why this would be useful
- **Possible implementation** if you have ideas
- **Examples** of how it would work

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the code style guidelines
3. **Add tests** for any new functionality
4. **Update documentation** as needed
5. **Ensure tests pass** by running `make test`
6. **Run linting** with `make lint`
7. **Submit a pull request**

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip
- make (optional but recommended)

### Setup Steps

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/pdf-mergician.git
cd pdf-mergician

# Create virtual environment (REQUIRED)
make venv

# Install with development dependencies
make dev-install
```

**Important:** All development work should be done in the virtual environment at `./venv/`. The Makefile automatically uses this virtual environment for all commands, keeping your system Python clean and ensuring consistent dependencies across all contributors.

**Manual setup (if not using make):**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Unix/macOS
# or
venv\Scripts\activate     # On Windows

# Install with development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
make test

# Run tests with coverage
make coverage

# Run quick tests (no coverage)
make test-quick
```

### Code Quality

```bash
# Format code
make format

# Run linter
make lint

# Auto-fix linting issues
make lint-fix

# Run all checks
make verify
```

## Code Style Guidelines

### Python Code

- Follow **PEP 8** style guide
- Use **type hints** for function signatures
- Write **docstrings** for all public functions and classes
- Keep functions **focused and small**
- Use **descriptive variable names**

### Docstring Format

```python
def function_name(param1: str, param2: int) -> bool:
    """
    Brief description of function.

    Longer description if needed, explaining behavior,
    edge cases, and important details.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: Description of when this is raised
        FileNotFoundError: Description of when this is raised

    Example:
        >>> function_name("test", 42)
        True
    """
```

### Testing

- Write tests for **all new features**
- Ensure **existing tests pass**
- Aim for **high code coverage** (>90%)
- Use **descriptive test names**
- Test **edge cases and error conditions**

### Test Structure

```python
class TestFeatureName:
    """Tests for feature_name functionality."""

    def test_basic_usage(self, fixture):
        """Test basic usage of feature."""
        # Arrange
        input_data = ...

        # Act
        result = function(input_data)

        # Assert
        assert result == expected

    def test_edge_case(self, fixture):
        """Test edge case handling."""
        # Test implementation
```

## Commit Messages

Write clear, descriptive commit messages:

- Use the **present tense** ("Add feature" not "Added feature")
- Use the **imperative mood** ("Move cursor to..." not "Moves cursor to...")
- **Limit the first line** to 72 characters or less
- **Reference issues** and pull requests when relevant

### Examples

```
Add rotate_pages function to core module

Implement page rotation with support for 90-degree increments.
Includes validation for rotation angles and page numbers.

Fixes #123
```

```
Fix page range validation in merge_pattern

- Add check for start > end
- Improve error messages
- Add tests for edge cases

Closes #456
```

## Project Structure

```
pdf-mergician/
├── merge_pdf/          # Main package
│   ├── __init__.py    # Package initialization
│   ├── core.py        # Core PDF functions
│   └── cli.py         # Click CLI interface
├── tests/             # Test suite
│   ├── conftest.py    # Pytest fixtures
│   ├── test_core.py   # Core function tests
│   └── test_cli.py    # CLI tests
├── docs/              # Documentation
│   ├── api.md         # API documentation
│   ├── cli.md         # CLI documentation
│   └── examples.md    # Usage examples
├── pyproject.toml     # Project configuration
├── Makefile           # Build automation
└── README.md          # Project overview
```

## Adding New Features

### 1. Plan the Feature

- Discuss in an issue first for major features
- Consider backward compatibility
- Think about edge cases
- Plan the API design

### 2. Implement the Feature

```python
# In merge_pdf/core.py
def new_feature(input_file: PathLike, output_file: PathLike) -> None:
    """
    Brief description of the new feature.

    Args:
        input_file: Description
        output_file: Description

    Raises:
        ValueError: When...
    """
    # Implementation
```

### 3. Add CLI Command (if applicable)

```python
# In merge_pdf/cli.py
@cli.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.argument("output_file", type=click.Path())
def new_command(input_file: str, output_file: str) -> None:
    """
    Brief description for CLI help.
    """
    try:
        new_feature(input_file, output_file)
        _echo_success(f"Created {output_file}")
    except Exception as e:
        _echo_error(str(e))
        sys.exit(1)
```

### 4. Write Tests

```python
# In tests/test_core.py
class TestNewFeature:
    """Tests for new_feature function."""

    def test_basic_usage(self, sample_pdf, tmp_path):
        """Test basic usage."""
        output = tmp_path / "output.pdf"
        new_feature(sample_pdf, output)
        assert output.exists()

    def test_error_handling(self, tmp_path):
        """Test error handling."""
        with pytest.raises(ValueError):
            new_feature("invalid", tmp_path / "output.pdf")
```

### 5. Update Documentation

- Add to README.md if user-facing
- Update docs/api.md for Python API
- Update docs/cli.md for CLI commands
- Add examples to docs/examples.md

### 6. Update Exports

```python
# In merge_pdf/__init__.py
__all__ = [
    "merge",
    "merge_pattern",
    "split_pdf",
    "rotate_pages",
    "extract_pages",
    "new_feature",  # Add new feature
]
```

## Release Process

(For maintainers)

pdf-mergician uses date-based versioning (YYYY.MM.DD.x). The version is automatically managed:

1. Update CHANGELOG.md with changes
2. Run full package preparation: `make package`
   - This automatically bumps the version
   - Runs linting and tests
   - Builds the distribution
3. Test on TestPyPI (optional): `make publish-test`
4. Publish to PyPI: `make publish`
5. Create GitHub release with tag

### Manual Version Management

If you need to manually manage versions:

```bash
# Show current version
make version

# Bump version
make version-bump

# Or use Python directly
python version.py bump
```

See [docs/versioning.md](docs/versioning.md) for detailed information.

## Getting Help

- **Questions**: Open a GitHub issue with the "question" label
- **Discussions**: Use GitHub Discussions
- **Chat**: (Add chat platform if available)

## Recognition

Contributors will be recognized in:
- GitHub contributors page
- Release notes
- Project documentation (if significant contribution)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to pdf-mergician! 🎉

