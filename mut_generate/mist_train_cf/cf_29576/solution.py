"""
QUESTION:
Implement the `convert` function that takes a string `s` and an integer `numRows` as input and returns the string in a zigzag pattern based on the number of rows specified. The function should handle the cases where `s` is an empty string or `numRows` is 1 or greater than or equal to the length of `s`. The output should be the concatenation of characters in each row of the zigzag pattern formed by moving characters up and down based on the number of rows specified.
"""

def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    index, step = 0, 1

    for char in s:
        rows[index] += char
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step

    return ''.join(rows)