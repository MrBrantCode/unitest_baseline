"""
QUESTION:
Implement the `get_aligned_body` method, which takes a string `formula` as input and returns a modified version of the formula with aligned body elements. The method should align the elements and their corresponding subscripts within the parentheses based on the opening parenthesis, adding spaces as necessary. The input `formula` represents a chemical formula where the body elements are enclosed in parentheses.
"""

def get_aligned_body(formula: str) -> str:
    stack = []
    result = ""
    for char in formula:
        if char == '(':
            if stack:
                result += ' ' * (len(stack) - 1)
            stack.append('(')
            result += char
        elif char == ')':
            stack.pop()
            result += char
        else:
            result += char
    return result