"""
QUESTION:
Write a function `solve(matrix)` that receives a two-dimensional array of strings with a maximum of 100 elements and returns the longest valid string. A string is considered valid if it does not contain the symbols '/' and '{'. If there are multiple longest strings, return any of them. The input matrix can have varying sizes.
"""

def solve(matrix):
    """
    This function receives a two-dimensional array, filters invalid words, and finds the longest valid string.
    """
    max_length = 0
    longest_string = ''
    for row in matrix:
        for s in row:
            if '/' not in s and '{' not in s and len(s) > max_length:
                max_length = len(s)
                longest_string = s
    return longest_string