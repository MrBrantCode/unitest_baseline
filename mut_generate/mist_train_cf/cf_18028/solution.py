"""
QUESTION:
Write a function `validate_login` that validates user login credentials after successful biometric authentication. The function should take three parameters: `username`, `password`, and `authenticated_biometrically`. If `authenticated_biometrically` is True and the `username` and `password` are valid, return a string indicating a successful login. If `authenticated_biometrically` is False or the `username` and `password` are invalid, return a string indicating an unsuccessful login.
"""

def validate_login(username, password, authenticated_biometrically):
    """
    Validates user login credentials after successful biometric authentication.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.
        authenticated_biometrically (bool): Whether the user has been authenticated biometrically.

    Returns:
        str: A message indicating whether the login was successful or not.
    """

    # Assuming we have a list of valid usernames and passwords for simplicity
    valid_credentials = {"user1": "password1", "user2": "password2"}

    # Check if the user has been authenticated biometrically
    if authenticated_biometrically:
        # Check if the username and password are valid
        if username in valid_credentials and valid_credentials[username] == password:
            # If both conditions are met, return a success message
            return "Login successful"
        else:
            # If the username or password is invalid, return an error message
            return "Invalid username or password"
    else:
        # If the user has not been authenticated biometrically, return an error message
        return "Biometric authentication failed"