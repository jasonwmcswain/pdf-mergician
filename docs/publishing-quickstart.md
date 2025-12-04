# 🚀 GitHub Trusted Publisher - Quick Start

**5-minute setup for automated PyPI publishing with GitHub Actions**

---

## Prerequisites

- ✅ GitHub repository with admin access
- ✅ PyPI account ([sign up](https://pypi.org/account/register/))
- ✅ TestPyPI account ([sign up](https://test.pypi.org/account/register/))

---

## Step 1: Configure PyPI (2 minutes)

### For New Projects (Pending Publisher)

1. Go to: https://pypi.org/manage/account/publishing/
2. Scroll to **"Add a new pending publisher"**
3. Fill in:
   ```
   PyPI Project Name:     pdf-mergician
   Owner:                 YOUR_GITHUB_USERNAME
   Repository name:       pdf-mergician
   Workflow name:         publish.yml
   Environment name:      pypi
   ```
4. Click **"Add"**

### For Existing Projects

1. Go to: https://pypi.org/manage/project/YOUR-PROJECT/settings/publishing/
2. Click **"Add a new publisher"**
3. Fill in the same information as above
4. Click **"Add"**

---

## Step 2: Configure TestPyPI (1 minute)

1. Go to: https://test.pypi.org/manage/account/publishing/
2. Add pending publisher:
   ```
   PyPI Project Name:     pdf-mergician
   Owner:                 YOUR_GITHUB_USERNAME
   Repository name:       pdf-mergician
   Workflow name:         publish-test.yml
   Environment name:      testpypi
   ```
3. Click **"Add"**

---

## Step 3: Create GitHub Environments (2 minutes)

1. Go to your GitHub repo → **Settings** → **Environments**
2. Create environment: `pypi`
   - ☑️ Optional: Add required reviewers for production safety
3. Create environment: `testpypi`
4. Done!

---

## Step 4: Test Publishing

### Test with TestPyPI

```bash
# Bump version (if needed)
make version-bump

# Create and push test tag
git tag test-2025.12.03.1
git push origin test-2025.12.03.1

# Watch workflow in GitHub Actions tab
```

Verify at: https://test.pypi.org/project/pdf-mergician/

### Publish to Production

```bash
# Create GitHub Release
# Go to: https://github.com/YOUR_USERNAME/pdf-mergician/releases/new
# - Tag: v2025.12.03.1
# - Title: Release 2025.12.03.1
# - Description: Release notes
# - Click "Publish release"

# Workflow runs automatically!
```

Verify at: https://pypi.org/project/pdf-mergician/

---

## ✅ Verification Checklist

- [ ] PyPI trusted publisher configured
- [ ] TestPyPI trusted publisher configured
- [ ] GitHub `pypi` environment created
- [ ] GitHub `testpypi` environment created
- [ ] Workflow files exist (`.github/workflows/publish*.yml`)
- [ ] Test tag published successfully to TestPyPI
- [ ] Production release published successfully to PyPI

---

## 🔧 Workflow Files

Your workflows should already be configured. Verify they exist:

- `.github/workflows/publish.yml` (Production)
- `.github/workflows/publish-test.yml` (TestPyPI)

**Critical requirements:**
```yaml
permissions:
  id-token: write  # ← Must have this!

environment:
  name: pypi  # ← Must match PyPI config
```

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| "Trusted publishing exchange failure" | Verify PyPI config matches workflow exactly |
| "Resource not accessible" | Add `id-token: write` permission |
| Workflow doesn't trigger | Create GitHub Release (not just tag) for production |
| Environment protection rules | Approve deployment in GitHub UI |

---

## 📚 Full Documentation

For detailed explanations, security considerations, and advanced configuration:

👉 **[Complete Trusted Publisher Guide](docs/github-trusted-publisher.md)**

---

## 🎯 Quick Commands

```bash
# Test publishing
make version-bump
git tag test-$(grep '^version' pyproject.toml | cut -d'"' -f2)
git push origin --tags

# Production publishing
# Create GitHub Release via UI or:
gh release create v$(grep '^version' pyproject.toml | cut -d'"' -f2) \
  --title "Release $(grep '^version' pyproject.toml | cut -d'"' -f2)" \
  --generate-notes
```

---

**🎉 That's it! Your package will now publish automatically with every release.**

**No tokens. No passwords. Just secure, automated publishing.**

