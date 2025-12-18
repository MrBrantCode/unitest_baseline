"""
QUESTION:
Design a function `greedy_sum_subset` that takes an array of integers `arr` and a target integer `target` as input, and returns the subset of numbers in `arr` that sums up to `target` using a greedy algorithm. The function should include the largest possible numbers in the subset without exceeding the target sum. The array can be modified in place.
"""

def greedy_sum_subset(arr, target):
    subset = []
    arr.sort(reverse=True)
    
    for num in arr:
        if num <= target and sum(subset) + num <= target:
            subset.append(num)
            target -= num
    
    return subset