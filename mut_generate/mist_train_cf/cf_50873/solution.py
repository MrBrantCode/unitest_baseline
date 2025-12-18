"""
QUESTION:
Create a function named `password_checker` that takes a password or a list of passwords as input and returns 'Acceptable' if the password(s) meet the following conditions:
- The password length is between 8 to 20 characters.
- The password contains at least one uppercase letter, one lowercase letter, one digit, and one special character (@, #, $, %, ^, &, *).
- The password does not contain any spaces.
If a password does not meet any of these conditions, the function should return 'Unacceptable'. The function should be able to handle both single and multiple password inputs.
"""

def password_checker(passwords):
    if isinstance(passwords, list):  
        return [password_checker(password) for password in passwords]
    if not (8 <= len(passwords) <= 20):
        return 'Unacceptable'
    if " " in passwords:
        return 'Unacceptable'
    if not any(char.isdigit() for char in passwords):
        return 'Unacceptable'
    if not any(char.isupper() for char in passwords):
        return 'Unacceptable'
    if not any(char.islower() for char in passwords):
        return 'Unacceptable'
    if not any(char in '@#$%^&*' for char in passwords):
        return 'Unacceptable'
    return 'Acceptable'