"""
QUESTION:
Write a function `match_braces_parens_brackets` that takes a list of two strings containing only parentheses '(', ')', squared brackets '[', ']', and curly braces '{', '}' as input. The function should check if the string concatenation results in a correctly nested and balanced parentheses, brackets, and braces string, where each open symbol must be closed by its respective closing symbol in a correct order. The function should return 'Yes' if a valid string can be formed, else 'No'.
"""

def match_braces_parens_brackets(lst):
    mapping = {'}': '{', ']': '[', ')': '('}
    stack = []
    for s in lst:
        for c in s:
            if c not in mapping:
                stack.append(c)
            elif not stack or stack.pop() != mapping[c]:
                return 'No'
    if stack:
        return 'No'
    return 'Yes'