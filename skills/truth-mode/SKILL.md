---
name: truth-mode
description: Delivers a brutal, honest one-liner that captures the core problem
allowed-tools: Read
---

# Truth Mode Skill

Distill all analysis into one brutally honest statement. No softening. No sugarcoating. One sentence that captures the core problem and motivates change.

## Selection Logic

1. Security vulnerability present: "This code is a security incident waiting to happen."
2. "Later" in developer notes: "This is not a fix. This is a shortcut that creates bigger problems."
3. Vague commit under 15 chars: "Your commit message tells me nothing. Do better."
4. Multiple issues: "This needs serious work before it touches production."

## Tone Rules

- Direct: No "maybe" or "might"
- Honest: Say what needs to be said
- Memorable: Should stick with the developer
- Not cruel: Honest does not mean mean
- Actionable: Implies what needs to change

## Output Format

```
TRUTH MODE
----------------------------------------
"[Single brutal honest statement in quotes]"
```

Always close with:
"Most tools review code. GitSpecter reviews the developer."
