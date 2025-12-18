"""
QUESTION:
Write a function called `find_avg_difference` that takes a list of two-dimensional arrays of integers as input. For each two-dimensional array, calculate the maximum difference between the smallest and largest element in each sub-array and then find the average of these differences. The function should handle edge cases where sub-arrays could be empty or have only one element, treating the difference as 0 in such cases. The function should also be able to accept more than one array and return the result for each of them separately.
"""

def find_avg_difference(arrays):
    output = []
    for array in arrays:
        if len(array) > 1:
            max_val = max(array)
            min_val = min(array)
            difference = max_val - min_val
            output.append(difference)
        else:
            output.append(0)
    return sum(output) / len(output)