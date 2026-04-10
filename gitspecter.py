#!/usr/bin/env python3
"""
GitSpecter - The AI Code Reviewer That Reviews Developers
"""

import sys
import re


class GitSpecter:
    def __init__(self):
        self.name = "GitSpecter"
        
    def analyze(self, commit_msg, code, dev_note=""):
        """Main analysis function"""
        print("=" * 60)
        print(f"🔍 {self.name} Analysis")
        print("=" * 60)
        print()
        
        self._code_review(commit_msg, code)
        print()
        self._bug_prediction(code)
        print()
        self._mindset_analysis(commit_msg, code, dev_note)
        print()
        self._truth_mode(commit_msg, code, dev_note)
        print()
        self._suggestions(code)
        print()
        print("=" * 60)
        print('💀 "Most tools review code. GitSpecter reviews the developer."')
        print("=" * 60)
    
    def _code_review(self, commit_msg, code):
        """Technical code review"""
        print("🧑‍💻 CODE REVIEW")
        print("-" * 40)
        
        issues = []
        
        # Analyze commit message
        if len(commit_msg) < 20 or not re.search(r'[A-Z]', commit_msg):
            issues.append("❌ Commit message is vague and unprofessional")
            issues.append("   No context of what was actually fixed")
        
        # Analyze code patterns
        if "==" in code and "password" in code.lower():
            issues.append("❌ Weak comparison logic (== instead of secure method)")
            issues.append("   Passwords should NEVER be compared directly")
        
        if "==" in code and "!=" not in code:
            issues.append("⚠️  Using loose equality - potential type coercion bugs")
        
        if "login = true" in code.lower():
            issues.append("❌ Boolean flag assignment without proper session handling")
        
        if not re.search(r'(try|catch|if.*null|validate)', code, re.IGNORECASE):
            issues.append("❌ No error handling or validation")
        
        for issue in issues:
            print(issue)
    
    def _bug_prediction(self, code):
        """Predict potential bugs"""
        print("🐞 BUG PREDICTION")
        print("-" * 40)
        
        bugs = []
        
        if "user." in code and "if" not in code.lower().split("user.")[0]:
            bugs.append("💥 Fails if user is null or undefined")
        
        if "password" in code.lower() and "hash" not in code.lower():
            bugs.append("🔓 No hashing → MAJOR SECURITY RISK")
            bugs.append("🎯 Vulnerable to brute force attacks")
            bugs.append("📊 Passwords exposed in memory/logs")
        
        if "==" in code:
            bugs.append("⚠️  Type coercion can cause unexpected behavior")
        
        if "login = true" in code.lower() and "session" not in code.lower():
            bugs.append("🚨 No session management → authentication bypass possible")
        
        for bug in bugs:
            print(bug)
    
    def _mindset_analysis(self, commit_msg, code, dev_note):
        """Analyze developer's thinking"""
        print("🧠 MINDSET ANALYSIS")
        print("-" * 40)
        
        if "later" in dev_note.lower() or "for now" in dev_note.lower():
            print("🎯 You are prioritizing quick completion over correctness")
            print("⚠️  'Later' never comes - technical debt compounds")
        
        if "fixed" in commit_msg.lower() and len(commit_msg) < 20:
            print("📝 You're avoiding documentation and clear communication")
        
        if "password" in code.lower() and "==" in code:
            print("🔐 You're avoiding proper authentication design")
            print("💭 Likely thinking: 'Security can wait'")
            print("❌ Reality: Security cannot wait")
        
        if "think" in dev_note.lower() and "fine" in dev_note.lower():
            print("🤔 You're uncertain but proceeding anyway")
            print("⚠️  Gut feeling ≠ Code quality")
    
    def _truth_mode(self, commit_msg, code, dev_note):
        """Brutal honesty section"""
        print("💀 TRUTH MODE")
        print("-" * 40)
        
        if "later" in dev_note.lower():
            print('"This is not a fix. This is a shortcut that creates bigger problems."')
        elif "password" in code.lower() and "==" in code:
            print('"This code is a security incident waiting to happen."')
        elif len(commit_msg) < 15:
            print('"Your commit message tells me nothing. Do better."')
        else:
            print('"This needs serious work before it touches production."')
    
    def _suggestions(self, code):
        """Provide improvements"""
        print("✅ IMPROVEMENTS NEEDED")
        print("-" * 40)
        
        if "password" in code.lower():
            print("1. Use bcrypt/argon2 for password hashing")
            print("2. Implement proper authentication library")
            print("3. Add rate limiting for login attempts")
        
        print("4. Write descriptive commit messages (what, why, how)")
        print("5. Add input validation and error handling")
        print("6. Implement proper session management")
        print("7. Add unit tests for authentication logic")


def main():
    """Demo scenarios"""
    specter = GitSpecter()
    
    print("\n")
    print("🎯 SCENARIO 1: The Original Example")
    print()
    
    commit_msg = "fixed login issue"
    code = """if (user.password == input) {
    login = true;
}"""
    dev_note = "I think this is fine for now, will improve later"
    
    specter.analyze(commit_msg, code, dev_note)
    
    print("\n\n")
    print("🎯 SCENARIO 2: Vague Commit")
    print()
    
    commit_msg2 = "updated stuff"
    code2 = """function process() {
    var x = getData();
    x.map(i => i.value).filter(v => v);
    return x;
}"""
    dev_note2 = "works somehow"
    
    specter.analyze(commit_msg2, code2, dev_note2)
    
    print("\n\n")
    print("🎯 SCENARIO 3: Null Check Pattern")
    print()
    
    commit_msg3 = "added check"
    code3 = """if (data != null) {
    process(data);
}"""
    dev_note3 = "I'll refactor later"
    
    specter.analyze(commit_msg3, code3, dev_note3)


if __name__ == "__main__":
    main()
