"""
QUESTION:
Write a function `find_smallest_positive_number` that takes a list of integers `nums` as input and returns the smallest positive number that is not present in `nums`. The function must have a time complexity of O(n), where n is the number of elements in `nums`.
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