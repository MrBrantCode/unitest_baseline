"""
QUESTION:
Create a function `is_palindrome` that determines whether a given string is a palindrome using a stack data structure. The function should be case-insensitive and ignore special characters and whitespace. It should return `True` if the string is a palindrome and `False` otherwise.
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