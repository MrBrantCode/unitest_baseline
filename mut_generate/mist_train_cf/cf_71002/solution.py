"""
QUESTION:
Implement the function `pluck(tree_branch_values, condition_function, minimum_limit)` that finds the smallest node value in `tree_branch_values` that satisfies the given `condition_function` and reaches or exceeds `minimum_limit`. The function should return a list `[smallest_value, index]` if such a value exists, and an empty list otherwise. Note that if multiple nodes share the minimum value, the one with the smaller index should be favored. The length of `tree_branch_values` should be between 1 and 10000, each node value should be non-negative, and `minimum_limit` should be between -1e7 and 1e7.
"""

def pluck(tree_branch_values, condition_function, minimum_limit):
    """
    The function finds the smallest node value that satisfies a specific condition function and reaches or exceeds a given minimum limit.
    If such a value exists, the function returns it and its index as a list [smallest_value, index].
    If it does not exist, the function returns an empty list.
    """

    # Check if the input array is empty
    if not tree_branch_values:
        return []
        
    # Initialize the minimum satisfying value and its index as None
    min_val, min_index = None, None
    
    # Iterate over the array and the condition function
    for i, val in enumerate(tree_branch_values):
        # Check if the value meets the condition and exceeds or equals the minimum limit 
        if condition_function(val) and val >= minimum_limit:
            # Update the minimum satisfying value and its index if it hasn't been set or a smaller suitable value has been found
            if min_val is None or val < min_val:
                min_val, min_index = val, i

    # If a satisfying value has been found, return it and its index as a list
    return [min_val, min_index] if min_val is not None else []