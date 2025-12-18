"""
QUESTION:
Write a function `count_char_in_parentheses` that takes an input string and a character as input. The function should count the occurrences of the character in the input string only if it is surrounded by a pair of non-nested parentheses.
"""

def count_char_in_parentheses(input_string, char):
    count = 0
    stack = []
    for c in input_string:
        if c == '(':
            stack.append(c)
        elif c == ')' and stack:
            stack.pop()
        elif c == char and len(stack) == 1:
            count += 1
    return count