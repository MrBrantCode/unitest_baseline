"""
QUESTION:
Write a function `compute_max_depth(nums)` that computes the maximum depth of a binary tree represented as a list of numbers where the index of each node's left child is `i*2 + 1` and the index of its right child is `i*2 + 2`. The list may contain invalid inputs such as strings or negative integers. If an invalid input is found, return an error message in the format "Invalid input: '{invalid_input}' is not a valid number."
"""

def compute_max_depth(nums, i=0):
    # Base case: if the index is out of range, return 0
    if i >= len(nums) or nums[i] is None:
        return 0

    # Check if the current node is a valid number
    if not isinstance(nums[i], int) or nums[i] < 0:
        return f"Invalid input: '{nums[i]}' is not a valid number."

    # Compute the maximum depth of the left and right subtrees recursively
    left_depth = compute_max_depth(nums, 2 * i + 1)
    right_depth = compute_max_depth(nums, 2 * i + 2)

    # Return the maximum depth of the tree
    return max(left_depth, right_depth) + 1