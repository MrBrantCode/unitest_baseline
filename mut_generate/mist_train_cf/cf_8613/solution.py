"""
QUESTION:
Implement a function `find_submatrix(array1, array2)` that finds the indices of the first occurrence of a submatrix in `array1` that matches `array2`. The function should return the starting indices (i, j) of the matching submatrix. If no matching submatrix is found, return `None`. 

Restrictions: 
- The time complexity should be less than O(n^4), where n is the size of the larger matrix (`array1`).
- The space complexity should be less than O(n^2), where n is the size of the larger matrix (`array1`).
- The input matrices can be of any size, but `array2` must be smaller than or equal to `array1` in both rows and columns.
- The function should handle all possible edge cases, including when `array2` is not found in `array1`.
"""

def find_submatrix(array1, array2):
    """
    Finds the indices of the first occurrence of a submatrix in `array1` that matches `array2`.
    
    Args:
        array1 (list of lists): The larger matrix to search in.
        array2 (list of lists): The smaller matrix to search for.
    
    Returns:
        tuple or None: The starting indices (i, j) of the matching submatrix, or None if no matching submatrix is found.
    """

    rows1, cols1 = len(array1), len(array1[0])
    rows2, cols2 = len(array2), len(array2[0])

    for i in range(rows1 - rows2 + 1):
        for j in range(cols1 - cols2 + 1):
            found = True
            for row in range(rows2):
                for col in range(cols2):
                    if array1[i + row][j + col] != array2[row][col]:
                        found = False
                        break
                if not found:
                    break
            if found:
                return i, j

    return None