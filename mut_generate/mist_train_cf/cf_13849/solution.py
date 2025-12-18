"""
QUESTION:
Implement a function `check_balanced_parentheses` that takes a string as input and returns a boolean indicating whether the parentheses in the string are balanced. The string may contain characters other than parentheses, and the function should consider the following types of parentheses: round brackets '(', ')', curly brackets '{', '}', and square brackets '[', ']'. The function should return True if the parentheses are balanced and False otherwise.
"""

def check_balanced_parentheses(string):
    stack = []
    opening_parentheses = ['(', '{', '[']
    closing_parentheses = [')', '}', ']']
    for char in string:
        if char in opening_parentheses:
            stack.append(char)
        elif char in closing_parentheses:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if opening_parentheses.index(top) != closing_parentheses.index(char):
                return False
    return len(stack) == 0