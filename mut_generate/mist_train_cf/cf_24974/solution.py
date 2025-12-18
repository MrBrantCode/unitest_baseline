"""
QUESTION:
Write a function `optimal_sum(target, numbers)` that determines whether it's possible to get a sum equal to the target from a set of given numbers. The function should take two parameters: `target` (the desired sum) and `numbers` (a list of integers). The function should return `True` if the target sum can be achieved and `False` otherwise.
"""

def optimal_sum(target, numbers):
    if (target == 0): 
        return True
    n = len(numbers) 
    subset = [True] + [False]*target 
  
    for i in range(n): 
        for j in range(target,numbers[i]-1,-1): 
            subset[j] = subset[j] or subset[j-numbers[i]] 
  
    return subset[target]