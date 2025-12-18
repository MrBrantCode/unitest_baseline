"""
QUESTION:
Create a function called `spiral_array` that takes a 2D array as input and returns a 1D array representing the spiral traversal of the input array. The function should work with any size of 2D array. The spiral traversal starts from the top-left corner and moves right, then down, then left, and finally up, moving in a clockwise direction.
"""

def spiral_array(input_array):
    rows = len(input_array)
    cols = len(input_array[0])
    spiral = []
    
    top_row = 0
    bottom_row = rows - 1
    left_col = 0
    right_col = cols - 1
    
    while top_row <= bottom_row and left_col <= right_col:
        # Traverse the top row
        for i in range(left_col, right_col + 1):
            spiral.append(input_array[top_row][i])
        top_row += 1
        
        # Traverse the right column
        for i in range(top_row, bottom_row + 1):
            spiral.append(input_array[i][right_col])
        right_col -= 1
        
        # Check if there is still a row left to traverse
        if top_row <= bottom_row:
            # Traverse the bottom row
            for i in range(right_col, left_col - 1, -1):
                spiral.append(input_array[bottom_row][i])
            bottom_row -= 1
        
        # Check if there is still a column left to traverse
        if left_col <= right_col:
            # Traverse the left column
            for i in range(bottom_row, top_row - 1, -1):
                spiral.append(input_array[i][left_col])
            left_col += 1
    
    return spiral