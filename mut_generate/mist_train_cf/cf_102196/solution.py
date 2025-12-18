"""
QUESTION:
Find the smallest positive integer missing from a given list of integers.

Function name: `find_smallest_positive_number(nums)`

The function should take a list of integers as input and return the smallest positive integer that is not present in the list.

The solution must have a time complexity of O(n), where n is the number of elements in the input list.
"""

def find_smallest_positive_number(nums):
    num_set = set()
    for num in nums:
        if num > 0:
            num_set.add(num)
    
    smallest_positive = 1
    while smallest_positive in num_set:
        smallest_positive += 1
    
    return smallest_positive