# GitHub Actions Trusted Publisher Setup

This guide walks you through setting up **Trusted Publishing** (OpenID Connect/OIDC) for automated PyPI releases using GitHub Actions. This is the **recommended and most secure** method for publishing packages.

## 📋 Table of Contents

- [What is Trusted Publishing?](#what-is-trusted-publishing)
- [Why Use Trusted Publishing?](#why-use-trusted-publishing)
- [Prerequisites](#prerequisites)
- [Step-by-Step Setup](#step-by-step-setup)
  - [1. Configure PyPI Trusted Publisher](#1-configure-pypi-trusted-publisher)
  - [2. Configure TestPyPI Trusted Publisher](#2-configure-testpypi-trusted-publisher)
  - [3. Create GitHub Environments](#3-create-github-environments)
  - [4. Verify Workflow Files](#4-verify-workflow-files)
- [Publishing Workflow](#publishing-workflow)
- [Troubleshooting](#troubleshooting)
- [Security Considerations](#security-considerations)

---

## What is Trusted Publishing?

**Trusted Publishing** uses OpenID Connect (OIDC) to authenticate GitHub Actions workflows with PyPI **without requiring API tokens or passwords**. Instead, PyPI trusts GitHub's identity verification and issues short-lived tokens (valid for 15 minutes) automatically during the publishing process.

### How It Works

```
┌─────────────────┐
│ GitHub Actions  │
│   Workflow      │
└────────┬────────┘
         │ 1. Request OIDC token
         ▼
┌─────────────────┐
│  GitHub OIDC    │
│   Provider      │
└────────┬────────┘
         │ 2. Issue signed token
         ▼
┌─────────────────┐
│      PyPI       │
│  (Verifies &    │
│   Trusts Token) │
└────────┬────────┘
         │ 3. Mint short-lived API token
         ▼
┌─────────────────┐
│   Package       │
│   Published     │
└─────────────────┘
```

---

## Why Use Trusted Publishing?

✅ **No Manual Token Management**: No need to create, store, or rotate API tokens
✅ **Enhanced Security**: Tokens are short-lived (15 minutes) and automatically expire
✅ **Reduced Attack Surface**: No long-lived credentials that can be compromised
✅ **Simpler Setup**: No secrets to configure in GitHub
✅ **Audit Trail**: PyPI logs show which workflow published each release
✅ **PyPI Recommended**: Official best practice from PyPI

---

## Prerequisites

Before you begin, ensure you have:

1. ✅ A **GitHub repository** for your project
2. ✅ A **PyPI account** (create at [pypi.org](https://pypi.org/account/register/))
3. ✅ A **TestPyPI account** (create at [test.pypi.org](https://test.pypi.org/account/register/))
4. ✅ **Maintainer or Owner** permissions on PyPI for your project (or ability to create it)
5. ✅ **Admin access** to your GitHub repository

---

## Step-by-Step Setup

### 1. Configure PyPI Trusted Publisher

#### Option A: For a New Project (Pending Publisher)

If your package doesn't exist on PyPI yet:

1. **Go to PyPI Trusted Publishers**:
   - Visit: https://pypi.org/manage/account/publishing/
   - Log in to your PyPI account

2. **Add a Pending Publisher**:
   - Scroll to **"Add a new pending publisher"**
   - Fill in the form:
     ```
     PyPI Project Name:     merge-pdf
     Owner:                 YOUR_GITHUB_USERNAME
     Repository name:       merge-pdf
     Workflow name:         publish.yml
     Environment name:      pypi
     ```
   - Click **"Add"**

3. **What Happens Next**:
   - The first time your workflow runs, it will **automatically create** the PyPI project
   - The pending publisher becomes a regular trusted publisher
   - Future releases use the same configuration

#### Option B: For an Existing Project

If your package already exists on PyPI:

1. **Go to Your Project Settings**:
   - Visit: https://pypi.org/manage/project/merge-pdf/settings/publishing/
   - (Replace `merge-pdf` with your actual project name)

2. **Add a Publisher**:
   - Scroll to **"Add a new publisher"**
   - Fill in the form:
     ```
     Owner:                 YOUR_GITHUB_USERNAME
     Repository name:       merge-pdf
     Workflow name:         publish.yml
     Environment name:      pypi
     ```
   - Click **"Add"**

---

### 2. Configure TestPyPI Trusted Publisher

Repeat the same process for TestPyPI (for testing before production):

1. **Go to TestPyPI Trusted Publishers**:
   - Visit: https://test.pypi.org/manage/account/publishing/

2. **Add a Pending Publisher**:
   ```
   PyPI Project Name:     merge-pdf
   Owner:                 YOUR_GITHUB_USERNAME
   Repository name:       merge-pdf
   Workflow name:         publish-test.yml
   Environment name:      testpypi
   ```

---

### 3. Create GitHub Environments

GitHub environments provide an additional security layer and allow you to require manual approval for production releases.

#### Create `pypi` Environment (Production)

1. Go to your GitHub repository
2. Click **Settings** → **Environments**
3. Click **"New environment"**
4. Name it: `pypi`
5. **Optional but Recommended**: Configure protection rules:
   - ☑️ **Required reviewers**: Add yourself or team members
   - ☑️ **Wait timer**: Add a delay (e.g., 5 minutes) before deployment
   - ☑️ **Deployment branches**: Restrict to `main` branch only
6. Click **"Save protection rules"**

#### Create `testpypi` Environment (Testing)

1. Click **"New environment"** again
2. Name it: `testpypi`
3. **Optional**: Add lighter protection rules or none for faster testing
4. Click **"Save protection rules"**

---

### 4. Verify Workflow Files

Ensure your workflow files are correctly configured:

#### `.github/workflows/publish.yml` (Production)

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

permissions:
  contents: read

jobs:
  publish:
    name: Publish to PyPI
    runs-on: ubuntu-latest

    permissions:
      id-token: write  # CRITICAL: Required for OIDC

    environment:
      name: pypi  # Must match PyPI configuration
      url: https://pypi.org/p/merge-pdf

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install build dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build

    - name: Build package
      run: python -m build

    - name: Publish to PyPI
      uses: pypa/gh-action-pypi-publish@release/v1
```

#### `.github/workflows/publish-test.yml` (TestPyPI)

```yaml
name: Publish to TestPyPI

on:
  push:
    tags:
      - 'test-*'

permissions:
  contents: read

jobs:
  publish-test:
    name: Publish to TestPyPI
    runs-on: ubuntu-latest

    permissions:
      id-token: write  # CRITICAL: Required for OIDC

    environment:
      name: testpypi  # Must match TestPyPI configuration
      url: https://test.pypi.org/p/merge-pdf

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Build package
      run: |
        python -m pip install --upgrade pip
        pip install build
        python -m build

    - name: Publish to TestPyPI
      uses: pypa/gh-action-pypi-publish@release/v1
      with:
        repository-url: https://test.pypi.org/legacy/
```

---

## Publishing Workflow

### Testing with TestPyPI

1. **Create a test tag**:
   ```bash
   git tag test-2025.12.03.1
   git push origin test-2025.12.03.1
   ```

2. **Monitor the workflow**:
   - Go to **Actions** tab in GitHub
   - Watch the "Publish to TestPyPI" workflow run

3. **Verify on TestPyPI**:
   - Visit: https://test.pypi.org/project/merge-pdf/
   - Check that your package appears

4. **Test installation**:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ merge-pdf
   ```

### Publishing to Production PyPI

1. **Create a GitHub Release**:
   - Go to **Releases** → **"Draft a new release"**
   - Create a new tag: `v2025.12.03.1` (or use your version)
   - Fill in release notes
   - Click **"Publish release"**

2. **Automatic Publishing**:
   - The workflow triggers automatically
   - If you configured required reviewers, approve the deployment
   - Monitor in the **Actions** tab

3. **Verify on PyPI**:
   - Visit: https://pypi.org/project/merge-pdf/
   - Your package is now live!

4. **Install from PyPI**:
   ```bash
   pip install merge-pdf
   ```

---

## Troubleshooting

### Error: "Trusted publishing exchange failure"

**Cause**: PyPI configuration doesn't match GitHub workflow

**Solution**: Double-check that these match exactly:
- Repository owner/name
- Workflow filename (`publish.yml`)
- Environment name (`pypi`)

### Error: "Resource not accessible by integration"

**Cause**: Missing `id-token: write` permission

**Solution**: Ensure your workflow has:
```yaml
permissions:
  id-token: write
```

### Error: "Environment protection rules not satisfied"

**Cause**: GitHub environment requires approval or has deployment restrictions

**Solution**:
- Approve the deployment in the GitHub UI
- Or adjust environment protection rules

### Workflow doesn't trigger

**Cause**: Workflow trigger conditions not met

**Solution**:
- For `publish.yml`: Create a GitHub Release (not just a tag)
- For `publish-test.yml`: Push a tag starting with `test-`
- Or use **"Run workflow"** button for manual trigger

### Package name already taken

**Cause**: Someone else registered the package name

**Solution**:
- Choose a different name
- Or contact PyPI support if you believe you have rights to the name

---

## Security Considerations

### ✅ Best Practices

1. **Use Environment Protection**:
   - Require manual approval for production releases
   - Restrict deployments to specific branches

2. **Minimal Permissions**:
   - Only grant `id-token: write` to the publish job
   - Keep top-level permissions minimal

3. **Separate Environments**:
   - Use different environments for TestPyPI and PyPI
   - Test thoroughly on TestPyPI before production

4. **Monitor Releases**:
   - Review PyPI release logs regularly
   - Set up notifications for new releases

5. **Branch Protection**:
   - Protect your `main` branch
   - Require PR reviews before merging

### 🔒 What Trusted Publishing Prevents

- ❌ Stolen API tokens
- ❌ Leaked credentials in logs
- ❌ Token rotation burden
- ❌ Long-lived credentials
- ❌ Manual token management

---

## Additional Resources

- 📖 [PyPI Trusted Publishers Documentation](https://docs.pypi.org/trusted-publishers/)
- 📖 [GitHub Actions OIDC Documentation](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
- 📖 [PyPA Publish Action](https://github.com/pypa/gh-action-pypi-publish)
- 📖 [OpenID Connect Standard](https://openid.net/connect/)

---

## Quick Reference

### PyPI Trusted Publisher URLs

| Service | Manage Publishers | Manage Account |
|---------|------------------|----------------|
| **PyPI** | https://pypi.org/manage/account/publishing/ | https://pypi.org/manage/account/ |
| **TestPyPI** | https://test.pypi.org/manage/account/publishing/ | https://test.pypi.org/manage/account/ |

### Required Workflow Configuration

```yaml
permissions:
  id-token: write  # ← CRITICAL

environment:
  name: pypi  # ← Must match PyPI config
```

### Workflow Triggers

| Workflow | Trigger | Command |
|----------|---------|---------|
| `publish.yml` | GitHub Release | Create release in GitHub UI |
| `publish-test.yml` | Tag `test-*` | `git tag test-v1.0.0 && git push origin test-v1.0.0` |

---

**🎉 You're all set!** Your package will now publish automatically using secure, credential-free trusted publishing.

