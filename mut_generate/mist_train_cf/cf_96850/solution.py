"""
QUESTION:
Create a function called `spiral_array` that takes a 2D array as input and returns a 1D array containing the elements of the input array in spiral order. The input array can have any number of rows and columns, and may contain negative numbers. The function should only use a single loop to iterate through the elements of the input array.
"""

def spiral_array(arr):
    spiral = []
    rows = len(arr)
    cols = len(arr[0])
    top_row = 0
    bottom_row = rows - 1
    left_col = 0
    right_col = cols - 1

    while top_row <= bottom_row and left_col <= right_col:
        # Traverse the top row
        for col in range(left_col, right_col + 1):
            spiral.append(arr[top_row][col])
        top_row += 1

        # Traverse the right column
        for row in range(top_row, bottom_row + 1):
            spiral.append(arr[row][right_col])
        right_col -= 1

        if top_row <= bottom_row:
            # Traverse the bottom row
            for col in range(right_col, left_col - 1, -1):
                spiral.append(arr[bottom_row][col])
            bottom_row -= 1

        if left_col <= right_col:
            # Traverse the left column
            for row in range(bottom_row, top_row - 1, -1):
                spiral.append(arr[row][left_col])
            left_col += 1

    return spiral