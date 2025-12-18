"""
QUESTION:
Write a function named `repeating_unit` that takes a string as input and returns the smallest repeating unit of that string. The function should find the shortest substring that, when repeated, equals the original string. If no repeating unit is found, the function should return the original string.
"""

def repeating_unit(s):
    length = len(s)
    for i in range(1, length//2 + 1):
        if length % i == 0:
            unit = s[:i]
            if unit*(length//i) == s:
                return unit
    return s