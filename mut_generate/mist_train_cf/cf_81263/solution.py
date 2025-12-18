"""
QUESTION:
Write a function called `organize_nums` that takes a list of integers as input and returns a list containing two lists. The first inner list should contain all even numbers from the input list, and the second inner list should contain all odd numbers.
"""

def organize_nums(nums):
    even_nums = []
    odd_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)
    return [even_nums, odd_nums]