"""
QUESTION:
Given a valid parentheses string `S` of length at most 10000, where each character is either `(` or `)`, write a function `countPrimitive` that returns the count of primitive valid parentheses strings in the primitive decomposition of `S`. A valid parentheses string is primitive if it is nonempty and cannot be split into two nonempty valid parentheses strings.
"""

def countPrimitive(S):
    stack = []
    count = 0
    for ch in S:
        if ch == '(':
            stack.append(ch)
        else:
            if stack[-1] == '(':
                if len(stack) == 1:
                    count += 1
                stack.pop()
            else:
                while stack[-1] != '(':
                    stack.pop()
                stack.pop()
    return count