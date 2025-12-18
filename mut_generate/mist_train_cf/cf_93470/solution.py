"""
QUESTION:
Create a function `evaluate_string` that takes a string as input and returns a boolean value. The function should return `True` if the string contains at least 3 consecutive uppercase letters and `False` otherwise.
"""

def evaluate_string(string):
    for i in range(len(string) - 2):
        if string[i:i+3].isupper():
            return True
    return False