"""
QUESTION:
Given an array of integers, write a function `prod_signs` that calculates the sum of the magnitudes of distinct non-zero integers multiplied by their respective signs (1 for positive, -1 for negative). The function should disregard duplicates and return `None` if the array is empty or contains a zero.
"""

def prod_signs(arr):
    if len(arr) == 0:
        return None

    result = 0
    distinct_nums = set()
    for num in arr:
        if num == 0:
            return None
        if num not in distinct_nums:
            result += abs(num) * (1 if num > 0 else -1)
            distinct_nums.add(num)

    return result