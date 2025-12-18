"""
QUESTION:
Write a function `transitive_closure_less_than` that takes a list of integers as input and returns the transitive closure of the binary relation "less than" on the given set of integers. The function should return a set of tuples, where each tuple represents a pair of numbers in the relation. The function should only include pairs where the first number is strictly less than the second number.
"""

def transitive_closure_less_than(nums):
    closure = set()
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] < nums[j]:
                closure.add((nums[i], nums[j]))
    return closure