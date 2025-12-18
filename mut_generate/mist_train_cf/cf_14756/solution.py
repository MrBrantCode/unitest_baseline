"""
QUESTION:
Create a function named `check_password` that verifies if a given password meets certain criteria. The function should check if the password is at least 8 characters long, contains at least one uppercase letter, one lowercase letter, and one numeric digit, and does not contain a given username. The function should return `True` if the password meets all the criteria and `False` otherwise.
"""

def check_password(username, password):
    """
    This function checks if a given password meets certain criteria.
    
    Parameters:
    username (str): The username of the user.
    password (str): The password to be checked.
    
    Returns:
    bool: True if the password meets all the criteria, False otherwise.
    """
    
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False
    
    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False
    
    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False
    
    # Check if the password contains at least one numeric digit
    if not any(char.isdigit() for char in password):
        return False
    
    # Check if the password does not contain the username
    if username in password:
        return False
    
    # If all checks pass, return True
    return True