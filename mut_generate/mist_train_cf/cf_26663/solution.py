"""
QUESTION:
Create a function named `generateParenthesis` that generates all combinations of well-formed parentheses given a positive integer `n`. The function should return a list of all well-formed parentheses combinations of length `2n`. The combinations should have every open parenthesis `(` matched with a corresponding closing parenthesis `)`, and the parentheses should be properly nested.
"""

from typing import List

def generateParenthesis(n: int) -> List[str]:
    def backtrack(s, left, right, res):
        if len(s) == 2 * n:
            res.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right, res)
        if right < left:
            backtrack(s + ')', left, right + 1, res)

    result = []
    backtrack('', 0, 0, result)
    return result