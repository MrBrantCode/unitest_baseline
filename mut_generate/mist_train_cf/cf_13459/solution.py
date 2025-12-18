"""
QUESTION:
Write a function `generate_permutations(nums)` that takes a list of distinct integers `nums` as input and returns a list of all possible permutations of the input list in lexicographic order, without using any built-in functions or libraries for generating permutations.
"""

def entrance(nums):
    # Base case: if the list is empty, return an empty list
    if not nums:
        return []

    # Initialize an empty list to store the permutations
    permutations = []

    # Helper function to generate permutations
    def backtrack(start, end):
        # If we have reached the end of the list, add the current permutation to the list of permutations
        if start == end:
            permutations.append(nums[:])

        # For each position after the current one, swap the current position with it and recursively generate permutations
        for i in range(start, end):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1, end)
            nums[start], nums[i] = nums[i], nums[start]  # backtrack by swapping back

    # Call the helper function to generate permutations
    backtrack(0, len(nums))

    # Sort the permutations in lexicographic order
    permutations.sort()

    # Return the list of permutations
    return permutations