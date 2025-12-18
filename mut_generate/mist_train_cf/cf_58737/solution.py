"""
QUESTION:
Given a column number `columnNumber` where 1 <= columnNumber <= 2^31 - 1, create a function `convertToTitle` that converts the integer to its corresponding Excel sheet column title, where A = 1, B = 2, C = 3, ..., Z = 26, AA = 27, AB = 28, and so on.
"""

def convertToTitle(columnNumber):
    result = ''
    while columnNumber > 0:
        columnNumber -= 1
        digit = columnNumber % 26
        result = chr(digit + ord('A')) + result
        columnNumber //= 26
    return result