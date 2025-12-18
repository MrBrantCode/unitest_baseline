"""
QUESTION:
Create a function called `authenticate_user` that takes in two parameters, `username` and `password`, and returns `True` if the user's credentials are valid, and `False` otherwise. Assume that the database connection and user table have already been created, and the function has access to the stored user credentials.
"""

def authenticate_user(username, password):
    # query the database to check if the user credentials are valid
    # return True if the credentials are valid, False otherwise
    # For the purpose of this example, assume we have a dictionary of valid credentials
    valid_credentials = {"user1": "password1", "user2": "password2"}
    return username in valid_credentials and valid_credentials[username] == password