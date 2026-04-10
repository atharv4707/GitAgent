---
name: bug-prediction
description: "Predicts potential failures, edge cases, and security vulnerabilities"
allowed-tools:
  - Read
---

# Bug Prediction Skill

## Purpose

Anticipate what will break in production by analyzing:
- Null/undefined access patterns
- Security vulnerabilities
- Type coercion issues
- Authentication bypasses
- Edge case failures

## How to Execute

1. **Trace data flow**
   - Identify where objects are accessed without null checks
   - Find property access on potentially undefined values

2. **Security vulnerability scan**
   - No password hashing → brute force risk
   - No rate limiting → DoS vulnerability
   - Plain text passwords → data breach risk
   - Missing session management → auth bypass

3. **Type safety analysis**
   - `==` usage → type coercion bugs
   - Missing validation → unexpected input handling

4. **Output format**
   ```
   🐞 BUG PREDICTION
   ----------------------------------------
   💥 [Crash scenario]
   🔓 [Security vulnerability]
   🎯 [Attack vector]
   ⚠️  [Edge case failure]
   ```

## Prediction Patterns

### Pattern: Null Access
```javascript
if (user.password == input)
```
**Prediction**: 💥 Fails if user is null or undefined

### Pattern: No Hashing
```javascript
password == input
```
**Predictions**:
- 🔓 No hashing → MAJOR SECURITY RISK
- 🎯 Vulnerable to brute force attacks
- 📊 Passwords exposed in memory/logs

### Pattern: Boolean Flag Auth
```javascript
login = true;
```
**Prediction**: 🚨 No session management → authentication bypass possible

## Severity Levels

- 💥 **Critical**: Will crash in production
- 🔓 **Security**: Exploitable vulnerability
- 🎯 **Attack Vector**: Specific exploit path
- ⚠️ **Warning**: Likely to cause issues

## Integration

This skill runs after code-review, building on technical issues to predict real-world failures.
