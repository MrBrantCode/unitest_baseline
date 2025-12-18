"""
QUESTION:
Construct a function `zigzagSum` that takes a 2D array `arr` as input, where `arr` has `m` rows and `n` columns. The function should access each element of the array in a zigzag pattern (right for even rows and left for odd rows) and return the sum of all elements accessed in the zigzag pattern. The time complexity of the solution should be O(m * n).
"""

def zigzagSum(arr):
    """
    This function calculates the sum of all elements in a 2D array accessed in a zigzag pattern.
    
    Parameters:
    arr (list): A 2D array with m rows and n columns.
    
    Returns:
    int: The sum of all elements accessed in the zigzag pattern.
    """
    # Initialize variables
    row = 0
    col = 0
    sum_elements = 0

    # Get the total number of rows and columns in the array
    num_rows = len(arr)
    num_cols = len(arr[0])

    # Loop through each element in the array
    for _ in range(num_rows * num_cols):
        # Access the current element and add it to the sum
        sum_elements += arr[row][col]
        
        # Check if the current row is even
        if row % 2 == 0:
            # Check if we are at the last column
            if col == num_cols - 1:
                # Move diagonally down-left
                row += 1
            else:
                # Move right
                col += 1
        else:
            # Check if we are at the first column
            if col == 0:
                # Move diagonally down-left
                row += 1
            else:
                # Move left
                col -= 1
                
    return sum_elements