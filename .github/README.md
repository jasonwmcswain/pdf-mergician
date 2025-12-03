# GitHub Actions Workflows

This directory contains CI/CD workflows for the `merge-pdf` project.

## Workflows

### `ci.yml` - Continuous Integration

Runs on every push and pull request to `main` and `develop` branches.

**Jobs:**
- **test**: Runs tests across multiple Python versions (3.8-3.12) and operating systems (Ubuntu, macOS, Windows)
- **build**: Builds the package and uploads artifacts

**What it does:**
1. Sets up Python environment
2. Installs dependencies
3. Runs linting with `ruff`
4. Runs tests with `pytest`
5. Generates coverage reports
6. Uploads coverage to Codecov
7. Builds the package distribution

### `publish.yml` - PyPI Publishing (Trusted Publisher) ⭐

**Recommended Method**: Uses OpenID Connect (OIDC) for secure, credential-free publishing.

**Triggers:**
- When a GitHub Release is published
- Manual workflow dispatch

**What it does:**
1. Builds the package
2. Checks package metadata
3. Publishes to PyPI using **Trusted Publishing** (no API token needed!)

**Requirements:**
- Trusted publisher configured on PyPI
- GitHub environment `pypi` created
- Workflow has `id-token: write` permission

### `publish-test.yml` - TestPyPI Publishing (Trusted Publisher)

**For Testing**: Publishes to TestPyPI before production release.

**Triggers:**
- Tags starting with `test-` (e.g., `test-2025.12.03.1`)
- Manual workflow dispatch

**What it does:**
1. Builds the package
2. Publishes to TestPyPI using **Trusted Publishing**

**Requirements:**
- Trusted publisher configured on TestPyPI
- GitHub environment `testpypi` created

## Configuration

### Method 1: Trusted Publishers (Recommended) ⭐

**No secrets required!** Uses OIDC for authentication.

#### Setup Steps:

1. **Configure PyPI Trusted Publisher**:
   - Go to: https://pypi.org/manage/account/publishing/
   - Add pending publisher:
     ```
     PyPI Project Name:     merge-pdf
     Owner:                 YOUR_GITHUB_USERNAME
     Repository name:       merge-pdf
     Workflow name:         publish.yml
     Environment name:      pypi
     ```

2. **Configure TestPyPI Trusted Publisher**:
   - Go to: https://test.pypi.org/manage/account/publishing/
   - Add pending publisher:
     ```
     PyPI Project Name:     merge-pdf
     Owner:                 YOUR_GITHUB_USERNAME
     Repository name:       merge-pdf
     Workflow name:         publish-test.yml
     Environment name:      testpypi
     ```

3. **Create GitHub Environments**:
   - Go to: **Settings** → **Environments**
   - Create environment: `pypi`
   - Create environment: `testpypi`
   - Optional: Add required reviewers for production safety

📖 **Complete Guide**: [GitHub Trusted Publisher Setup](../docs/github-trusted-publisher.md)
🚀 **Quick Start**: [GITHUB_PUBLISHING_QUICKSTART.md](../GITHUB_PUBLISHING_QUICKSTART.md)

### Method 2: API Tokens (Legacy)

If you prefer traditional API tokens:

**Secrets Required:**
- `PYPI_API_TOKEN`: Your PyPI API token
- `TEST_PYPI_API_TOKEN`: Your TestPyPI API token

**Note**: You'll need to modify the workflows to use token-based authentication instead of trusted publishing.

## Usage

### Running CI

CI runs automatically on:
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches

### Testing with TestPyPI

```bash
# Bump version
make version-bump

# Create and push test tag
git tag test-2025.12.03.1
git push origin test-2025.12.03.1

# Workflow runs automatically
# Verify at: https://test.pypi.org/project/merge-pdf/
```

### Publishing to Production PyPI

#### Option 1: GitHub UI (Recommended)

1. Go to **Releases** → **Draft a new release**
2. Create a new tag (e.g., `v2025.12.03.1`)
3. Add release notes
4. Click **Publish release**
5. Workflow runs automatically!

#### Option 2: Command Line (with GitHub CLI)

```bash
# Bump version
make version-bump

# Create release
gh release create v$(grep '^version' pyproject.toml | cut -d'"' -f2) \
  --title "Release $(grep '^version' pyproject.toml | cut -d'"' -f2)" \
  --generate-notes

# Workflow runs automatically
```

#### Option 3: Manual Workflow Dispatch

1. Go to **Actions** → **Publish to PyPI**
2. Click **Run workflow**
3. Select branch and run

## Monitoring

- View workflow runs in the **Actions** tab
- Check build status badges in the main README
- Review coverage reports on Codecov
- Monitor releases on [PyPI](https://pypi.org/project/merge-pdf/)

## Troubleshooting

### CI Failures

- Check the workflow logs in the Actions tab
- Common issues:
  - Linting errors: Run `make lint-fix` locally
  - Test failures: Run `make test` locally
  - Build errors: Run `make build` locally

### Publishing Failures (Trusted Publishing)

| Error | Solution |
|-------|----------|
| "Trusted publishing exchange failure" | Verify PyPI config matches workflow exactly (owner, repo, workflow name, environment) |
| "Resource not accessible by integration" | Ensure workflow has `permissions: id-token: write` |
| "Environment protection rules not satisfied" | Approve deployment in GitHub UI or adjust environment settings |
| Workflow doesn't trigger | For production: Create GitHub Release (not just tag). For test: Push tag starting with `test-` |

### Publishing Failures (API Tokens)

- Verify tokens are correctly set in GitHub Secrets
- Ensure the version hasn't been published before
- Check PyPI status: https://status.python.org/

## Local Testing

Before pushing, test locally:

```bash
# Run full validation
make validate

# Or run individual steps
make lint
make test
make build

# Test complete pipeline
make clean-validate
```

## Security

### Trusted Publishing Benefits

- ✅ No long-lived credentials
- ✅ Automatic token expiration (15 minutes)
- ✅ No secrets to manage
- ✅ Reduced attack surface
- ✅ PyPI-recommended approach

### Best Practices

1. **Use Environment Protection**:
   - Require manual approval for production releases
   - Restrict deployments to specific branches

2. **Minimal Permissions**:
   - Only grant `id-token: write` to publish jobs
   - Keep top-level permissions minimal

3. **Branch Protection**:
   - Protect `main` branch
   - Require PR reviews before merging

4. **Monitor Releases**:
   - Review PyPI release logs regularly
   - Set up notifications for new releases

## Additional Resources

- 📖 [PyPI Trusted Publishers Documentation](https://docs.pypi.org/trusted-publishers/)
- 📖 [GitHub Actions OIDC Documentation](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
- 📖 [PyPA Publish Action](https://github.com/pypa/gh-action-pypi-publish)
- 📖 [Complete Setup Guide](../docs/github-trusted-publisher.md)
