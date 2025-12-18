"""
QUESTION:
Write a function named `count_occurrences` that takes a string `string` and a character `char` as input. The function should return the number of occurrences of `char` in `string`, ignoring any occurrences within parentheses and curly brackets. The function should be case-sensitive and consider only exact matches.
"""

def count_occurrences(string, char):
    count = 0
    stack = []
    for c in string:
        if c == '(' or c == '{':
            stack.append(c)
        elif c == ')' or c == '}':
            if stack:
                stack.pop()
        elif not stack and c == char:
            count += 1
    return count