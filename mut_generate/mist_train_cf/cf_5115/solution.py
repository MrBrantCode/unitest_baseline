"""
QUESTION:
Write a function `find_largest_subarray(array, k)` that finds the largest sub-array in a given array with contiguous elements and its sum. The sub-array must have a length of at least 3 and a sum greater than a given threshold `k`. The function should return the sub-array and its sum. If no such sub-array exists, the function should return "No sub-array found".
"""

def find_largest_subarray(array, k):
    max_sum = float('-inf')
    max_start = 0
    max_end = 0

    current_sum = 0
    current_start = 0

    for i in range(len(array)):
        current_sum += array[i]

        if current_sum > max_sum and i - current_start + 1 >= 3 and current_sum > k:
            max_sum = current_sum
            max_start = current_start
            max_end = i

        if current_sum < 0:
            current_sum = 0
            current_start = i + 1

    if max_sum < k or max_end - max_start + 1 < 3:
        return "No sub-array found"

    return array[max_start:max_end+1], max_sum