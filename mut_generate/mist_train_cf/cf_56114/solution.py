"""
QUESTION:
Delete specific rows from a 2D numpy array. The function should take two parameters: a 2D numpy array and a list of row indices to delete. The function should ignore out-of-bound indices. 

Example: if the input array is [[1,2,3,4], [5,6,7,8], [9,10,11,12]] and the row indices to delete are [0, 2, 3, 4], the function should return [[5, 6, 7, 8]].
"""

import numpy as np

def delete_rows(a, del_row):
    """
    Delete specific rows from a 2D numpy array.

    Parameters:
    a (numpy array): The input 2D numpy array.
    del_row (list): A list of row indices to delete.

    Returns:
    numpy array: The resulting array after deleting the specified rows.
    """
    result = a.copy()
    for i in sorted(del_row, reverse=True):
        if i < np.size(a, 0):
            result = np.delete(result, i, axis=0)
    return result