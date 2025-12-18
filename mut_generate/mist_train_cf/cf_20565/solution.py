"""
QUESTION:
Write a function `transitive_closure_less_than` that takes a list of distinct integers as input and returns the transitive closure of the binary relation "less than or equal to" on the set of integers. The transitive closure consists of all pairs (a, b) such that there is a sequence of elements a1, a2, ..., an where a = a1, b = an, and for each i, ai ≤ ai+1. The function should return a set of tuples representing the transitive closure.
"""

def transitive_closure_less_than(nums):
    closure = set()
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] <= nums[j]:
                closure.add((nums[i], nums[j]))
    return closure