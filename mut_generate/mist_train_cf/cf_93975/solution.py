"""
QUESTION:
Write a function `find_longest_sublist(lst, target)` that takes a list of lists `lst` and a positive integer `target` as input. The function should return the longest sublist from `lst` where the sum of its elements is greater than the target value. If multiple sublists have the same maximum length and their sums are greater than the target, return any one of them.
"""

def find_longest_sublist(lst, target):
    longest_sublist = []
    longest_length = 0
    
    for sublist in lst:
        if sum(sublist) > target and len(sublist) > longest_length:
            longest_sublist = sublist
            longest_length = len(sublist)
    
    return longest_sublist