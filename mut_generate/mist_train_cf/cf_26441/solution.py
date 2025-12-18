"""
QUESTION:
You are given a string `s` consisting of parentheses, where the length of `s` is within the range [1, 1000]. Write a function `removeOuterParentheses` to remove the outermost parentheses of every primitive string in the input string `s` and return the resulting string. A primitive string is a non-empty string that is recursively derived from some primitive string `t` by adding `t` to the left or right of `t`, with an empty string being considered primitive, and a string `x` being considered primitive if `(x)` is primitive.
"""

def removeOuterParentheses(s: str) -> str:
    result = []
    opened = 0
    for char in s:
        if char == '(':
            if opened > 0:
                result.append(char)
            opened += 1
        else:
            opened -= 1
            if opened > 0:
                result.append(char)
    return ''.join(result)