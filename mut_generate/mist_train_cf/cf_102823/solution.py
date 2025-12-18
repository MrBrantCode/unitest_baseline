"""
QUESTION:
Create a function `divisible_by_2_and_3` that takes a list of integers as input and returns the total sum of all elements in the list that are divisible by both 2 and 3. If no such elements exist, return 0.
"""

def divisible_by_2_and_3(nums):
    total = 0
    for num in nums:
        if num % 2 == 0 and num % 3 == 0:
            total += num
    return total