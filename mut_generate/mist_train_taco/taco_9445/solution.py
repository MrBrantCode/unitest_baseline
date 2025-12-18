"""
QUESTION:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:


Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

def letter_combinations(digits: str) -> list[str]:
    def dfs(digits, current, result):
        if not digits:
            result.append(current)
            return
        for c in digit_to_letters[digits[0]]:
            dfs(digits[1:], current + c, result)
    
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    result = []
    dfs(digits, '', result)
    return result