"""
QUESTION:
Given an array (ints) of n integers, find three integers in arr such that the sum is closest to a given number (num), target.

Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

Example:

Note: your solution should not modify the input array.
"""

from itertools import combinations

def find_closest_sum_of_three(ints, target):
    # Generate all combinations of three integers from the input list
    three_combinations = combinations(ints, 3)
    
    # Find the combination with the sum closest to the target
    closest_combination = min(three_combinations, key=lambda a: abs(target - sum(a)))
    
    # Return the sum of the closest combination
    return sum(closest_combination)