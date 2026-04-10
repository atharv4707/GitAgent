---
name: bug-prediction
description: Predicts potential failures, edge cases, and security vulnerabilities
allowed-tools: Read
---

# Bug Prediction Skill

Anticipate what will break in production by analyzing null access patterns, security vulnerabilities, type coercion issues, and authentication bypasses.

## Steps

1. Trace data flow â€” identify where objects are accessed without null checks
2. Security vulnerability scan â€” no hashing, no rate limiting, plain text passwords, missing session management
3. Type safety analysis â€” == usage, missing validation

## Prediction Patterns

- user.property access without null check: Crashes if user is null
- password == input with no hashing: Major security risk, brute force vulnerable
- login = true without session: Authentication bypass possible

## Severity Levels

- Critical: Will crash in production
- Security: Exploitable vulnerability
- Attack Vector: Specific exploit path
- Warning: Likely to cause issues

## Output Format

```
BUG PREDICTION
----------------------------------------
[Crash scenario]
[Security vulnerability]
[Attack vector]
[Edge case failure]
```
