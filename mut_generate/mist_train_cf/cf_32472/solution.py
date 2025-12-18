"""
QUESTION:
Create a function named `validate_registration` that takes in 9 parameters: `password1`, `password2`, `name`, `modes`, `homepage`, `api_url`, `miptaurl`, `phone`, and `email`. The function should perform the following validations:
- Check if `password1` matches `password2`.
- Ensure `password1` is at least 8 characters long and contains one uppercase letter, one lowercase letter, one digit, and one special character.
- Verify `name` is not empty and contains only alphabets and spaces.
- Validate `modes` contains at least one mode and does not contain duplicates.
- Confirm `homepage`, `api_url`, and `miptaurl` start with "http://" or "https://".
- Verify `phone` is in a valid format (e.g., +1234567890).
- Validate `email` is in a valid format (e.g., example@example.com).
The function should return a string indicating whether the registration details are valid or not.
"""

import re

def validate_registration(password1, password2, name, modes, homepage, api_url, miptaurl, phone, email):
    if password1 != password2:
        return "Passwords do not match"

    if not re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password1):
        return "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character"

    if not name.replace(' ', '').isalpha():
        return "Name should only contain alphabets and spaces"

    if len(modes) == 0 or len(modes) != len(set(modes)):
        return "Modes list should contain at least one mode and not have any duplicates"

    if not homepage.startswith("http://") and not homepage.startswith("https://"):
        return "Homepage URL should start with 'http://' or 'https://'"

    if not api_url.startswith("http://") and not api_url.startswith("https://"):
        return "API URL should start with 'http://' or 'https://'"

    if not miptaurl.startswith("http://") and not miptaurl.startswith("https://"):
        return "MIPTA URL should start with 'http://' or 'https://'"

    if not re.match(r'^\+\d{10,15}$', phone):
        return "Invalid phone number format"

    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return "Invalid email address format"

    return "Registration details are valid"