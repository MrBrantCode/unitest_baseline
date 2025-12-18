"""
QUESTION:
Implement a function named `count_occurrences` that takes two parameters: a string `string` and a character `char`. The function should return the number of occurrences of `char` in `string`, ignoring any occurrences within parentheses.
"""

def count_occurrences(string, char):
    count = 0
    parenStack = []

    for c in string:
        if c == '(':
            parenStack.append('(')
        elif c == ')':
            parenStack.pop() if parenStack else None
        elif c == char and not parenStack:
            count += 1

    return count