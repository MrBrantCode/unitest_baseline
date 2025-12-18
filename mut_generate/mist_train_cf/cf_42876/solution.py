"""
QUESTION:
Convert the input string `s` into a zigzag pattern when printed in `numRows` rows and return the resulting string. The zigzag pattern is formed by moving characters in a specific manner through the rows. The function should take in a string `s` and an integer `numRows` as input, and return the resulting string after filling the zigzag pattern.

Function name: `convertToZigZag`
Input: string `s` and integer `numRows`
Output: resulting string after filling the zigzag pattern
Restriction: numRows > 0
"""

def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    L = [''] * numRows
    index, step = 0, 1

    for x in s:
        L[index] += x
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step

    return ''.join(L)