"""
QUESTION:
Write a function `maxDepth(s)` that calculates the maximum nesting depth of parentheses in a given valid parentheses string `s`. The length of `s` is between 1 and 100, and it is composed of digits `0-9` and characters `+`, `-`, `*`, `/`, `(`, and `)`. The input string `s` is guaranteed to be a valid parentheses string (VPS).
"""

def maxDepth(s):
    max_d = d = 0
    for i in s:
        if i == '(':
            d += 1
            max_d = max(max_d, d)
        elif i == ')':
            d -= 1
    return max_d