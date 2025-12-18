"""
QUESTION:
Write a function `count_max(matrix)` that takes a 2D array of numerical values as input and returns the number of times the maximum value appears in the array. The function should have a time complexity of O(n^2), where n is the length of the longest row in the 2D array, and should use constant space complexity, without creating any additional data structures.
"""

def count_max(matrix):
    max_val = float('-inf')
    count = 0

    for row in matrix:
        for val in row:
            if val > max_val:
                max_val = val
                count = 1
            elif val == max_val:
                count += 1

    return count