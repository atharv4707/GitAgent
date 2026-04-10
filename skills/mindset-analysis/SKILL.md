---
name: mindset-analysis
description: "Analyzes developer thinking patterns, shortcuts, and decision-making"
allowed-tools:
  - Read
---

# Mindset Analysis Skill

## Purpose

Reveal the thinking behind the code by analyzing:
- Developer notes and comments
- Commit message quality
- Code patterns that reveal shortcuts
- Language that signals uncertainty or avoidance

## How to Execute

1. **Parse developer language**
   - "later" → procrastination, technical debt
   - "for now" → temporary solutions becoming permanent
   - "I think" → uncertainty without validation
   - "fine" → settling for less than quality

2. **Analyze commit patterns**
   - Vague messages → poor communication habits
   - Missing context → avoiding documentation
   - Short commits → rushing or carelessness

3. **Identify avoidance patterns**
   - Security shortcuts → "security can wait" mentality
   - Missing tests → avoiding verification
   - No error handling → optimistic coding

4. **Output format**
   ```
   🧠 MINDSET ANALYSIS
   ----------------------------------------
   🎯 [Core thinking pattern]
   ⚠️  [Consequence of this thinking]
   💭 [What developer is likely thinking]
   ❌ [Reality check]
   ```

## Language Signals

### "Later" Pattern
```
"I'll improve later"
"Will refactor later"
```
**Analysis**:
```
🎯 You are prioritizing quick completion over correctness
⚠️  'Later' never comes - technical debt compounds
```

### "For Now" Pattern
```
"This is fine for now"
```
**Analysis**:
```
💭 Likely thinking: 'Good enough for now'
❌ Reality: Temporary solutions become permanent
```

### "I Think" Pattern
```
"I think this is fine"
```
**Analysis**:
```
🤔 You're uncertain but proceeding anyway
⚠️  Gut feeling ≠ Code quality
```

### Security Avoidance
```javascript
if (password == input) // no hashing
```
**Analysis**:
```
🔐 You're avoiding proper authentication design
💭 Likely thinking: 'Security can wait'
❌ Reality: Security cannot wait
```

## Mindset Categories

1. **Procrastination**: "later", "eventually", "soon"
2. **Uncertainty**: "I think", "maybe", "probably"
3. **Shortcuts**: "for now", "quick fix", "temporary"
4. **Avoidance**: Vague commits, missing tests, no docs
5. **Optimism Bias**: No error handling, no validation

## Integration

This skill runs after bug-prediction, connecting technical issues to the thinking that created them.
