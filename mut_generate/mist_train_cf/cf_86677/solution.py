"""
QUESTION:
Write a function `longest_sublist(lst, target)` that takes a list of integers `lst` and a positive integer `target` as input, and returns the longest sublist where the sum of its elements is greater than `target` and the sublist contains at least one odd number.
"""

def longest_sublist(lst, target):
    longest = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j+1]
            if sum(sublist) > target and any(num % 2 != 0 for num in sublist):
                if len(sublist) > len(longest):
                    longest = sublist
    return longest