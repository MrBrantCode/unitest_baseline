"""
QUESTION:
Write a function `count_char_in_parentheses` that takes an input string and a character as arguments. The function should return the number of occurrences of the given character in the input string, but only if the character is surrounded by a pair of non-nested parentheses.
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