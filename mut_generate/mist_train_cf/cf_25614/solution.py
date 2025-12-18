"""
QUESTION:
Write a function named `sum_divisible_numbers` that takes an array of integers as input, calculates the sum of all numbers in the array that have at least one divisor in the array, and returns the sum. The function should run in O(N) time complexity.
"""

def sum_divisible_numbers(nums):
    total_sum = 0
    for num in nums:
        for other_num in nums:
            if num != other_num and num % other_num == 0:
                total_sum += num
                break
    return total_sum