"""
QUESTION:
Write a function `search_2d_array` that efficiently searches for an item in a sorted two-dimensional array, where each row and column is sorted in ascending order. The function should take as input the 2D array and the target item, and return the position of the item if found or "Item not found" otherwise. The function should have a time complexity of O(m + n), where m is the number of rows and n is the number of columns in the array.
"""

def search_2d_array(matrix, target):
    """
    Searches for an item in a sorted two-dimensional array.
    
    Args:
    matrix (list): A 2D list of integers, where each row and column is sorted in ascending order.
    target (int): The item to be searched.
    
    Returns:
    tuple: The position of the item if found, otherwise "Item not found".
    """
    
    # Check if the matrix is empty
    if not matrix or not matrix[0]:
        return "Item not found"
    
    row, col = 0, len(matrix[0]) - 1
    
    # Continue the search until the boundaries of the array are reached
    while row < len(matrix) and col >= 0:
        # If the item is found, return its position
        if matrix[row][col] == target:
            return (row, col)
        # If the item is greater than the current element, move down to the next row
        elif matrix[row][col] < target:
            row += 1
        # If the item is smaller than the current element, move left to the previous column
        else:
            col -= 1
    
    # If the boundaries of the array are reached and the item is not found, return "Item not found"
    return "Item not found"