---
name: truth-mode
description: "Delivers brutal, honest one-liner that captures the core problem"
allowed-tools:
  - Read
---

# Truth Mode Skill

## Purpose

Distill all analysis into one brutally honest statement that:
- Cuts through excuses
- States the core problem clearly
- Motivates change through honesty
- Leaves no room for misinterpretation

## How to Execute

1. **Synthesize all findings**
   - Review code issues from code-review
   - Consider predicted failures from bug-prediction
   - Factor in thinking patterns from mindset-analysis

2. **Identify the core problem**
   - Is it a security issue?
   - Is it a shortcut mentality?
   - Is it poor communication?
   - Is it technical debt?

3. **Craft the truth statement**
   - One sentence maximum
   - No softening language
   - Direct and memorable
   - Actionable implication

4. **Output format**
   ```
   💀 TRUTH MODE
   ----------------------------------------
   "[Brutal honest statement in quotes]"
   ```

## Truth Templates

### Security Issues
```
"This code is a security incident waiting to happen."
"No hashing = no security. This is not production-ready."
```

### Shortcut Mentality
```
"This is not a fix. This is a shortcut that creates bigger problems."
"'Later' is not a strategy. It's technical debt with interest."
```

### Poor Communication
```
"Your commit message tells me nothing. Do better."
"Vague commits reflect vague thinking."
```

### Quality Issues
```
"This needs serious work before it touches production."
"You're writing code that you know is broken."
```

### Avoidance Patterns
```
"You're avoiding the real problem by creating a temporary one."
"This is what happens when you code without thinking."
```

## Selection Logic

Choose based on severity:

1. **Security vulnerability** → Always prioritize
   - "This code is a security incident waiting to happen."

2. **"Later" in dev notes** → Technical debt focus
   - "This is not a fix. This is a shortcut that creates bigger problems."

3. **Vague commit (< 15 chars)** → Communication focus
   - "Your commit message tells me nothing. Do better."

4. **Multiple issues** → General quality statement
   - "This needs serious work before it touches production."

## Tone Guidelines

- **Direct**: No "maybe" or "might"
- **Honest**: Say what needs to be said
- **Memorable**: Should stick with the developer
- **Not cruel**: Honest ≠ mean
- **Actionable**: Implies what needs to change

## Integration

This skill runs last, providing the memorable closing statement that drives home the message.

Always end with the signature:
```
💀 "Most tools review code. GitSpecter reviews the developer."
```
