"""
QUESTION:
Given an integer `rowIndex`, return the `rowIndexth` (0-indexed) row of the Pascal's triangle, where each element in the row is the result of a bitwise XOR operation with `rowIndex`. The function should use `O(rowIndex)` extra space and should not directly use the formula for Pascal's Triangle, instead using array manipulations.
"""

def getRow(rowIndex):
    row = [1] + [0]*rowIndex
    for i in range(rowIndex):
        row[rowIndex-i] = row[rowIndex-i] + row[rowIndex-i-1]
        
    for i in range(len(row)):
        row[i] = row[i] ^ rowIndex
    return row