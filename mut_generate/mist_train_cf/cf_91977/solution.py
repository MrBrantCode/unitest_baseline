"""
QUESTION:
Create a function named `grant_access` that takes two parameters: `age` (an integer) and `password` (a string). The function should return `True` if access is granted and `False` otherwise. The access is granted if the provided `age` is 18 or above and the `password` matches the predefined password "abc123". If the `age` is below 18, access should be denied regardless of the password.
"""

def grant_access(age, password):
    predefined_password = "abc123"
    
    if age < 18:
        return False
    elif password == predefined_password:
        return True
    else:
        return False