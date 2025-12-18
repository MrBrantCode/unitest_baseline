"""
QUESTION:
Create a function `reverseParentheses(s)` that takes a string `s` composed of lower case English alphabets and balanced parentheses as input, and returns a string with the sequences within each pair of corresponding parentheses inverted, starting from the most internal one, and without any brackets. The input string `s` has a length between 0 and 2000, inclusive.
"""

def reverseParentheses(s):
    stack = ['']
    for c in s:
        if c == '(':
            stack.append('')
        elif c == ')':
            add = stack.pop()[::-1]
            stack[-1] += add
        else:
            stack[-1] += c
    return stack[0]