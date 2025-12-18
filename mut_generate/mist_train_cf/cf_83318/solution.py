"""
QUESTION:
Create a function `asterisk_string(n)` that generates a string of asterisk characters with a specified length `n`. The function should take an integer `n` as input, where `n` is between 0 and 1,000,000 (inclusive), and return a string of `n` asterisks. If `n` is not an integer or is outside the specified range, the function should return an error message.
"""

def asterisk_string(n):
    # validate input type
    if not isinstance(n, int):
        return "Invalid input! Input must be integer."

    # validate input range
    if n < 0 or n > 10**6:
        return "Invalid input! Input must be between 0 and 1,000,000."

    # populate string with n asterisks
    return "*" * n