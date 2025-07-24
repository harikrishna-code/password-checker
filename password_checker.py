import re

def check_strength(password):
    score = 0

    # Rule 1: Length at least 8
    if len(password) >= 8:
        score += 1
    else:
        print("Too short (minimum 8 characters)")

    # Rule 2: At least one digit
    if re.search(r"\d", password):
        score += 1
    else:
        print("No number (0–9)")

    # Rule 3: At least one uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        print("No uppercase letter (A–Z)")

    # Rule 4: At least one lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        print("No lowercase letter (a–z)")

    # Rule 5: At least one special symbol
    if re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>?,./]", password):
        score += 1
    else:
        print("No special symbol (!@#$...)")

    # Final score interpretation
    print(f"\n Password Score: {score}/5")

    if score <= 1:
        print("Very Weak Password")
    elif score == 2:
        print("⚠Weak Password")
    elif score == 3:
        print("⚠Moderate Password")
    elif score == 4:
        print("Strong Password")
    else:
        print("Very Strong Password!")

# Get input from user
user_password = input("Enter your password: ")
check_strength(user_password)
