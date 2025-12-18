"""
QUESTION:
Create a function that takes a list of one or more non-negative integers, and arranges them such that they form the largest possible number.

Examples:

`largestArrangement([4, 50, 8, 145])` returns 8504145 (8-50-4-145)

`largestArrangement([4, 40, 7])` returns 7440 (7-4-40)

`largestArrangement([4, 46, 7])` returns 7464 (7-46-4)

`largestArrangement([5, 60, 299, 56])` returns 60565299 (60-56-5-299)

`largestArrangement([5, 2, 1, 9, 50, 56])` returns 95655021 (9-56-5-50-21)
"""

from functools import cmp_to_key

def largest_arrangement(nums):
    # Custom comparator function
    def cmp(a, b):
        return int(f'{b}{a}') - int(f'{a}{b}')
    
    # Sort the list using the custom comparator
    sorted_nums = sorted(nums, key=cmp_to_key(cmp))
    
    # Join the sorted numbers into a single string and convert to integer
    largest_number = int(''.join(map(str, sorted_nums)))
    
    return largest_number