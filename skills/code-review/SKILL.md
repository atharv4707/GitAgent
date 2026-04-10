---
name: code-review
description: Analyzes code quality, structure, and commit messages for technical issues
allowed-tools: Read
---

# Code Review Skill

Perform technical analysis of code and commit messages to identify code quality issues, security vulnerabilities, structural problems, and vague commit messages.

## Steps

1. Analyze the commit message â€” check length, context, and clarity
2. Scan for security patterns â€” password handling, authentication logic, direct comparisons on sensitive data
3. Check code structure â€” error handling, input validation, null checks, type safety

## Red Flags

- password + == operator: Security vulnerability
- login = true without session: Authentication bypass
- No try/catch or validation: Crash risk
- Commit message under 20 chars: Poor communication

## Output Format

```
CODE REVIEW
----------------------------------------
[Critical issue with explanation]
[Warning with context]
```
