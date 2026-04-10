# 🎯 GitSpecter Demo Guide

## The Hook

Start with this line:

> "Most tools review code. GitSpecter reviews the developer."

Let that sink in for a second.

## Live Demo Flow

### 1. Show the Problem (30 seconds)

"Here's what most developers do:"

```javascript
// Commit: "fixed login issue"
if (user.password == input) {
    login = true;
}
// Dev note: "I think this is fine for now, will improve later"
```

"Looks simple, right? Let's see what GitSpecter thinks."

### 2. Run GitSpecter (45 seconds)

```bash
python gitspecter.py
```

Walk through the output:

**CODE REVIEW** - "See these red flags? Weak comparison, no hashing, no error handling."

**BUG PREDICTION** - "Here's what breaks: null user crashes it, no hashing means security breach, authentication bypass possible."

**MINDSET ANALYSIS** - "This is the interesting part. GitSpecter sees 'later' and knows: you're prioritizing speed over correctness. 'Later' never comes."

**TRUTH MODE** - Pause here. Read it slowly:

> "This is not a fix. This is a shortcut that creates bigger problems."

Let that land.

### 3. The Difference (30 seconds)

"Traditional code review tools would say: 'Consider using bcrypt for password hashing.'

GitSpecter says: 'No hashing → MAJOR SECURITY RISK. This is not production-ready.'

See the difference? One is a suggestion. The other is truth."

### 4. The Architecture (30 seconds)

"GitSpecter is built using the gitagent format:
- SOUL.md defines the personality
- RULES.md enforces the analysis framework
- Four skills work together: code-review → bug-prediction → mindset-analysis → truth-mode

Each skill builds on the last, going from 'what's wrong' to 'why you wrote it wrong.'"

### 5. The Close (15 seconds)

"GitSpecter doesn't just make your code better. It makes you better.

Because most tools review code. GitSpecter reviews the developer."

## Quick Demo Scenarios

If you have extra time, show these:

### Scenario 2: Vague Commit
```
Commit: "updated stuff"
Code: messy function
Note: "works somehow"
```

Truth Mode: "Your commit message tells me nothing. Do better."

### Scenario 3: Null Check
```javascript
if (data != null) {
    process(data);
}
```

Note: "I'll refactor later"

Truth Mode: "This is not a fix. This is a shortcut that creates bigger problems."

## Judging Criteria Alignment

Point out:

1. **Agent Quality (30%)**: "SOUL.md gives GitSpecter a distinct personality - senior engineer who doesn't sugarcoat"

2. **Skill Design (25%)**: "Four focused skills, each documented, each building on the last"

3. **Working Demo (25%)**: "You just saw it run. It works."

4. **Creativity (20%)**: "Nobody else is reviewing the developer's thinking. That's the innovation."

## Pro Tips

- Pause after Truth Mode statements
- Let judges react to the brutal honesty
- Emphasize "reviews the developer" not "reviews code"
- Show confidence - this is a product, not a project
- If asked about real-world use: "Pre-commit hooks, CI/CD gates, junior dev mentoring"

## The Memorable Moment

End every demo with:

💀 "Most tools review code. GitSpecter reviews the developer."

That's your mic drop. 🎤
