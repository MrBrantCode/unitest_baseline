"""
QUESTION:
Implement the `isValid` function in the `Solution` class to determine if a given string `s` containing only '(', ')', '{', '}', '[' and ']' is valid. A string is considered valid if open brackets are closed by the same type of brackets and in the correct order. The function should return a boolean value indicating whether the input string is valid or not. 

The function takes a single parameter `s`, a string, and returns a boolean value.
"""

def isValid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack