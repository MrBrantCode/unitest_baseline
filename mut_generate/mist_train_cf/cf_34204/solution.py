"""
QUESTION:
Create a function named `validate_reset_password` that takes three parameters: `reset_key`, `password1`, and `password2`, all of which are strings. The function should return a tuple containing a boolean `valid` and a string `message`. The function should check that `reset_key` is not empty and that `password1` and `password2` match exactly. If these conditions are met, return `True` and the message "Password reset successful." Otherwise, return `False` and a specific error message.
"""

def validate_reset_password(reset_key, password1, password2):
    if not reset_key:
        return False, "Reset key cannot be empty."

    if password1 != password2:
        return False, "Passwords do not match."

    return True, "Password reset successful."