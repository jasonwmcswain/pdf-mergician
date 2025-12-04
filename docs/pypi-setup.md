# PyPI Setup Guide

Complete guide for setting up PyPI and TestPyPI credentials for publishing pdf-mergician.

## Overview

You'll need accounts and API tokens for:
1. **TestPyPI** - For testing releases (https://test.pypi.org)
2. **PyPI** - For production releases (https://pypi.org)

---

## Step 1: Create PyPI Accounts

### TestPyPI Account

1. Go to https://test.pypi.org/account/register/
2. Fill in the registration form:
   - Username
   - Email address
   - Password
3. Verify your email address
4. Enable 2FA (Two-Factor Authentication) - **Required for API tokens**

### PyPI Account

1. Go to https://pypi.org/account/register/
2. Fill in the registration form:
   - Username
   - Email address
   - Password
3. Verify your email address
4. Enable 2FA (Two-Factor Authentication) - **Required for API tokens**

**Note:** These are separate accounts. You need to register on both sites.

---

## Step 2: Enable Two-Factor Authentication (2FA)

### Why 2FA is Required

PyPI requires 2FA to create API tokens for security reasons.

### Enable 2FA on TestPyPI

1. Log in to https://test.pypi.org
2. Go to Account Settings: https://test.pypi.org/manage/account/
3. Click "Add 2FA with authentication application"
4. Scan the QR code with your authenticator app (Google Authenticator, Authy, etc.)
5. Enter the verification code
6. Save your recovery codes in a safe place!

### Enable 2FA on PyPI

1. Log in to https://pypi.org
2. Go to Account Settings: https://pypi.org/manage/account/
3. Click "Add 2FA with authentication application"
4. Scan the QR code with your authenticator app
5. Enter the verification code
6. Save your recovery codes in a safe place!

---

## Step 3: Create API Tokens

### TestPyPI API Token

1. Log in to https://test.pypi.org
2. Go to Account Settings: https://test.pypi.org/manage/account/
3. Scroll to "API tokens" section
4. Click "Add API token"
5. Enter token details:
   - **Token name:** `pdf-mergician-test` (or any descriptive name)
   - **Scope:** "Entire account" (for first time) or "Project: pdf-mergician" (after first upload)
6. Click "Add token"
7. **IMPORTANT:** Copy the token immediately! Format: `pypi-AgEIcHlwaS5vcmc...`
8. Store it securely - you won't be able to see it again!

### PyPI API Token

1. Log in to https://pypi.org
2. Go to Account Settings: https://pypi.org/manage/account/
3. Scroll to "API tokens" section
4. Click "Add API token"
5. Enter token details:
   - **Token name:** `pdf-mergician-production` (or any descriptive name)
   - **Scope:** "Entire account" (for first time) or "Project: pdf-mergician" (after first upload)
6. Click "Add token"
7. **IMPORTANT:** Copy the token immediately! Format: `pypi-AgEIcHlwaS5vcmc...`
8. Store it securely - you won't be able to see it again!

---

## Step 4: Configure Credentials

You have two options for storing credentials:

### Option 1: Using `.pypirc` File (Recommended)

Create a `.pypirc` file in your home directory:

**Location:**
- Linux/Mac: `~/.pypirc`
- Windows: `%USERPROFILE%\.pypirc`

**Content:**

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmc...YOUR_PYPI_TOKEN_HERE...

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-AgEIcHlwaS5vcmc...YOUR_TESTPYPI_TOKEN_HERE...
```

**Important:**
- Replace `YOUR_PYPI_TOKEN_HERE` with your actual PyPI token
- Replace `YOUR_TESTPYPI_TOKEN_HERE` with your actual TestPyPI token
- Username is always `__token__` when using API tokens
- Keep this file secure! Add to `.gitignore` if in project directory

**Set Permissions (Linux/Mac):**

```bash
chmod 600 ~/.pypirc
```

### Option 2: Using Environment Variables

Set environment variables with your tokens:

**Linux/Mac (bash/zsh):**

Add to `~/.bashrc` or `~/.zshrc`:

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-AgEIcHlwaS5vcmc...YOUR_PYPI_TOKEN_HERE...
export TWINE_TEST_USERNAME=__token__
export TWINE_TEST_PASSWORD=pypi-AgEIcHlwaS5vcmc...YOUR_TESTPYPI_TOKEN_HERE...
```

Then reload:
```bash
source ~/.bashrc  # or source ~/.zshrc
```

**Windows (PowerShell):**

```powershell
$env:TWINE_USERNAME = "__token__"
$env:TWINE_PASSWORD = "pypi-AgEIcHlwaS5vcmc...YOUR_PYPI_TOKEN_HERE..."
$env:TWINE_TEST_USERNAME = "__token__"
$env:TWINE_TEST_PASSWORD = "pypi-AgEIcHlwaS5vcmc...YOUR_TESTPYPI_TOKEN_HERE..."
```

For permanent variables, use System Properties → Environment Variables.

---

## Step 5: Update Makefile (Already Done!)

The Makefile is already configured to use your credentials:

**For TestPyPI:**
```makefile
publish-test: package check-dist
	@echo "$(YELLOW)Publishing to TestPyPI...$(NC)"
	@$(PYTHON) -m twine upload --repository testpypi dist/*
	@echo "$(GREEN)✓ Published to TestPyPI$(NC)"
```

**For PyPI:**
```makefile
publish: package check-dist
	@echo "$(RED)⚠ Publishing to PyPI (production)...$(NC)"
	@read -p "Are you sure you want to publish to PyPI? [y/N] " -n 1 -r; \
	echo; \
	if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
		$(PYTHON) -m twine upload dist/*; \
		echo "$(GREEN)✓ Published to PyPI$(NC)"; \
	else \
		echo "$(YELLOW)Publish cancelled$(NC)"; \
	fi
```

---

## Step 6: Test Your Setup

### Test TestPyPI Upload

```bash
# Build and publish to TestPyPI
make publish-test
```

**Expected output:**
```
Publishing to TestPyPI...
Uploading distributions to https://test.pypi.org/legacy/
Uploading merge_pdf-2025.12.03.3-py3-none-any.whl
Uploading merge_pdf-2025.12.03.3.tar.gz
✓ Published to TestPyPI
```

### Verify on TestPyPI

1. Go to https://test.pypi.org/project/pdf-mergician/
2. You should see your package listed!

### Test Installation from TestPyPI

```bash
# Create a test environment
python -m venv test_env
source test_env/bin/activate  # or test_env\Scripts\activate on Windows

# Install from TestPyPI
pip install -i https://test.pypi.org/simple/ pdf-mergician

# Test the package
pdf-mergician --version

# Clean up
deactivate
rm -rf test_env
```

### Test PyPI Upload (When Ready)

```bash
# Build and publish to PyPI
make publish
```

You'll be prompted:
```
⚠ Publishing to PyPI (production)...
Are you sure you want to publish to PyPI? [y/N]
```

Type `y` and press Enter to confirm.

---

## Security Best Practices

### 1. Protect Your Tokens

- **Never commit tokens to git**
- Store in `.pypirc` with restricted permissions (600)
- Use environment variables for CI/CD
- Regenerate tokens if exposed

### 2. Use Project-Scoped Tokens

After first upload, create project-specific tokens:

1. Go to PyPI project page: https://pypi.org/project/pdf-mergician/
2. Go to "Manage" → "Settings"
3. Create a new API token scoped to this project only
4. Replace the account-wide token in `.pypirc`

### 3. Rotate Tokens Regularly

- Regenerate tokens every 6-12 months
- Delete old tokens after creating new ones
- Update `.pypirc` or environment variables

### 4. Keep Recovery Codes Safe

- Store 2FA recovery codes in a password manager
- Don't lose them - you'll need them if you lose your phone!

---

## Troubleshooting

### "Invalid or non-existent authentication information"

**Cause:** Incorrect token or username

**Solution:**
1. Verify username is `__token__` (with double underscores)
2. Check token is copied completely (starts with `pypi-`)
3. Ensure no extra spaces in `.pypirc`

### "403 Forbidden"

**Cause:** Insufficient permissions or package name already taken

**Solution:**
1. Check if package name is available
2. Verify token has correct scope
3. Ensure 2FA is enabled

### "Package already exists"

**Cause:** Version already published

**Solution:**
1. Bump version: `make version-bump`
2. Rebuild: `make build`
3. Try publishing again

### "Connection error"

**Cause:** Network issues or incorrect repository URL

**Solution:**
1. Check internet connection
2. Verify repository URL in `.pypirc`
3. Try again

---

## CI/CD Setup (GitHub Actions)

For automated publishing, add secrets to GitHub:

### Add Secrets to GitHub Repository

1. Go to your GitHub repository
2. Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Add these secrets:
   - **Name:** `PYPI_API_TOKEN`
   - **Value:** Your PyPI token
   - **Name:** `TEST_PYPI_API_TOKEN`
   - **Value:** Your TestPyPI token

### GitHub Actions Workflow

Already configured in `.github/workflows/publish.yml`:

```yaml
- name: Publish to PyPI
  env:
    TWINE_USERNAME: __token__
    TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
  run: twine upload dist/*
```

---

## Quick Reference

### Commands

```bash
# Test publishing
make publish-test

# Production publishing
make publish

# Full pipeline
make all
```

### Files

```bash
~/.pypirc              # Credentials file
~/.bashrc              # Environment variables (Linux/Mac)
%USERPROFILE%\.pypirc  # Credentials file (Windows)
```

### URLs

- **TestPyPI:** https://test.pypi.org
- **PyPI:** https://pypi.org
- **TestPyPI Package:** https://test.pypi.org/project/pdf-mergician/
- **PyPI Package:** https://pypi.org/project/pdf-mergician/

---

## First-Time Publishing Checklist

- [ ] Create TestPyPI account
- [ ] Create PyPI account
- [ ] Enable 2FA on both accounts
- [ ] Create TestPyPI API token
- [ ] Create PyPI API token
- [ ] Configure `.pypirc` file
- [ ] Set file permissions (Linux/Mac)
- [ ] Test with `make publish-test`
- [ ] Verify on TestPyPI
- [ ] Test installation from TestPyPI
- [ ] When ready, `make publish` to PyPI
- [ ] Verify on PyPI
- [ ] Create project-scoped tokens
- [ ] Update `.pypirc` with project tokens

---

## Additional Resources

- [PyPI Help](https://pypi.org/help/)
- [TestPyPI Help](https://test.pypi.org/help/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Python Packaging Guide](https://packaging.python.org/)
- [API Token Guide](https://pypi.org/help/#apitoken)

---

## Support

If you encounter issues:

1. Check [Troubleshooting](#troubleshooting) section
2. Review [PyPI Help](https://pypi.org/help/)
3. Check [GitHub Issues](https://github.com/jmcswain/pdf-mergician/issues)
4. Contact PyPI support: https://pypi.org/help/#support

---

**Ready to publish?** Follow the steps above and you'll be publishing to PyPI in no time! 🚀

