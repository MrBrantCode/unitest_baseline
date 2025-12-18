"""
QUESTION:
Write a function `caseCombinations` that takes a string `S` consisting of digits and lowercase letters as input. The function should return a list of all possible combinations of `S` where each lowercase letter can be either in its original case or uppercase, while digits remain unchanged.
"""

from typing import List

def caseCombinations(S: str) -> List[str]:
    def backtrack(index, current):
        if index == len(S):
            result.append(current)
            return
        if S[index].isalpha():
            backtrack(index + 1, current + S[index].lower())
            backtrack(index + 1, current + S[index].upper())
        else:
            backtrack(index + 1, current + S[index])

    result = []
    backtrack(0, "")
    return result