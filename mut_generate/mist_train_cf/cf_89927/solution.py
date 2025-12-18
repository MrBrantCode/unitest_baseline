"""
QUESTION:
Create a function named `spiral_array` that takes a 2D array as input and returns a 1D array with the elements arranged in a spiral order, starting from the top left corner and moving in a clockwise direction. The function should handle cases where the input array contains negative numbers, has an odd number of rows and columns, and only use a single loop to iterate through the elements of the input array.
"""

def spiral_array(input_array):
    rows = len(input_array)
    cols = len(input_array[0])
    output_array = []

    top_row = 0
    bottom_row = rows - 1
    left_col = 0
    right_col = cols - 1

    while top_row <= bottom_row and left_col <= right_col:
        # Traverse top row
        for i in range(left_col, right_col + 1):
            output_array.append(input_array[top_row][i])
        top_row += 1

        # Traverse right column
        for i in range(top_row, bottom_row + 1):
            output_array.append(input_array[i][right_col])
        right_col -= 1

        # Traverse bottom row
        if top_row <= bottom_row:
            for i in range(right_col, left_col - 1, -1):
                output_array.append(input_array[bottom_row][i])
            bottom_row -= 1

        # Traverse left column
        if left_col <= right_col:
            for i in range(bottom_row, top_row - 1, -1):
                output_array.append(input_array[i][left_col])
            left_col += 1

    return output_array