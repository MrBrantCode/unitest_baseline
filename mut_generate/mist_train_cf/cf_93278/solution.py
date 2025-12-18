"""
QUESTION:
Write a function named `calculate_sum_except_self` that takes an array of integers as input and returns an array of the same size. Each element in the output array should be equal to the sum of all the elements in the input array except itself.
"""

def calculate_sum_except_self(nums):
    total_sum = sum(nums)
    result = []
    for num in nums:
        result.append(total_sum - num)
    return result