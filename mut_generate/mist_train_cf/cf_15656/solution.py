"""
QUESTION:
Create a function called `validateRegistrationForm` that takes four parameters: `fullName`, `email`, `password`, and `confirmPassword`. The function should perform the following validations:
- The `fullName` field should not be empty.
- The `email` field should be a valid email address and unique (for the purpose of this problem, assume it is unique).
- The `password` field should be at least 8 characters long.
- The `confirmPassword` field should match the `password` field.

The function should return an object containing a boolean `isValid` indicating whether the form is valid, and an object `errorMessages` containing error messages for each invalid field. 

Note: Do not include any server-side validation, registration logic, or error handling for email uniqueness in this function. 

For example, the function call `validateRegistrationForm('John Doe', 'john@example.com', 'password123', 'password123')` should return `{ isValid: true, errorMessages: {} }`. The function call `validateRegistrationForm('', 'invalid-email', 'short', 'mismatch')` should return `{ isValid: false, errorMessages: { fullName: 'Full name is required', email: 'Invalid email', password: 'Password must be at least 8 characters long', confirmPassword: 'Passwords do not match' } }`.
"""

import re

def validateRegistrationForm(fullName, email, password, confirmPassword):
    """
    Validate a registration form.

    Args:
    fullName (str): The full name of the user.
    email (str): The email address of the user.
    password (str): The password of the user.
    confirmPassword (str): The confirmed password of the user.

    Returns:
    dict: A dictionary containing a boolean 'isValid' and a dictionary 'errorMessages'.
    """

    errorMessages = {}
    isValid = True

    # Check if full name is not empty
    if not fullName:
        errorMessages['fullName'] = 'Full name is required'
        isValid = False

    # Check if email is valid
    if not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', email):
        errorMessages['email'] = 'Invalid email'
        isValid = False

    # Check if password is at least 8 characters long
    if len(password) < 8:
        errorMessages['password'] = 'Password must be at least 8 characters long'
        isValid = False

    # Check if password and confirm password match
    if password != confirmPassword:
        errorMessages['confirmPassword'] = 'Passwords do not match'
        isValid = False

    return {'isValid': isValid, 'errorMessages': errorMessages}