"""
QUESTION:
Write a function `longest_sublist_with_sum_greater_than_target` that takes a list of lists and a positive integer target as input. The function should return the longest sublist where the sum of its elements is greater than the target value. If there are multiple sublists with the same maximum length, return any one of them.
"""

def longest_sublist_with_sum_greater_than_target(lists, target):
    longest_sublist = []
    longest_length = 0
    
    for sublist in lists:
        sublist_sum = sum(sublist)
        
        if sublist_sum > target and len(sublist) > longest_length:
            longest_sublist = sublist
            longest_length = len(sublist)
    
    return longest_sublist