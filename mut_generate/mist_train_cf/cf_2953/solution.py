"""
QUESTION:
Write a single-line Python function named `helloWorld` that takes a user input string, checks if it is alphanumeric and contains at least one special character, prints the input string in uppercase if valid, and then prints "Hello World". If the input is invalid, it prints "Invalid input".
"""

def helloWorld(s):
    return s.upper() + " Hello World" if not s.isalpha() and any(not c.isalnum() for c in s) else "Invalid input"