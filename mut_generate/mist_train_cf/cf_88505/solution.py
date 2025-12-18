"""
QUESTION:
Write a function called `count_distinct_values` that calculates how many distinct values can be inserted in a balanced binary tree containing N nodes, where N is a positive integer. The values must be inserted in such a way that the resulting tree remains balanced at all times. The time complexity of your solution should be better than O(N^2), where N is the number of nodes in the tree.
"""

import math

def count_distinct_values(N):
    return (2 ** (int(math.log2(N + 1))) - 1)