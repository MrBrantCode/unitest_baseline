"""
QUESTION:
Write a function named `permute` that takes a list of numbers as input and returns all possible permutations of the list. The permutations must contain at least one even number, and the even number should be at an odd index position in the permutation.
"""

def permute(nums):
    # Base case: if the list has only one element, return it
    if len(nums) == 1:
        return [nums]

    # Initialize an empty list to store the permutations
    permutations = []

    # Iterate over each number in the input list
    for i in range(len(nums)):
        # Check if the current number is even and its index is odd
        if nums[i] % 2 == 0 and i % 2 == 1:
            # Generate a sub-list by removing the current number
            sub_nums = nums[:i] + nums[i+1:]

            # Recursively generate all permutations of the sub-list
            sub_permutations = permute(sub_nums)

            # Append the current number at the beginning of each sub-permutation
            for p in sub_permutations:
                permutations.append([nums[i]] + p)

    # Return the list of permutations
    return permutations