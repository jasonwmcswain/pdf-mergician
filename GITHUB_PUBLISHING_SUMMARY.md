# GitHub Publishing Setup Summary

This document provides a complete overview of the GitHub Actions publishing configuration for `merge-pdf`.

## 📋 Overview

The project uses **Trusted Publishers (OpenID Connect/OIDC)** for secure, credential-free publishing to PyPI. This is the **recommended and most secure** method endorsed by PyPI.

## 🎯 What's Been Configured

### 1. GitHub Workflows

Three workflows handle CI/CD:

#### `ci.yml` - Continuous Integration
- **Triggers**: Push/PR to `main` or `develop`
- **Purpose**: Validate code quality and tests
- **Matrix**: Python 3.8-3.12 on Ubuntu, macOS, Windows
- **Actions**: Lint, format check, test, coverage

#### `publish.yml` - Production Publishing ⭐
- **Triggers**: GitHub Release published, manual dispatch
- **Purpose**: Publish to PyPI using Trusted Publishers
- **Environment**: `pypi`
- **Authentication**: OIDC (no tokens needed!)

#### `publish-test.yml` - Test Publishing
- **Triggers**: Tags starting with `test-*`, manual dispatch
- **Purpose**: Publish to TestPyPI for testing
- **Environment**: `testpypi`
- **Authentication**: OIDC (no tokens needed!)

### 2. Documentation

Comprehensive guides for every aspect:

| Document | Purpose | Location |
|----------|---------|----------|
| **GitHub Trusted Publisher Setup** | Complete OIDC setup guide | `docs/github-trusted-publisher.md` |
| **Quick Start Guide** | 5-minute setup checklist | `GITHUB_PUBLISHING_QUICKSTART.md` |
| **Publishing Comparison** | OIDC vs API tokens comparison | `docs/publishing-comparison.md` |
| **PyPI Setup (Traditional)** | API token setup (legacy) | `docs/pypi-setup.md` |
| **GitHub Workflows README** | Workflow documentation | `.github/README.md` |

### 3. Key Features

✅ **No Secrets Required**: OIDC eliminates API token management
✅ **Short-Lived Credentials**: Tokens expire after 15 minutes
✅ **Environment Protection**: Optional manual approval for releases
✅ **Dual Publishing**: Separate workflows for TestPyPI and PyPI
✅ **Comprehensive Docs**: Step-by-step guides for every scenario
✅ **Security Best Practices**: Following PyPI recommendations

## 🚀 Quick Start (5 Minutes)

### Step 1: Configure PyPI Trusted Publisher (2 min)

1. Go to: https://pypi.org/manage/account/publishing/
2. Add pending publisher:
   ```
   PyPI Project Name:     merge-pdf
   Owner:                 YOUR_GITHUB_USERNAME
   Repository name:       merge-pdf
   Workflow name:         publish.yml
   Environment name:      pypi
   ```

### Step 2: Configure TestPyPI Trusted Publisher (1 min)

1. Go to: https://test.pypi.org/manage/account/publishing/
2. Add pending publisher:
   ```
   PyPI Project Name:     merge-pdf
   Owner:                 YOUR_GITHUB_USERNAME
   Repository name:       merge-pdf
   Workflow name:         publish-test.yml
   Environment name:      testpypi
   ```

### Step 3: Create GitHub Environments (2 min)

1. Go to: **Settings** → **Environments**
2. Create: `pypi` (optional: add required reviewers)
3. Create: `testpypi`

### Step 4: Test & Publish

```bash
# Test with TestPyPI
git tag test-2025.12.03.1
git push origin test-2025.12.03.1

# Publish to PyPI (via GitHub UI)
# Go to: Releases → Draft new release → Publish
```

## 📊 Publishing Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     Development Workflow                         │
└─────────────────────────────────────────────────────────────────┘

Developer commits code
         ↓
    Push to GitHub
         ↓
┌────────────────────┐
│   CI Workflow      │  ← Runs on every push/PR
│   (ci.yml)         │  ← Tests, lints, builds
└────────────────────┘
         ↓
    Tests pass ✓
         ↓
