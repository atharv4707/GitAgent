#!/usr/bin/env python3
"""
GitSpecter AI Runner - Uses FREE APIs (Groq or Gemini)
Get free key at: https://console.groq.com  OR  https://aistudio.google.com
"""

import os
import sys
import subprocess

# ── Load system prompt from gitagent export ──────────────────────────
def get_system_prompt():
    soul = open("SOUL.md", encoding="utf-8").read()
    rules = open("RULES.md", encoding="utf-8").read()
    return soul + "\n\n" + rules


SYSTEM_PROMPT = get_system_prompt()

USER_INPUT = """
Analyze this:

Commit Message: "fixed login issue"

Code:
if (user.password == input) {
    login = true;
}

Developer Note: "I think this is fine for now, will improve later"

Respond in 4 sections: CODE REVIEW, BUG PREDICTION, MINDSET ANALYSIS, TRUTH MODE.
"""


# ── Option A: Groq (FREE) ─────────────────────────────────────────────
def run_with_groq():
    try:
        from groq import Groq
    except ImportError:
        print("Installing groq...")
        subprocess.run([sys.executable, "-m", "pip", "install", "groq"], check=True)
        from groq import Groq

    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("\n❌ Missing GROQ_API_KEY")
        print("1. Go to https://console.groq.com")
        print("2. Sign up free (no credit card)")
        print("3. Create API key")
        print("4. Run: $env:GROQ_API_KEY = 'your-key-here'")
        sys.exit(1)

    client = Groq(api_key=api_key)
    print("🔍 GitSpecter is analyzing... (via Groq - free)\n")

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # free, fast, powerful
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_INPUT}
        ],
        temperature=0.7,
        max_tokens=1500
    )

    print(response.choices[0].message.content)


# ── Option B: Gemini (FREE) ───────────────────────────────────────────
def run_with_gemini():
    try:
        import google.generativeai as genai
    except ImportError:
        print("Installing google-generativeai...")
        subprocess.run([sys.executable, "-m", "pip", "install", "google-generativeai"], check=True)
        import google.generativeai as genai

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("\n❌ Missing GEMINI_API_KEY")
        print("1. Go to https://aistudio.google.com")
        print("2. Sign in with Google account (free)")
        print("3. Click 'Get API Key'")
        print("4. Run: $env:GEMINI_API_KEY = 'your-key-here'")
        sys.exit(1)

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",  # free tier
        system_instruction=SYSTEM_PROMPT
    )

    print("🔍 GitSpecter is analyzing... (via Gemini - free)\n")
    response = model.generate_content(USER_INPUT)
    print(response.text)


# ── Main ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    provider = sys.argv[1] if len(sys.argv) > 1 else "groq"

    print("=" * 60)
    print("💀 GitSpecter — AI Code Reviewer")
    print("=" * 60)
    print()

    if provider == "gemini":
        run_with_gemini()
    else:
        run_with_groq()
