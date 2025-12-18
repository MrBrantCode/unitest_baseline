"""
QUESTION:
Write a function `lowest_even_numbers` that takes a list of integers `nums` and an integer `k` as input, and returns the `k` lowest even numbers in the list. The function should use an efficient sorting algorithm and filter the list to only include even numbers.
"""

def lowest_even_numbers(nums, k):
    evens = sorted([num for num in nums if num % 2 == 0])
    return evens[:k]