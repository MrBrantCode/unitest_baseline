"""
QUESTION:
Write a function `find_max_subarray_sum` that takes a two-dimensional array of integers as input and returns a list of maximum sums of any subarray within each row. The function should handle rows with all negative values, all positive values, and mixed values. It should also handle empty arrays and rows, returning an empty list in such cases. The function should have a time complexity of O(n), where n is the total number of elements in the array.
"""

def find_max_subarray_sum(A):
    if not A or not any(A):
        return []

    max_sums = []
    for row in A:
        if all(num < 0 for num in row):
            max_sums.append(0)
        elif all(num >= 0 for num in row):
            max_sums.append(sum(row))
        else:
            max_sum = float('-inf')
            current_sum = 0
            for num in row:
                current_sum = max(num, current_sum + num)
                max_sum = max(max_sum, current_sum)
            max_sums.append(max_sum)

    return max_sums