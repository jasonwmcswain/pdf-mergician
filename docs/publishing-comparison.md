# Publishing Methods Comparison

This document compares the two methods available for publishing `merge-pdf` to PyPI.

## Quick Comparison

| Feature | Trusted Publishers (OIDC) | API Tokens |
|---------|---------------------------|------------|
| **Security** | ⭐⭐⭐⭐⭐ Short-lived (15 min) | ⭐⭐⭐ Long-lived |
| **Setup Complexity** | ⭐⭐⭐⭐ One-time config | ⭐⭐⭐⭐⭐ Simple |
| **Maintenance** | ⭐⭐⭐⭐⭐ Zero maintenance | ⭐⭐⭐ Token rotation needed |
| **Secrets Management** | ⭐⭐⭐⭐⭐ No secrets | ⭐⭐⭐ Must store securely |
| **PyPI Recommendation** | ✅ Recommended | ⚠️ Legacy |
| **CI/CD Integration** | ✅ GitHub Actions native | ✅ Works everywhere |
| **Manual Publishing** | ❌ Not supported | ✅ Supported |
| **Attack Surface** | ⭐⭐⭐⭐⭐ Minimal | ⭐⭐⭐ Moderate |

## Method 1: Trusted Publishers (Recommended) ⭐

### Overview

Uses OpenID Connect (OIDC) to authenticate GitHub Actions workflows with PyPI without requiring API tokens.

### How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                    Publishing Workflow                       │
└─────────────────────────────────────────────────────────────┘

1. Developer creates GitHub Release
   ↓
2. GitHub Actions workflow triggered
   ↓
3. GitHub issues OIDC token (signed, verifiable)
   ↓
4. Workflow sends OIDC token to PyPI
   ↓
5. PyPI verifies token against trusted publisher config
   ↓
6. PyPI mints short-lived API token (15 min)
   ↓
7. Package published automatically
   ↓
8. Token expires (no cleanup needed)
```

### Pros

✅ **No Secret Management**: No tokens to create, store, or rotate
✅ **Enhanced Security**: Tokens expire automatically after 15 minutes
✅ **Reduced Attack Surface**: No long-lived credentials to compromise
✅ **Audit Trail**: PyPI logs show exact workflow that published
✅ **PyPI Recommended**: Official best practice
✅ **Zero Maintenance**: Set once, works forever
✅ **Environment Protection**: Can require manual approval for releases

### Cons

❌ **GitHub Actions Only**: Requires GitHub Actions (not for local/manual publishing)
❌ **Initial Setup**: Requires one-time configuration on PyPI and GitHub
❌ **Learning Curve**: New concept for developers unfamiliar with OIDC

### Setup Time

- **Initial**: ~5 minutes
- **Ongoing**: 0 minutes

### Use Cases

- ✅ Automated releases via GitHub Actions
- ✅ Teams wanting maximum security
- ✅ Projects with frequent releases
- ✅ Open source projects
- ❌ Manual/local publishing
- ❌ Non-GitHub CI systems

### Setup Guide

📖 [GitHub Trusted Publisher Setup](github-trusted-publisher.md)
🚀 [Quick Start Guide](../GITHUB_PUBLISHING_QUICKSTART.md)

---

## Method 2: API Tokens (Traditional)

### Overview

Uses long-lived API tokens generated from PyPI and stored as GitHub Secrets or in `~/.pypirc`.

### How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                    Publishing Workflow                       │
└─────────────────────────────────────────────────────────────┘

1. Developer generates API token on PyPI (one-time)
   ↓
2. Token stored in GitHub Secrets or ~/.pypirc
   ↓
3. Workflow/script reads token from storage
   ↓
4. Token sent to PyPI with package
   ↓
5. PyPI validates token
   ↓
6. Package published
   ↓
7. Token remains valid (until manually revoked)
```

### Pros

✅ **Universal**: Works with any CI/CD system
✅ **Manual Publishing**: Can publish from local machine
✅ **Simple Concept**: Easy to understand
✅ **Flexible**: Works in any environment
✅ **Immediate**: No workflow configuration needed

### Cons

