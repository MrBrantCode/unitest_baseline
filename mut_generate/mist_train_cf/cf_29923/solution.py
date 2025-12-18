"""
QUESTION:
Create a function `validate_binary_password(binary_password)` that takes a binary password as input and returns `True` if the password is valid and `False` otherwise. The password is valid if its length is a multiple of 8 and it contains both the substrings "101" and "010".
"""

def validate_binary_password(binary_password):
    if len(binary_password) % 8 != 0:
        return False
    if "101" not in binary_password or "010" not in binary_password:
        return False
    return True