"""
QUESTION:
Write a function `balancedStringSplit` that takes a string `s` consisting of only 'L' and 'R' characters and returns the maximum number of balanced strings that can be formed by splitting `s`, where a balanced string has an equal number of 'L' and 'R' characters.
"""

def balancedStringSplit(s: str) -> int:
    count = 0
    balance = 0
    for char in s:
        if char == 'L':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            count += 1
    return count