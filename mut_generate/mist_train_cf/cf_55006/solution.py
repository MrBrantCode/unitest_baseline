"""
QUESTION:
Write a function `parseTernary(expression)` that takes a string `expression` of length up to 10000 characters, representing an arbitrarily nested ternary expression, and returns the outcome of the expression as a string. The expression will only include digits `0-9`, `?`, `:`, `T` and `F`, where `T` and `F` denote True and False respectively. The condition will always be either `T` or `F`, and the expression's outcome will always be a digit `0-9`, `T` or `F`. The conditional expressions group from right to left.
"""

def entrance(expression):
    stack = []
    for char in reversed(expression):
        if stack and stack[-1] == '?': 
            stack.pop() 
            first = stack.pop()
            stack.pop() 
            second = stack.pop()
            stack.append(first if char == 'T' else second)
        else:
            stack.append(char)
    return stack[0]