"""
QUESTION:
Write a function `minAddToMakeValid(S)` that takes a string `S` consisting only of `(`, `)`, `[`, and `]` characters and returns the minimum number of parentheses or square brackets that must be added to make the resulting string valid. The string is valid if it is empty or can be written as `AB` (`A` concatenated with `B`), `(A)`, or `[A]`, where `A` and `B` are valid strings. The length of `S` is guaranteed to be less than or equal to 1000.
"""

def minAddToMakeValid(S):
    stack = []
    for char in S:
        if char in '([' :
            stack.append(char)
        else:
            if stack and ((stack[-1]=='(' and char==')') or (stack[-1]=='[' and char==']')):
                stack.pop()
            else:
                stack.append(char)
    return len(stack)