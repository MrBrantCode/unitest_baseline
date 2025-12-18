"""
QUESTION:
Write a function named `check_parentheses` that takes a string `input_string` of up to 10^6 characters consisting only of '(' and ')' and returns a boolean indicating whether the string's parentheses are balanced, with a time complexity of O(n), where n is the length of the input string. A string of parentheses is considered balanced if every opening parenthesis has a corresponding closing parenthesis and the parentheses are nested correctly.
"""

def check_parentheses(input_string: str) -> bool:
    stack = []
    for char in input_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0