.PHONY: help clean build lint test coverage package publish install dev-install format check-format version version-bump version-show test-fixtures validate clean-validate venv venv-clean all all-test

# Virtual environment configuration
VENV := ./venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
PYTEST := $(VENV)/bin/pytest
RUFF := $(VENV)/bin/ruff
TWINE := $(VENV)/bin/twine

# Colors for output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
NC := \033[0m # No Color

help: ## Show this help message
	@echo "$(BLUE)merge-pdf - Makefile targets$(NC)"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-15s$(NC) %s\n", $$1, $$2}'
	@echo ""
	@echo "$(YELLOW)Note: All commands use the virtual environment at ./venv/$(NC)"
	@echo "$(YELLOW)Run 'make venv' first if venv doesn't exist$(NC)"
	@echo ""

venv: ## Create virtual environment
	@if [ ! -d "$(VENV)" ]; then \
		echo "$(YELLOW)Creating virtual environment at $(VENV)...$(NC)"; \
		python3 -m venv $(VENV); \
		echo "$(GREEN)✓ Virtual environment created$(NC)"; \
		echo "$(YELLOW)Installing base dependencies...$(NC)"; \
		$(PIP) install --upgrade pip setuptools wheel; \
		echo "$(GREEN)✓ Base dependencies installed$(NC)"; \
	else \
		echo "$(GREEN)✓ Virtual environment already exists at $(VENV)$(NC)"; \
	fi

venv-clean: ## Remove virtual environment
	@echo "$(YELLOW)Removing virtual environment...$(NC)"
	@rm -rf $(VENV)
	@echo "$(GREEN)✓ Virtual environment removed$(NC)"

clean: ## Remove build artifacts, cache files, and test outputs (keeps venv)
	@echo "$(YELLOW)Cleaning build artifacts...$(NC)"
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info/
	@rm -rf .eggs/
	@rm -rf .pytest_cache/
	@rm -rf .ruff_cache/
	@rm -rf htmlcov/
	@rm -rf .coverage
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
	@find . -type f -name "*.egg" -delete
	@echo "$(GREEN)✓ Clean complete$(NC)"

clean-all: clean venv-clean ## Remove all artifacts including virtual environment
	@echo "$(GREEN)✓ Complete clean finished$(NC)"

install: venv ## Install the package in the virtual environment
	@echo "$(YELLOW)Installing merge-pdf...$(NC)"
	@$(PIP) install .
	@echo "$(GREEN)✓ Installation complete$(NC)"

dev-install: venv ## Install the package with development dependencies
	@echo "$(YELLOW)Installing merge-pdf with dev dependencies...$(NC)"
	@$(PIP) install -e ".[dev]"
	@echo "$(GREEN)✓ Development installation complete$(NC)"

format: dev-install ## Format code with ruff
	@echo "$(YELLOW)Formatting code...$(NC)"
	@$(RUFF) format merge_pdf/ tests/
	@echo "$(GREEN)✓ Formatting complete$(NC)"

check-format: dev-install ## Check code formatting without making changes
	@echo "$(YELLOW)Checking code format...$(NC)"
	@$(RUFF) format --check merge_pdf/ tests/
	@echo "$(GREEN)✓ Format check complete$(NC)"

lint: dev-install ## Run linting checks with ruff
	@echo "$(YELLOW)Running linter...$(NC)"
	@$(RUFF) check merge_pdf/ tests/
	@echo "$(GREEN)✓ Linting complete$(NC)"

lint-fix: dev-install ## Run linting and automatically fix issues
	@echo "$(YELLOW)Running linter with auto-fix...$(NC)"
	@$(RUFF) check --fix merge_pdf/ tests/
	@echo "$(GREEN)✓ Linting with fixes complete$(NC)"

test-fixtures: dev-install ## Create test PDF fixtures
	@echo "$(YELLOW)Creating test PDF fixtures...$(NC)"
	@$(PYTHON) tests/fixtures/create_test_pdfs.py
	@echo "$(GREEN)✓ Test fixtures created$(NC)"

test: test-fixtures ## Run tests with pytest
	@echo "$(YELLOW)Running tests...$(NC)"
	@$(PYTEST) tests/ -v
	@echo "$(GREEN)✓ Tests complete$(NC)"

test-quick: test-fixtures ## Run tests without coverage
	@echo "$(YELLOW)Running quick tests...$(NC)"
	@$(PYTEST) tests/ -v --no-cov
	@echo "$(GREEN)✓ Quick tests complete$(NC)"

coverage: dev-install ## Run tests with coverage report
	@echo "$(YELLOW)Running tests with coverage...$(NC)"
	@$(PYTEST) tests/ -v --cov=merge_pdf --cov-report=term-missing --cov-report=html
	@echo "$(GREEN)✓ Coverage report generated in htmlcov/$(NC)"

version-show: venv ## Show current version
	@$(PYTHON) version.py show

version-bump: venv ## Bump version to next build number (YYYY.MM.DD.x)
	@$(PYTHON) version.py bump

version: version-show ## Alias for version-show

build: clean dev-install ## Build distribution packages (wheel and source)
	@echo "$(YELLOW)Building distribution packages...$(NC)"
	@$(PYTHON) -m build
	@echo "$(GREEN)✓ Build complete - packages in dist/$(NC)"

package: version-bump lint test build ## Run full package preparation (bump version, lint, test, build)
	@echo "$(GREEN)✓ Package ready for distribution$(NC)"

check-dist: build ## Check distribution packages with twine
	@echo "$(YELLOW)Checking distribution packages...$(NC)"
	@$(TWINE) check dist/*
	@echo "$(GREEN)✓ Distribution check complete$(NC)"

publish-test: package check-dist ## Publish to TestPyPI
	@echo "$(YELLOW)Publishing to TestPyPI...$(NC)"
	@$(TWINE) upload --repository testpypi dist/*
	@echo "$(GREEN)✓ Published to TestPyPI$(NC)"

publish: package check-dist ## Publish to PyPI (production)
	@echo "$(RED)⚠ Publishing to PyPI (production)...$(NC)"
	@read -p "Are you sure you want to publish to PyPI? [y/N] " -n 1 -r; \
	echo; \
	if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
		$(TWINE) upload dist/*; \
		echo "$(GREEN)✓ Published to PyPI$(NC)"; \
	else \
		echo "$(YELLOW)Publish cancelled$(NC)"; \
	fi

verify: clean lint test ## Run verification checks (clean, lint, test)
	@echo "$(GREEN)✓ All verification checks passed$(NC)"

validate: build lint-fix lint coverage ## Run validation (build, lint-fix, lint, coverage)
	@echo "$(GREEN)✓ Validation complete$(NC)"

clean-validate: clean build lint-fix lint coverage ## Run full validation with clean (clean, build, lint-fix, lint, coverage)
	@echo "$(GREEN)✓ Clean validation complete$(NC)"

all-test: version-bump clean-validate publish-test ## Full pipeline: version-bump, clean-validate, publish-test
	@echo "$(GREEN)✓ All test pipeline complete - package published to TestPyPI!$(NC)"

all: version-bump clean-validate publish-test publish ## Full pipeline: version-bump, clean-validate, publish-test, publish
	@echo "$(GREEN)✓ Full pipeline complete - package published!$(NC)"

.DEFAULT_GOAL := help

