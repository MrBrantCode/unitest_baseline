"""
QUESTION:
Create a function called `validate_signup_form` that takes in a dictionary containing user information: name, age, gender, email, and password. The function should validate the user's input based on the following requirements: 
- The name must be at least 5 characters long and consist of only letters.
- The age must be between 20 and 60.
- The gender must be one of 'male', 'female', or 'non-binary'.
- The email address must be in a valid format.
- The password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one digit, and one special character (!@#$%^&*).
- If any of the fields are empty or if the validation fails, return the corresponding error messages.
"""

import re

def validate_signup_form(user_info):
    """
    Validate the user's input based on the following requirements:
    - The name must be at least 5 characters long and consist of only letters.
    - The age must be between 20 and 60.
    - The gender must be one of 'male', 'female', or 'non-binary'.
    - The email address must be in a valid format.
    - The password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one digit, and one special character (!@#$%^&*).
    
    Args:
        user_info (dict): A dictionary containing user information: name, age, gender, email, and password.
    
    Returns:
        list: A list of error messages for invalid inputs or empty fields.
    """
    
    errors = []
    
    # Check if name is at least 5 characters long and consists of only letters
    if not user_info['name'] or not re.match('^[a-zA-Z]+$', user_info['name']) or len(user_info['name']) < 5:
        errors.append('Invalid name. Please enter a name with at least 5 characters and only letters.')
    
    # Check if age is between 20 and 60
    if not user_info['age'] or not user_info['age'].isdigit() or not 20 <= int(user_info['age']) <= 60:
        errors.append('Invalid age. Please enter an age between 20 and 60.')
    
    # Check if gender is one of 'male', 'female', or 'non-binary'
    if user_info['gender'] not in ['male', 'female', 'non-binary']:
        errors.append('Invalid gender. Please select one of the following: male, female, or non-binary.')
    
    # Check if email address is in a valid format
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not user_info['email'] or not re.match(email_regex, user_info['email']):
        errors.append('Invalid email address. Please enter a valid email address.')
    
    # Check if password is at least 8 characters long, contains at least one uppercase letter, one lowercase letter, one digit, and one special character
    password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    if not user_info['password'] or not re.match(password_regex, user_info['password']):
        errors.append('Invalid password. Please enter a password with at least 8 characters, one uppercase letter, one lowercase letter, one digit, and one special character.')
    
    return errors