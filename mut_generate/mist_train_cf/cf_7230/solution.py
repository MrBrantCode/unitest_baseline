"""
QUESTION:
Write a function called `count_max_occurrences` that takes a 2D array of numerical values as input, including negative numbers and duplicates, and returns the number of times the maximum value appears. The function should have a time complexity of O(n^2), where n is the length of the longest row in the 2D array, and should use only constant space complexity, without creating any additional data structures.
"""

def count_max_occurrences(arr):
    max_val = float('-inf')
    max_count = 0

    for row in arr:
        for num in row:
            if num > max_val:
                max_val = num
                max_count = 1
            elif num == max_val:
                max_count += 1

    return max_count