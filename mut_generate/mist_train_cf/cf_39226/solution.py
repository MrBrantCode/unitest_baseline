"""
QUESTION:
Create a function `valid_password(password)` that takes an integer `password` as input. The function should return `True` if the password is a six-digit number with at least two adjacent digits that are the same and its digits never decrease from left to right, and `False` otherwise.
"""

def valid_password(password):
    password_str = str(password)
    
    # Check if it is a six-digit number
    if len(password_str) != 6:
        return False
    
    # Check for adjacent digits and non-decreasing order
    has_adjacent = False
    for i in range(5):
        if password_str[i] == password_str[i+1]:
            has_adjacent = True
        if int(password_str[i]) > int(password_str[i+1]):
            return False
    
    return has_adjacent