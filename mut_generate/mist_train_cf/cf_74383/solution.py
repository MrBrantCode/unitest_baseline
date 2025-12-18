"""
QUESTION:
Given a valid parentheses string S, count the number of primitive valid parentheses strings in its primitive decomposition and the maximum nested level of parentheses. A primitive valid parentheses string is a nonempty string that cannot be split into two nonempty valid parentheses strings. The maximum nested level is the maximum depth of nested parentheses. 

The function should take a string S as input and return a tuple (count, maxLevel), where count is the number of primitive valid parentheses strings and maxLevel is the maximum nested level of parentheses.

Restrictions:
- S.length <= 10000
- S[i] is either "(" or ")"
- S is a valid parentheses string
"""

def maxPrimitiveAndLevel(S):
    level = 0
    maxLevel = 0
    count = 0
    stack = []
    for i in range(len(S)):
        if S[i] == '(':
            level += 1
            stack.append('(')
            maxLevel = max(maxLevel, level)
        else:
            level -= 1
            stack.pop()
        if not stack:
            # the stack is empty, we've found a primitive string
            count += 1
    return count, maxLevel