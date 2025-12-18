"""
QUESTION:
Given a positive integer N, write a function `count_distinct_values(N)` that calculates the number of distinct values that can be inserted in a balanced binary tree containing N nodes. The function should return the maximum number of distinct values that can be inserted. The time complexity of the solution should be better than O(N^2), where N is the number of nodes in the tree.
"""

import math

def count_distinct_values(N):
    height = int(math.log2(N + 1) - 1)
    nodes = 2 ** (height + 1) - 1
    return nodes