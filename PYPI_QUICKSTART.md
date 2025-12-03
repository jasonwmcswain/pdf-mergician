# PyPI Quick Start Guide

Fast track to publishing merge-pdf to PyPI.

## 🚀 5-Minute Setup

### 1. Create Accounts (2 minutes)

**TestPyPI:** https://test.pypi.org/account/register/
**PyPI:** https://pypi.org/account/register/

### 2. Enable 2FA (1 minute each)

Required for API tokens. Use Google Authenticator or similar app.

**TestPyPI:** https://test.pypi.org/manage/account/
**PyPI:** https://pypi.org/manage/account/

### 3. Create API Tokens (1 minute each)

**TestPyPI Token:**
1. Go to https://test.pypi.org/manage/account/
2. Scroll to "API tokens" → "Add API token"
3. Name: `merge-pdf-test`, Scope: "Entire account"
4. **Copy the token!** (starts with `pypi-`)

**PyPI Token:**
1. Go to https://pypi.org/manage/account/
2. Scroll to "API tokens" → "Add API token"
3. Name: `merge-pdf`, Scope: "Entire account"
4. **Copy the token!** (starts with `pypi-`)

### 4. Configure Credentials (1 minute)

Create `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR_PYPI_TOKEN_HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR_TESTPYPI_TOKEN_HERE
```

**Linux/Mac only:**
```bash
chmod 600 ~/.pypirc
```

### 5. Test It! (1 minute)

```bash
# Test on TestPyPI first
make publish-test

# Verify at: https://test.pypi.org/project/merge-pdf/

# When ready, publish to PyPI
make publish
```

---

## 📋 Complete Workflow

```bash
# 1. Full validation
make clean-validate

# 2. Test on TestPyPI
make publish-test

# 3. Verify installation
pip install -i https://test.pypi.org/simple/ merge-pdf

# 4. Publish to PyPI
make publish

# OR: Do it all at once!
make all
```

---

## 🔑 Template Files

### Copy `.pypirc.example`

```bash
cp .pypirc.example ~/.pypirc
# Edit and add your tokens
vim ~/.pypirc
# Secure it (Linux/Mac)
chmod 600 ~/.pypirc
```

---

## ⚠️ Important Notes

1. **Username is always `__token__`** (with double underscores)
2. **Tokens start with `pypi-`** and are very long
3. **Never commit tokens to git!**
4. **TestPyPI and PyPI are separate** - need both accounts
5. **2FA is required** for API tokens

---

## 🆘 Troubleshooting

### "Invalid authentication"
- Check username is `__token__`
- Verify token is complete (no spaces)
- Ensure 2FA is enabled

### "403 Forbidden"
- Package name might be taken
- Token needs correct scope
- Try account-wide scope first

### "Package already exists"
- Bump version: `make version-bump`
- Rebuild: `make build`
- Try again

---

## 📚 Full Documentation

See [docs/pypi-setup.md](docs/pypi-setup.md) for:
- Detailed setup instructions
- Security best practices
- CI/CD configuration
- Advanced troubleshooting

---

## ✅ Checklist

- [ ] TestPyPI account created
- [ ] PyPI account created
- [ ] 2FA enabled on both
- [ ] TestPyPI token created
- [ ] PyPI token created
- [ ] `~/.pypirc` configured
- [ ] File permissions set (Linux/Mac)
- [ ] Tested with `make publish-test`
- [ ] Ready to `make publish`!

---

**Need help?** See [docs/pypi-setup.md](docs/pypi-setup.md) for complete instructions.

