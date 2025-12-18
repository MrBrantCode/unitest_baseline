"""
QUESTION:
Create a function `greet(name)` that takes a string `name` as input and returns a greeting message. If the `name` contains any special characters or numbers, return an error message. If the `name` is in all uppercase letters, return the greeting in all uppercase letters; otherwise, return the greeting in lowercase. The function should have a time complexity of O(n), where n is the length of the `name`.
"""

def greet(name):
    # Check if the name contains any special characters or numbers
    if not name.isalpha():
        return "Error: Name should only contain alphabetic characters"
    
    # Check if the name is in all uppercase letters
    if name.isupper():
        return "HELLO, " + name + "!"
    
    # Return the greeting with the name
    return "Hello, " + name + "!"