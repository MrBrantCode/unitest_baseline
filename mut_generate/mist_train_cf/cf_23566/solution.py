"""
QUESTION:
Write a function `largest_number` that takes a list of integers as input. The function should return a list of the largest number from the input list, where each subsequent number is larger than the previous one. In other words, the function should filter out the non-increasing numbers from the input list.
"""

def largest_number(nums):
    largest = []
    for num in nums:
        if len(largest) == 0 or num > largest[-1]:
            largest.append(num)
    return largest