┌────────────────────┐
│  Ready to Release  │
└────────────────────┘
         ↓
    ┌────┴────┐
    │         │
    ▼         ▼
┌─────┐   ┌─────┐
│Test │   │Prod │
└─────┘   └─────┘

TEST PUBLISHING:                PRODUCTION PUBLISHING:
1. Tag: test-v1.0.0            1. Create GitHub Release
2. Push tag                     2. Workflow triggers
3. publish-test.yml runs        3. publish.yml runs
4. Publishes to TestPyPI        4. Publishes to PyPI
5. Verify & test                5. Package live!

┌─────────────────────────────────────────────────────────────────┐
│                   OIDC Authentication Flow                       │
└─────────────────────────────────────────────────────────────────┘

GitHub Actions Workflow
         ↓
Request OIDC token from GitHub
         ↓
GitHub issues signed token
         ↓
Send token to PyPI
         ↓
PyPI verifies token signature
         ↓
PyPI checks trusted publisher config
         ↓
PyPI mints short-lived API token (15 min)
         ↓
Package published
         ↓
Token expires automatically
```

## 🔐 Security Model

### What Makes Trusted Publishers Secure?

1. **Short-Lived Tokens**: Expire after 15 minutes
2. **No Stored Secrets**: No tokens in GitHub Secrets or code
3. **Cryptographic Verification**: OIDC tokens are signed and verified
4. **Granular Trust**: PyPI trusts specific workflow + environment
5. **Audit Trail**: PyPI logs show exact workflow that published

### Attack Scenarios Prevented

| Attack | API Tokens | Trusted Publishers |
|--------|------------|-------------------|
| Stolen credentials | ❌ Vulnerable | ✅ Protected |
| Compromised dev machine | ❌ Vulnerable | ✅ Protected |
| Leaked secrets in logs | ❌ Vulnerable | ✅ Protected |
| Forgotten old tokens | ❌ Vulnerable | ✅ Protected |
| Long-term exposure | ❌ Vulnerable | ✅ Protected |

## 📚 Complete Documentation Index

### Quick References
- 🚀 [5-Minute Quick Start](GITHUB_PUBLISHING_QUICKSTART.md)
- 📖 [PyPI Quick Reference Card](PYPI_QUICKSTART.md)

### Detailed Guides
- 📘 [GitHub Trusted Publisher Setup](docs/github-trusted-publisher.md) - Complete OIDC guide
- 📗 [Publishing Methods Comparison](docs/publishing-comparison.md) - OIDC vs API tokens
- 📕 [PyPI Credentials Setup](docs/pypi-setup.md) - Traditional API token method
- 📙 [GitHub Workflows Documentation](.github/README.md) - Workflow details

### Project Documentation
- 📄 [README](README.md) - Project overview with examples
- 📄 [Contributing Guide](CONTRIBUTING.md) - Development workflow
- 📄 [Project Summary](PROJECT_SUMMARY.md) - Technical overview

## 🎯 Publishing Cheat Sheet

### Test Publishing (TestPyPI)

```bash
# Bump version
make version-bump

# Create test tag
git tag test-$(grep '^version' pyproject.toml | cut -d'"' -f2)
git push origin --tags

# Workflow runs automatically
# Verify: https://test.pypi.org/project/merge-pdf/

# Test installation
pip install --index-url https://test.pypi.org/simple/ merge-pdf
```

### Production Publishing (PyPI)

**Option 1: GitHub UI (Recommended)**
```
1. Go to: https://github.com/YOUR_USERNAME/merge-pdf/releases/new
2. Tag: v2025.12.03.1
3. Title: Release 2025.12.03.1
4. Generate release notes
5. Publish release
6. Workflow runs automatically!
```

**Option 2: GitHub CLI**
```bash
# Bump version
make version-bump

# Create release
gh release create v$(grep '^version' pyproject.toml | cut -d'"' -f2) \
  --title "Release $(grep '^version' pyproject.toml | cut -d'"' -f2)" \
  --generate-notes

