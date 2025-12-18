"""
QUESTION:
Create a Python function called `is_parentheses_balanced` that checks whether the parentheses in a given mathematical expression are balanced. The function should take a string as input and return True if the parentheses are balanced and False otherwise. The function should handle different types of parentheses, including round brackets '()', square brackets '[]', and curly brackets '{}'.
"""

def is_parentheses_balanced(string):
    stack = []
    parentheses = {'(': ')', '[': ']', '{': '}'}

    for char in string:
        if char in parentheses.keys():
            stack.append(char)
        elif char in parentheses.values():
            if len(stack) == 0 or parentheses[stack.pop()] != char:
                return False
    return len(stack) == 0