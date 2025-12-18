"""
QUESTION:
Write a function named `verify_brackets` that accepts an array of two strings consisting only of open '(' and closed ')' brackets. The function should determine if a valid nested brackets sequence can be formed by concatenating the strings, and return 'Yes' if valid or 'No' if not.
"""

def verify_brackets(arr):
    stack = []
    combined = "".join(arr)
    for bracket in combined:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if len(stack) == 0:
                return 'No'
            else:
                stack.pop()
    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'