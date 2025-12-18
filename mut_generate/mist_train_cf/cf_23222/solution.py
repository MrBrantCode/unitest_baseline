"""
QUESTION:
Write a function called `remove_element` that takes an array of integers and an integer to be removed as input. The function should remove all occurrences of the given integer from the array and return the number of times the integer was removed.
"""

def remove_element(nums, val):
    count = 0
    while val in nums:
        nums.remove(val)
        count += 1
    return count