"""
QUESTION:
Write a Python function named `pluck` that takes an array of non-negative integers, a condition function `cond_fn`, and a threshold value `thresh` as inputs. The function should return a list containing the smallest node value that satisfies the condition and is greater than or equal to the threshold, along with its index in the array. If no such value exists or the array is empty, the function should return an empty list. 

The length of the array should be between 1 and 10000, the value of each node should be a non-negative integer, and the threshold should be between -1e7 and 1e7.
"""

def pluck(arr, cond_fn, thresh):
    """
    Extracts and returns the node with the smallest value that satisfies a certain condition and is greater or equal to 
    a specified threshold.

    Args:
        arr (list): An array of non-negative integers representing nodes of a tree branch.
        cond_fn (function): A function that takes a node value and returns a boolean value indicating 
                            whether the condition is satisfied.
        thresh (int): A threshold, the node value must be greater or equal to this.

    Returns:
        list: The smallest node value satisfying the condition and the index of that value in the format [smallest_value, index].
              Returns an empty list if no values fulfill the condition, the array is empty, or all node values are below the threshold.

    Constraints:
        * arr length is between 1 and 10000.
        * Each node value in arr is a non-negative integer.
        * thresh is between -1e7 and 1e7.
    """

    eligible_nodes = [(value, index) for index, value in enumerate(arr) if value >= thresh and cond_fn(value)]
    if eligible_nodes:
        smallest_value_node = min(eligible_nodes)
        return list(smallest_value_node)
    return []