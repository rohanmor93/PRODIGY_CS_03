import re

def check_password_strength(password):
    feedback = []

    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"\d", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    common = password.lower() in ['password', '123456', 'admin', 'qwerty', 'letmein']

    score = sum([length, bool(upper), bool(lower), bool(digit), bool(special)])

    if not length:
        feedback.append("- Password should be at least 8 characters long.")
    if not upper:
        feedback.append("- Add at least one UPPERCASE letter.")
    if not lower:
        feedback.append("- Add at least one lowercase letter.")
    if not digit:
        feedback.append("- Include at least one number.")
    if not special:
        feedback.append("- Include at least one special character (e.g. !@#...).")
    if common:
        feedback.append("- Avoid common or easy-to-guess passwords.")

    if score <= 2:
        strength = "❌ Weak"
    elif score == 3 or score == 4:
        strength = "⚠️ Moderate"
    else:
        strength = "✅ Strong"

    return strength, feedback

# CLI interface
if __name__ == "__main__":
    print("🔐 Password Strength Checker")
    password = input("Enter your password: ")
    strength, tips = check_password_strength(password)

    print(f"\nStrength: {strength}")
    if tips:
        print("Suggestions to improve:")
        for tip in tips:
            print(tip)
    else:
        print("Great job! Your password is strong.")
