"""
QUESTION:
Write a function called `reverse_string` that takes a string `s` as input and returns the reversed string. The function should not use slicing or any built-in functions. The goal is to optimize for both time and space complexity.
"""

def reverse_string(s):
    stack = []
    for ch in s:
        stack.append(ch)

    result = ''
    while stack:
        result += stack.pop()
    
    return result