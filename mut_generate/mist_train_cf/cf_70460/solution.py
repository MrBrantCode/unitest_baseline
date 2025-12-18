"""
QUESTION:
Create a function named `find_smallest_integer` that takes a list of integers as an argument and returns the smallest positive integer greater than 0 that is not present in the list. The function should start checking from 1 and increment by 1 each time until it finds the smallest missing positive integer.
"""

def find_smallest_integer(nums):
    i = 1
    while True:
        if i not in nums:
            return i
        i += 1