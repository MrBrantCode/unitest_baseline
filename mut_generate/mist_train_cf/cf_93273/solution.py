"""
QUESTION:
Create a function `greet(name)` that takes a string `name` as input. The function should return a greeting string that includes the input name. If the input name is in all uppercase letters, the greeting should also be in all uppercase letters. However, if the input name contains any non-alphabetic characters, the function should return an error message instead of a greeting. The function's time complexity should be O(n), where n is the length of the input name.
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