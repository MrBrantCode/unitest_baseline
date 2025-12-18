"""
QUESTION:
Write a function `find_pair` that takes a list of positive fractions `lst` and a target value `target` as input, and returns the first pair of numbers in the list that multiply to the target value. If no such pair exists, return 'No pair found'.
"""

def find_pair(lst, target):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] * lst[j] == target:
                return [lst[i], lst[j]]
    return 'No pair found'