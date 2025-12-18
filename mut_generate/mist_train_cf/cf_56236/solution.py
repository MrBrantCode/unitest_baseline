"""
QUESTION:
Create a function `find_vect` that takes a 3D array `lst3d` and two integers `x` and `y` as input. The function should return a list of tuples, where each tuple contains the coordinates (depth, row, index) of the subvector `[x, y]` in the 3D array. The returned list should be sorted in ascending order by depth, then by row, and finally by index. The 3D array is a vector of vectors of vectors, where each sub-sub-vector may not contain the same number of elements. The coordinates should be zero-indexed.
"""

def find_vect(lst3d, x, y):
    """
    This function finds the coordinates of the subvector [x, y] in a 3D array.
    
    Args:
        lst3d (list): A 3D array (vector of vectors of vectors).
        x (int): The first element of the subvector.
        y (int): The second element of the subvector.
    
    Returns:
        list: A list of tuples, where each tuple contains the coordinates (depth, row, index) of the subvector [x, y] in the 3D array.
    """
    result = []
    
    for depth, subvector in enumerate(lst3d):
        for row, sub_subvector in enumerate(subvector):
            for index in range(len(sub_subvector) - 1):
                if sub_subvector[index] == x and sub_subvector[index + 1] == y:
                    result.append((depth, row, index))
                    
    # Sorting is not necessary here as elements are inserted in ascending order due to the sequence of traversal
    # If you have any other way of traversal where this cannot be ensured, use the below line of code to sort
    # result.sort()
    
    return result