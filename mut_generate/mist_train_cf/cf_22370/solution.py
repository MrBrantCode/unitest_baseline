"""
QUESTION:
Implement a function named `function(message)` that takes a string `message` of maximum length 1000 as input and returns its reversed version. The function should handle strings containing special characters, numbers, and uppercase letters, and ignore leading and trailing whitespace characters.
"""

def function(message):
    # Remove leading and trailing whitespace characters
    message = message.strip()
    
    # Reverse the string
    reversed_message = message[::-1]
    
    return reversed_message