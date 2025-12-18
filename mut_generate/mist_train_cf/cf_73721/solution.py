"""
QUESTION:
Write a function named `find_subsets` that takes a list of integers as input and returns all possible subsets of the input list. The function should return an empty subset and the input list itself as subsets, and the order of the subsets does not matter.
"""

def find_subsets(nums):
    subsets = []
    def generate_subsets(index, current):
        subsets.append(list(current))
        for i in range(index, len(nums)):
            current.append(nums[i])
            generate_subsets(i + 1, current)
            current.pop()
    generate_subsets(0, [])
    return subsets