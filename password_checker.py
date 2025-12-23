import re

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*]", password):
        score += 1

    if score <= 2:
        return "Weak Password ❌" #for formatting
    elif score <= 4:
        return "Moderate Password ⚠️" #for formatting
    else:
        return "Strong Password ✅" #for formatting

password = input("Enter password to check: ")
print(check_password(password))
