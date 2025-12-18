"""
QUESTION:
Write the function `pluck_dict(arr, cond_fn_dict, thresh)` that takes a non-negative integer array `arr`, a dictionary of condition functions `cond_fn_dict`, and a threshold `thresh` as input. 

The function should return a dictionary where the keys are the function names, and the values are lists [smallest_value, index] representing the node with the smallest value that fulfills each condition and is greater than or equal to the given threshold. If multiple nodes meet these requirements, choose the one with the smallest index. Return an empty dictionary if no values satisfy any condition, the array is empty, or all node values are less than the threshold.

The constraints are: 
- 1 <= length of `arr` <= 10000
- 0 <= node value in `arr`
- -1e7 <= `thresh` <= 1e7
- Number of functions in `cond_fn_dict` is up to 100
"""

def pluck_dict(arr, cond_fn_dict, thresh):
    
    # Check if array is empty
    if not arr:
        return {}
    
    res_dict = {}

    for name, fn in cond_fn_dict.items():  # For each function in the dictionary...
        filtered_values = [(idx, val) for idx, val in enumerate(arr) if val >= thresh and fn(val)]  # Filter the array
        if not filtered_values:  # If no values fulfill the condition...
            res_dict[name] = []  # Add empty. value to the results
        else:  # Otherwise...
            min_val_tuple = min(filtered_values, key=lambda x: (x[1], x[0]))  # Find the value with the smallest index and value
            res_dict[name] = [min_val_tuple[1], min_val_tuple[0]]  # Add it to the results
    return res_dict