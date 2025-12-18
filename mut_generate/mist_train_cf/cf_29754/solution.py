"""
QUESTION:
Implement a function named `is_valid_expression` that checks whether a given string expression is properly formatted with parentheses and single quotes. The expression is considered valid if it meets the following conditions:
- It ends with three consecutive closing parentheses `)))`.
- It contains an even number of single quotes `'`.
- The single quotes are properly paired and enclosed within the parentheses.
The function should return a boolean indicating whether the expression is valid or not.
"""

def is_valid_expression(expression: str) -> bool:
    if expression.endswith(")))"):
        quote_count = expression.count("'")
        if quote_count % 2 == 0:
            stack = []
            for char in expression:
                if char == "(":
                    stack.append(char)
                elif char == ")":
                    if not stack:
                        return False
                    stack.pop()
                elif char == "'":
                    if not stack or stack[-1] != "(":
                        return False
            return not stack
    return False