# Workflow runs automatically
```

**Option 3: Manual Workflow Dispatch**
```
1. Go to: Actions → Publish to PyPI
2. Click: Run workflow
3. Select branch
4. Run
```

## 🔧 Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| "Trusted publishing exchange failure" | Config mismatch | Verify PyPI config matches workflow exactly |
| "Resource not accessible" | Missing permission | Add `permissions: id-token: write` |
| "Environment protection rules" | Approval needed | Approve deployment in GitHub UI |
| Workflow doesn't trigger | Wrong trigger | Create Release (not just tag) for production |
| "Package already exists" | Version conflict | Bump version with `make version-bump` |

### Debug Checklist

- [ ] PyPI trusted publisher configured correctly
- [ ] TestPyPI trusted publisher configured correctly
- [ ] GitHub `pypi` environment exists
- [ ] GitHub `testpypi` environment exists
- [ ] Workflow has `id-token: write` permission
- [ ] Environment name matches PyPI config exactly
- [ ] Workflow filename matches PyPI config exactly
- [ ] Repository owner/name matches PyPI config

## 📈 Monitoring & Verification

### After Publishing

1. **Check GitHub Actions**:
   - Go to: **Actions** tab
   - Verify workflow completed successfully
   - Review logs for any warnings

2. **Verify on PyPI**:
   - Production: https://pypi.org/project/merge-pdf/
   - Test: https://test.pypi.org/project/merge-pdf/
   - Check version number
   - Verify metadata

3. **Test Installation**:
   ```bash
   # Create fresh virtual environment
   python -m venv test_env
   source test_env/bin/activate  # or test_env\Scripts\activate on Windows

   # Install from PyPI
   pip install merge-pdf

   # Verify
   merge-pdf --version
   merge-pdf --help
   ```

## 🎓 Learning Resources

### Official Documentation
- [PyPI Trusted Publishers](https://docs.pypi.org/trusted-publishers/)
- [GitHub Actions OIDC](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
- [PyPA Publish Action](https://github.com/pypa/gh-action-pypi-publish)

### Tutorials
- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Publishing with GitHub Actions](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)

## ✅ Verification Checklist

Use this checklist to verify your setup:

### PyPI Configuration
- [ ] PyPI account created with 2FA enabled
- [ ] TestPyPI account created with 2FA enabled
- [ ] PyPI trusted publisher configured
- [ ] TestPyPI trusted publisher configured
- [ ] Configuration matches workflow exactly

### GitHub Configuration
- [ ] Repository has admin access
- [ ] Environment `pypi` created
- [ ] Environment `testpypi` created
- [ ] Optional: Required reviewers configured
- [ ] Workflow files exist and are correct

### Testing
- [ ] Test tag pushed successfully
- [ ] TestPyPI workflow completed
- [ ] Package appears on TestPyPI
- [ ] Test installation works
- [ ] Production release created
- [ ] PyPI workflow completed
- [ ] Package appears on PyPI
- [ ] Production installation works

### Documentation
- [ ] README updated with publishing info
- [ ] Team members know how to publish
- [ ] Troubleshooting guide accessible

## 🎉 Success Criteria

Your setup is complete when:

✅ You can publish to TestPyPI by pushing a `test-*` tag
✅ You can publish to PyPI by creating a GitHub Release
✅ No API tokens are stored anywhere
✅ Workflows complete without errors
✅ Packages install correctly from PyPI
✅ Team members understand the process

---

## 📞 Support

If you encounter issues:

1. Check the [Troubleshooting section](#troubleshooting)
2. Review [GitHub Workflows README](.github/README.md)
3. Consult [Complete Setup Guide](docs/github-trusted-publisher.md)
4. Check [PyPI Trusted Publishers FAQ](https://docs.pypi.org/trusted-publishers/)

---

**🎊 Congratulations!** You now have a secure, automated publishing pipeline using the latest best practices from PyPI.

**No tokens. No passwords. Just secure, automated publishing.**

