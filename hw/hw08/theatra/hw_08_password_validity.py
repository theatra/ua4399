import re

def check_password(password):
    if len(password) < 6 or len(password) > 16:
        return "Invalid: Password must be 6–16 characters long."
    if not re.search(r"[a-z]", password):
        return "Invalid: Must contain at least one lowercase letter."
    if not re.search(r"[A-Z]", password):
        return "Invalid: Must contain at least one uppercase letter."
    if not re.search(r"[0-9]", password):
        return "Invalid: Must contain at least one digit."
    if not re.search(r"[$#@]", password):
        return "Invalid: Must contain at least one special character from $#@."
    return "Password is valid."


user_input = input("Enter your password: ")
print(check_password(user_input))