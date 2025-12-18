"""
QUESTION:
Write a function `find_largest_sum(array: list) -> int` that finds the maximum sum of a subarray within the given array where no two adjacent elements have consecutive values. The function should return the maximum sum. 

Restrictions: The function should only consider subarrays with a length of at least 2.
"""

def find_largest_sum(array: list) -> int:
    largest_sum = 0
    for i in range(len(array)):
        for j in range(i + 2, len(array)):
            if all(array[k] + 1 != array[k + 1] for k in range(i, j)):
                subarray_sum = sum(array[i:j+1])
                if subarray_sum > largest_sum:
                    largest_sum = subarray_sum
    return largest_sum