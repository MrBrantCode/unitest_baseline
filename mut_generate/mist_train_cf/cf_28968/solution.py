"""
QUESTION:
Given a string of digits from 2-9, write a function `letter_combinations(digits: str)` that returns all possible letter combinations based on the following mapping:
- 2 -> "abc"
- 3 -> "def"
- 4 -> "ghi"
- 5 -> "jkl"
- 6 -> "mno"
- 7 -> "pqrs"
- 8 -> "tuv"
- 9 -> "wxyz"
The input string will not contain any 0 or 1, and the order of the combinations does not matter.
"""

from typing import List

def letter_combinations(digits: str) -> List[str]:
    if not digits:
        return []

    digit_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def backtrack(index, path):
        if index == len(digits):
            combinations.append(''.join(path))
            return
        for letter in digit_map[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    combinations = []
    backtrack(0, [])
    return combinations