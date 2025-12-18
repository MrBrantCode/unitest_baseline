"""
QUESTION:
Write a function called `evaluate_string` that takes a string as input and returns `True` if the string contains at least 3 consecutive uppercase letters, and `False` otherwise. The function should iterate through the input string to check for the specified condition.
"""

def evaluate_string(string):
    for i in range(len(string) - 2):
        if string[i:i+3].isupper():
            return True
    return False