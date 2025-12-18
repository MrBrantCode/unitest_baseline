"""
QUESTION:
Create a function `pluck(arr, cond_fn)` that traverses a mathematical tree structured as an array, with each node corresponding to a positive integer. The function should 'pluck' the node with the smallest value that adheres to a particular condition defined by the auxiliary function `cond_fn`, which evaluates an integer and returns a boolean. If multiple nodes meet the condition and share the minimum value, the one with the highest index should be selected. The function should return a list containing the minimal value and its corresponding index. If the array is empty or no nodes satisfy the condition, the function should return an empty list. The array can have a random length from 1 to 10,000 and node values can extend up to 10^9.
"""

def pluck(arr, cond_fn):
    """
    Traverse a mathematical tree structured as an array, plucking the node with the smallest value 
    that adheres to a particular condition defined by the auxiliary function `cond_fn`.

    Args:
    arr (list): A list of positive integers representing the mathematical tree.
    cond_fn (function): A function that evaluates an integer and returns a boolean.

    Returns:
    list: A list containing the minimal value and its corresponding index. If the array is empty or 
    no nodes satisfy the condition, an empty list is returned.
    """

    result = []
    for i, num in enumerate(arr):
        if cond_fn(num):
            result.append([num, i])
    if not result:
        return []
    result.sort(key=lambda x: (x[0], -x[1]))
    return result[0]