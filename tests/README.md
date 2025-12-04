# Test Suite Documentation

This directory contains the comprehensive test suite for pdf-mergician.

## Test Structure

```
tests/
├── conftest.py              # Pytest configuration and fixtures
├── test_core.py             # Unit tests for core functions (36 tests)
├── test_cli.py              # Unit tests for CLI commands (30 tests)
├── test_cli_integration.py  # Integration tests with real PDFs (24 tests)
├── fixtures/                # Test PDF fixtures
│   ├── create_test_pdfs.py  # Script to generate test PDFs
│   └── *.pdf                # Generated test PDFs (not in git)
└── README.md                # This file
```

## Test Categories

### Unit Tests (66 tests)

**test_core.py** - Tests for core PDF manipulation functions:
- Merge operations
- Pattern-based merging
- PDF splitting
- Page rotation
- Page extraction
- Error handling

**test_cli.py** - Tests for CLI interface:
- Command parsing
- Option handling
- Error messages
- Help text
- Version display

### Integration Tests (24 tests)

**test_cli_integration.py** - End-to-end tests with real PDFs:
- Complete workflows
- Real PDF manipulation
- Error scenarios
- Multi-step operations

## Test Fixtures

Test PDFs are generated automatically using `create_test_pdfs.py`:

```bash
# Create fixtures manually
python tests/fixtures/create_test_pdfs.py

# Or use make target
make test-fixtures
```

**Generated PDFs:**
- `doc_a.pdf` - 10 pages
- `doc_b.pdf` - 10 pages
- `doc_c.pdf` - 5 pages
- `small_doc.pdf` - 3 pages
- `single_page.pdf` - 1 page

These PDFs are **not committed to git** but are generated on-demand.

## Running Tests

### All Tests

```bash
# With coverage
make test

# Without coverage (faster)
make test-quick

# Using pytest directly
pytest tests/ -v
```

### Specific Test Files

```bash
# Core tests only
pytest tests/test_core.py -v

# CLI tests only
pytest tests/test_cli.py -v

# Integration tests only
pytest tests/test_cli_integration.py -v
```

### Specific Test Classes or Functions

```bash
# Run specific test class
pytest tests/test_core.py::TestMerge -v

# Run specific test
pytest tests/test_core.py::TestMerge::test_merge_multiple_pdfs -v
```

### Coverage Reports

```bash
# Terminal report
make coverage

# HTML report (opens in browser)
make coverage
open htmlcov/index.html
```

## Current Coverage

- **Overall:** 84%
- **merge_pdf/core.py:** 100%
- **merge_pdf/cli.py:** 73%
- **merge_pdf/__init__.py:** 100%

The CLI coverage is lower because some error paths are difficult to trigger in tests (e.g., Click's internal error handling).

## Writing New Tests

### Unit Test Template

```python
class TestNewFeature:
    """Tests for new_feature functionality."""

    def test_basic_usage(self, fixture):
        """Test basic usage."""
        # Arrange
        input_data = ...

        # Act
        result = new_feature(input_data)

        # Assert
        assert result == expected

    def test_error_handling(self):
        """Test error handling."""
        with pytest.raises(ValueError):
            new_feature(invalid_input)
```

### Integration Test Template

```python
def test_workflow_name(runner, test_pdfs, tmp_path):
    """Test complete workflow."""
    # Step 1: Setup
    output = tmp_path / "output.pdf"

    # Step 2: Execute
    result = runner.invoke(cli, ["command", str(output), ...])

    # Step 3: Verify
    assert result.exit_code == 0
    assert output.exists()

    # Step 4: Validate content
    reader = PdfReader(output)
    assert len(reader.pages) == expected_pages
```

## Test Fixtures

### Using Existing Fixtures

```python
def test_with_fixture(sample_pdf, tmp_path):
    """Test using a fixture."""
    # sample_pdf is a Path to a temporary PDF
    # tmp_path is a temporary directory
    pass
```

### Available Fixtures

From `conftest.py`:
- `temp_pdf_dir` - Temporary directory for PDFs
- `sample_pdf` - Single-page PDF
- `multi_page_pdf` - 10-page PDF
- `multiple_pdfs` - List of PDFs with different page counts

From `test_cli_integration.py`:
- `test_pdfs` - Dictionary of test PDFs with known page counts
- `fixtures_dir` - Path to fixtures directory
- `runner` - Click test runner

## Best Practices

1. **Test Isolation** - Each test should be independent
2. **Descriptive Names** - Use clear, descriptive test names
3. **Arrange-Act-Assert** - Follow AAA pattern
4. **One Assertion** - Test one thing per test (when possible)
5. **Use Fixtures** - Reuse common setup with fixtures
6. **Clean Up** - Use tmp_path for temporary files
7. **Error Testing** - Test both success and failure cases

## Continuous Integration

Tests run automatically on:
- Push to main/develop branches
- Pull requests
- Multiple Python versions (3.8-3.12)
- Multiple OS (Linux, macOS, Windows)

See `.github/workflows/ci.yml` for CI configuration.

## Debugging Tests

### Run with verbose output

```bash
pytest tests/ -vv
```

### Show print statements

```bash
pytest tests/ -s
```

### Stop on first failure

```bash
pytest tests/ -x
```

### Run last failed tests

```bash
pytest tests/ --lf
```

### Debug with pdb

```bash
pytest tests/ --pdb
```

## Test Performance

Current test suite performance:
- **Unit tests:** ~0.3 seconds
- **Integration tests:** ~0.2 seconds
- **Total:** ~0.6 seconds

## Adding New Tests

When adding new features:

1. Write tests first (TDD)
2. Add unit tests for core functionality
3. Add CLI tests for command interface
4. Add integration tests for workflows
5. Ensure coverage stays above 80%
6. Update this README if needed

## Troubleshooting

### Tests fail with "No module named 'merge_pdf'"

```bash
# Install in development mode
pip install -e .
```

### Fixtures not found

```bash
# Create fixtures
make test-fixtures
```

### Coverage not working

```bash
# Install pytest-cov
pip install pytest-cov
```

## Resources

- [pytest documentation](https://docs.pytest.org/)
- [pytest-cov documentation](https://pytest-cov.readthedocs.io/)
- [Click testing](https://click.palletsprojects.com/en/8.1.x/testing/)

---

For questions about tests, see [CONTRIBUTING.md](../CONTRIBUTING.md).

