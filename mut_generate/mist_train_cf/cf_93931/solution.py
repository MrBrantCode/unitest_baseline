"""
QUESTION:
Write a function `find_odd_number` that takes a list of integers as input and returns the first number that appears an odd number of times. If no number appears an odd number of times, return -1. The list can contain negative numbers and may not be sorted.
"""

def find_odd_number(arr):
    count_dict = {}
    
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    for num, count in count_dict.items():
        if count % 2 != 0:
            return num
    
    return -1