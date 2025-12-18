"""
QUESTION:
Given a list of floating point numbers and an integer n, write a function `nth_least_occuring(nums, n)` to identify the nth least occurring number in the list. The function should handle all edge cases including duplicate counts and return None if there is no nth least occurring number.
"""

import collections

def nth_least_occuring(nums, n):
    counter = collections.Counter(nums)
    occurance_count = collections.defaultdict(list)
    
    for num, count in counter.items():
        occurance_count[count].append(num)
    
    for key in sorted(occurance_count.keys()):
        if len(occurance_count[key]) >= n:
            return occurance_count[key][n-1]
        else:
            n -= len(occurance_count[key])
    
    return None