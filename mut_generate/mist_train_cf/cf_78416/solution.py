"""
QUESTION:
Create a function `password_complexity(password)` that assesses the complexity of a given password and returns a dictionary with two keys: 'strength' and 'suggestions'. 

The 'strength' key should contain a numerical value representing the password's complexity based on the following criteria:
- The password contains at least one number.
- The password contains at least one uppercase letter.
- The password contains at least one lowercase letter.
- The password contains at least one special character.
- The password is at least 8 characters long.

The 'suggestions' key should contain a list of suggestions for enhancing the password's complexity, based on the above criteria. 

Restrictions: 
- The function should not take any additional arguments other than the password.
- The function should return a dictionary with the exact keys 'strength' and 'suggestions'.
"""

def password_complexity(password):
    has_number = any(char.isdigit() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_special = any(not char.isalnum() for char in password)
    has_min_length = len(password) >= 8
    suggestions = []

    if not has_number:
        suggestions.append('Add at least one number.')
    if not has_uppercase:
        suggestions.append('Add at least one uppercase letter.')
    if not has_lowercase:
        suggestions.append('Add at least one lowercase letter.')
    if not has_special:
        suggestions.append('Add at least one special character.')
    if not has_min_length:
        suggestions.append('Increase password length to at least 8.')

    return {
        'strength': sum([has_number, has_uppercase, has_lowercase, has_special, has_min_length]),
        'suggestions': suggestions
    }