❌ **Security Risk**: Long-lived credentials can be compromised
❌ **Secret Management**: Must store and protect tokens
❌ **Maintenance**: Should rotate tokens periodically
❌ **Attack Surface**: Stolen token = full project access
❌ **No Expiration**: Valid until manually revoked
❌ **Legacy**: Not PyPI's recommended approach

### Setup Time

- **Initial**: ~2 minutes
- **Ongoing**: ~5 minutes per rotation (recommended quarterly)

### Use Cases

- ✅ Manual/local publishing
- ✅ Non-GitHub CI systems (GitLab, Jenkins, etc.)
- ✅ Quick testing/prototyping
- ✅ Developers who prefer traditional methods
- ❌ Maximum security requirements
- ❌ GitHub Actions workflows (use Trusted Publishers instead)

### Setup Guide

📖 [PyPI Credentials Setup](pypi-setup.md)

---

## Security Comparison

### Trusted Publishers (OIDC)

```
Token Lifetime: 15 minutes
┌─────────────────────────────────────────────────────────────┐
│ Token Created → Used → Expired (automatic)                   │
│ [====15 min====]                                             │
└─────────────────────────────────────────────────────────────┘

Risk Window: 15 minutes
Attack Scenarios Prevented:
✓ Stolen credentials from logs
✓ Compromised developer machines
✓ Leaked secrets in code
✓ Long-term credential exposure
```

### API Tokens

```
Token Lifetime: Until manually revoked
┌─────────────────────────────────────────────────────────────┐
│ Token Created ────────────────────────────────→ Revoked      │
│ [============ Months/Years ============]                     │
└─────────────────────────────────────────────────────────────┘

Risk Window: Months to years
Attack Scenarios:
✗ Stolen credentials remain valid
✗ Compromised machines can publish
✗ Leaked secrets in code/logs
✗ Forgotten tokens in old CI configs
```

---

## Migration Path

### From API Tokens to Trusted Publishers

1. **Set up Trusted Publishers** (5 minutes)
   - Configure on PyPI
   - Create GitHub environments
   - Update workflows

2. **Test with TestPyPI** (5 minutes)
   - Push test tag
   - Verify publishing works

3. **Publish to Production** (1 minute)
   - Create GitHub Release
   - Verify publishing works

4. **Clean Up** (2 minutes)
   - Revoke old API tokens
   - Remove tokens from GitHub Secrets
   - Delete `~/.pypirc` (optional)

**Total Migration Time: ~15 minutes**

---

## Recommendations

### For New Projects

**Use Trusted Publishers** from day one:
- Maximum security
- No maintenance burden
- PyPI recommended
- Future-proof

### For Existing Projects

**Migrate to Trusted Publishers** if:
- Using GitHub Actions for CI/CD
- Want improved security
- Tired of managing tokens
- Want to follow best practices

**Keep API Tokens** if:
- Need manual publishing capability
- Using non-GitHub CI systems
- Have specific workflow requirements

### For Teams

**Trusted Publishers** provide:
- No shared secrets
- Individual accountability (via GitHub)
- Environment-based approvals
- Audit trail

---

## Cost Comparison

| Aspect | Trusted Publishers | API Tokens |
|--------|-------------------|------------|
| **Setup Time** | 5 minutes | 2 minutes |
| **Ongoing Maintenance** | 0 minutes/year | ~20 minutes/year |
| **Security Incidents** | Near zero risk | Low-moderate risk |
| **Developer Onboarding** | Zero (no secrets) | 5 minutes per dev |
| **Token Rotation** | Automatic | Manual |

**Total Cost (1 year)**: Trusted Publishers wins by ~25 minutes/year per project

---

## Conclusion

### Choose Trusted Publishers If:

- ✅ Using GitHub Actions
- ✅ Want maximum security
- ✅ Prefer zero maintenance
- ✅ Following PyPI best practices
- ✅ Building open source projects

### Choose API Tokens If:

- ✅ Need manual publishing
- ✅ Using non-GitHub CI
- ✅ Have specific workflow needs
- ✅ Prefer traditional methods

---

## Additional Resources

- 📖 [PyPI Trusted Publishers Documentation](https://docs.pypi.org/trusted-publishers/)
- 📖 [GitHub Actions OIDC Documentation](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
- 📖 [PyPI API Token Documentation](https://pypi.org/help/#apitoken)
- 📖 [Security Best Practices](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)

