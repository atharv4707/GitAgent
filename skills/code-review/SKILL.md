---
name: code-review
description: "Analyzes code quality, structure, and commit messages for technical issues"
allowed-tools:
  - Read
---

# Code Review Skill

## Purpose

Perform technical analysis of code and commit messages to identify:
- Code quality issues
- Security vulnerabilities
- Structural problems
- Poor practices
- Vague or unprofessional commit messages

## How to Execute

1. **Analyze the commit message**
   - Check length (< 20 chars = vague)
   - Check for context and clarity
   - Verify professional formatting

2. **Scan for security patterns**
   - Password handling (must use hashing)
   - Authentication logic (must have session management)
   - Direct comparisons on sensitive data (❌ ==, ✅ secure methods)

3. **Check code structure**
   - Error handling presence
   - Input validation
   - Null/undefined checks
   - Type safety (== vs ===)

4. **Output format**
   ```
   🧑‍💻 CODE REVIEW
   ----------------------------------------
   ❌ [Critical issue with explanation]
   ⚠️  [Warning with context]
   ```

## Red Flags

- `password` + `==` → Security vulnerability
- `login = true` without session → Authentication bypass
- No try/catch or validation → Crash risk
- Commit message < 20 chars → Poor communication

## Examples

### Bad Code
```javascript
if (user.password == input) {
    login = true;
}
```

### Review Output
```
❌ Weak comparison logic (== instead of secure method)
   Passwords should NEVER be compared directly
❌ Boolean flag assignment without proper session handling
❌ No error handling or validation
```

## Integration

This skill runs first in the analysis pipeline, providing the technical foundation for bug prediction and mindset analysis.
