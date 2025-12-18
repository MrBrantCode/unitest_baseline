"""
QUESTION:
Create a function named `countUpperCase` that takes a string as input and returns the number of uppercase letters in the string.
"""

def countUpperCase(string):
    count = 0
    for c in string:
        if c.isupper():
            count += 1
    return count