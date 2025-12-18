"""
QUESTION:
Implement a function `find_indices` that takes two parameters: an integer `x` and a list `arr` of integers. The function should return a list of indices where the number `x` appears in `arr`. Note that `arr` may contain duplicate elements and no built-in functions or libraries should be used to solve this problem.
"""

def find_indices(x, arr):
    """
    Returns a list of indices where the number `x` appears in `arr`.

    Parameters:
    x (int): The number to find indices for.
    arr (list): The list of integers to search in.

    Returns:
    list: A list of indices where `x` appears in `arr`.
    """
    indices = []
    for i in range(len(arr)):
        if arr[i] == x:
            indices.append(i)
    return indices