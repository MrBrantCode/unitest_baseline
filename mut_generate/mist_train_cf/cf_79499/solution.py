"""
QUESTION:
Write a function `optimalPluck` that takes an array of non-negative integers `arr` and a boolean function `cond_fn` as input. The function should return a list containing the smallest node value that fulfills the condition, its index in the array, and its depth in the min-heap tree, where the tree depth is calculated as the floor of the base 2 logarithm of the node's index plus 2. If multiple nodes meet the condition, select the one with the smallest index. If the array is empty or no values meet the condition, return an empty list. The function should have a time complexity of O(n), where n is the length of the array.
"""

from math import log2, floor

def optimalPluck(arr, cond_fn):
    min_info = [float('inf'), float('inf'), float('inf')]
    
    for i, node in enumerate(arr):
        if cond_fn(node):
            d = floor(log2(i+2)) 
            if node < min_info[0] or (node==min_info[0] and d<min_info[2]) or (node==min_info[0] and d==min_info[2] and i<min_info[1]):
                min_info = [node, i, d]

    return min_info if min_info[0] != float('inf') else []