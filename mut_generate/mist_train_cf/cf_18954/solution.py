"""
QUESTION:
Write a function named `is_palindrome` that takes a string as input, determines whether it is a palindrome using a stack data structure, and returns a boolean value indicating whether the string is a palindrome or not. The function should be case-insensitive and ignore special characters and whitespace.
"""

def is_palindrome(s):
    # Step 1: Remove special characters and whitespace
    s = ''.join(e for e in s if e.isalnum())
    # Step 2: Convert to lowercase
    s = s.lower()
    
    # Step 3: Push each character onto a stack
    stack = []
    for char in s:
        stack.append(char)
    
    # Step 4: Pop each character from the stack and compare with original string
    for char in s:
        if stack.pop() != char:
            return False
    
    return True