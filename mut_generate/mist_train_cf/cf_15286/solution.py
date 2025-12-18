"""
QUESTION:
Write a function named `powerset(nums)` that takes a list of integers as input, which may contain duplicate elements. The function should return the powerset of the input list in lexicographical order, without any duplicate subsets.
"""

def subsets(nums):
    nums.sort()  # Sort the list to ensure lexicographical order
    subsets = [[]]  # Initialize the powerset with an empty subset

    for num in nums:
        # Generate new subsets by adding the current number to existing subsets
        new_subsets = [subset + [num] for subset in subsets]

        # Avoid adding duplicate subsets
        for subset in new_subsets:
            if subset not in subsets:
                subsets.append(subset)

    return subsets