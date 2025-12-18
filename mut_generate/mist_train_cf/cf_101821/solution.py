"""
QUESTION:
Create a function called `check_sum` that takes a string as input and returns "even" or "odd" depending on whether the sum of the Unicode values of each character in the string is even or odd.
"""

def check_sum(s):
    total = sum(ord(char) for char in s)
    if total % 2 == 0:
        return "even"
    else:
        return "odd"