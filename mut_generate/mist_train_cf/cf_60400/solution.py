"""
QUESTION:
Function: `minRemoveToMakeValid(s)`

Given a string `s` containing `'('`, `')'`, lowercase English characters, and digits, remove the minimum number of parentheses so that the resulting string is a valid parentheses string and the number of digits is even. If the number of digits is odd, remove one digit to make it even.

Restrictions:
- The length of `s` is between 1 and 10^5.
- Each character in `s` is either `'('`, `')'`, a lowercase English letter, or a digit.
"""

def minRemoveToMakeValid(s):
    s = list(s)
    stack = []
    digits = 0
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                s[i] = ''
        elif c.isdigit():
            digits += 1

    while stack:
        s[stack.pop()] = ''

    if digits % 2 == 1:
        for i in reversed(range(len(s))):
            if s[i].isdigit():
                s[i] = ''
                digits -= 1
                break

    return ''.join(s)