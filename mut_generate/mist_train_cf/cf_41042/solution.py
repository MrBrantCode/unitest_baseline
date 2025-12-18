"""
QUESTION:
Create a function `authenticate_user` that takes in a `username` and `password` as input. The function should use a `TaskService` object to find a user by their `username` and return the corresponding result based on the following rules: 

- If the `username` is not found in the system, return the string "User not found".
- If the `username` is found but the `password` is incorrect, return the string "Incorrect password".
- If both the `username` and `password` are correct, return the authenticated `User` object. 

Assume that the `TaskService` class has a method `find_user_by_username` which takes a `username` as input and returns a `User` object if found, or `None` if not found, and that the `User` class has attributes `username` and `password` representing the user's credentials.
"""

def authenticate_user(username, password, task_service):
    """
    Authenticates a user by checking the username and password.

    Args:
    username (str): The username of the user.
    password (str): The password of the user.
    task_service: An instance of TaskService.

    Returns:
    User or str: The authenticated User object if credentials are correct, 
                 "User not found" if the username is not found, 
                 "Incorrect password" if the password is incorrect.
    """
    user = task_service.find_user_by_username(username)
    
    if user is None:
        return "User not found"
    elif user.password != password:
        return "Incorrect password"
    else:
        return user