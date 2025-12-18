"""
QUESTION:
Write a function named `is_palindrome` that determines whether a given alphanumeric string is a palindrome, ignoring non-alphanumeric characters and case sensitivity. The function should only use basic string and list operations, and not rely on built-in string manipulation functions or libraries. The input string is guaranteed to be non-empty.
"""

def is_palindrome(string):
    # Step 1: Remove special characters and whitespace
    clean_string = ""
    for char in string:
        if char.isalnum():
            clean_string += char
    
    # Step 2: Convert to lowercase
    clean_string = clean_string.lower()
    
    # Step 3: Push each character onto a stack
    stack = []
    for char in clean_string:
        stack.append(char)
    
    # Step 4: Pop each character from the stack and compare with original string
    for char in clean_string:
        if stack.pop() != char:
            return False
    
    # Step 5: If all characters match, return True
    return True