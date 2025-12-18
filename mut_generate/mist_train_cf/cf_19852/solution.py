"""
QUESTION:
Design a function `greedy_sum_subset` that takes an array of integers `arr` and a target integer `target` as inputs, and returns a subset of `arr` such that the sum of the subset is equal to `target` using a greedy algorithm. If no such subset exists, return an empty list. The function should consider all possible numbers in `arr` and find an optimal subset if it exists.
"""

def greedy_sum_subset(arr, target):
    subset = []
    remaining = target
    
    for num in sorted(arr, reverse=True):
        if num <= remaining:
            subset.append(num)
            remaining -= num
    
    if remaining != 0:
        return []
    
    return subset