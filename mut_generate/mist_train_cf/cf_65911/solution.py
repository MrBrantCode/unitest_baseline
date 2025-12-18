"""
QUESTION:
Write a function named `linear_search` that takes an array and a target value as input and returns the index of the target value if it is present in the array, otherwise return `None`. The input array is not guaranteed to be sorted. Analyze and explain the computational complexity of this function in terms of time and space complexity. If possible, suggest an alternative algorithm with lower computational complexity and discuss the trade-offs.
"""

def linear_search(array, target):
    for index, value in enumerate(array):
        if value == target:
            return index
    return None