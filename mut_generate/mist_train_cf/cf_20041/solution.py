"""
QUESTION:
Write a function named `sum_odd_numbers` that takes a list of integers as a parameter. The function should return the sum of all positive odd numbers in the list, ignoring non-positive numbers and even numbers. The function must achieve this in linear time complexity O(n) and constant space complexity O(1).
"""

def sum_odd_numbers(nums):
    total = 0
    for num in nums:
        if num > 0 and num % 2 != 0:
            total += num
    return total