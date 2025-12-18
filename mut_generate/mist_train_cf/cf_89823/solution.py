"""
QUESTION:
Create a function `count_max_occurrences` that takes a 2D array of numerical values as input. The function should return the number of times the maximum value appears in the array. The function must have a time complexity of O(n^2), where n is the length of the longest row in the array, and use only constant space complexity.
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