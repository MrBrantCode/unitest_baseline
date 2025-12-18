"""
QUESTION:
Write a function `convertToZigzag` that takes in a string `s` and an integer `nRows` and returns the string in zigzag pattern, where the zigzag pattern is formed by writing the characters of the string in a zigzag pattern and then reading them out row by row. The function must handle the following conditions: the input string contains only uppercase or lowercase letters (a-z, A-Z), the input string may be empty, and the value of nRows is greater than 1. If nRows is 1 or nRows is greater than or equal to the length of the string, return the original string.
"""

def convertToZigzag(s: str, nRows: int) -> str:
    if nRows == 1 or nRows >= len(s):
        return s

    res = [''] * nRows
    index, step = 0, 1

    for char in s:
        res[index] += char
        if index == 0:
            step = 1
        elif index == nRows - 1:
            step = -1
        index += step

    return ''.join(res)