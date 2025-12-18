"""
QUESTION:
Create a function named `check_file_access` that takes two parameters, `username` and `file_uri`, and returns a boolean value indicating whether the user is authorized to view the file. Implement the file access control logic based on the following restrictions: 
- If the `username` is "admin", return `True`.
- If the `username` is "iago", return `False`.
- For other usernames, return `True` by default.
"""

def check_file_access(username, file_uri):
    if username == "admin":
        return True  # Admin has access to all files
    elif username == "iago":
        return False  # User 'iago' is not authorized to view any files
    else:
        # Implement additional access control logic based on the file URI and user's role
        return True  # Default to allowing access for other users