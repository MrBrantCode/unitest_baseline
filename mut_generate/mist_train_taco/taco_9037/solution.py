"""
QUESTION:
Please write a function that sums a list, but ignores any duplicate items in the list.

For instance, for the list [3, 4, 3, 6] , the function should return 10.
"""

from collections import Counter

def sum_no_duplicates(nums):
    # Count the occurrences of each number in the list
    counts = Counter(nums)
    
    # Sum the numbers that appear exactly once
    return sum(num for num, count in counts.items() if count == 1)