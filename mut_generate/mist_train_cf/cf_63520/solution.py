"""
QUESTION:
Write a function named `power_set` that takes a list of numbers as input and returns the power set of the given list. The power set of a set is the set of all subsets of that set, including the empty set and the set itself. Each subset can be represented as a list, and the order of elements in the subsets does not matter. The output should be a list of lists, where each sublist is a subset of the input list.
"""

def power_set(nums):
    result = [[]]
    for num in nums:
        result += [curr + [num] for curr in result]
    return result