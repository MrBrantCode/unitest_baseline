"""
QUESTION:
Write a function `count_occurrences(string, char)` that takes a string and a character as input and returns the number of occurrences of the character in the string, ignoring any occurrences within parentheses.
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