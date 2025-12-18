"""
QUESTION:
Write a function named `count_occurrences` that takes a string and a character as input, and returns the number of occurrences of the character in the string, excluding any occurrences within parentheses and curly brackets. The function should handle nested parentheses and curly brackets correctly.
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