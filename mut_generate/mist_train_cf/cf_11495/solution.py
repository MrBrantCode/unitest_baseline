"""
QUESTION:
Write a function named `print2Dlist` that takes a 2D list as input and prints its elements in a clockwise spiral order starting from the top-left corner. The function should handle empty input lists.
"""

def print2Dlist(list):
    if len(list) == 0:
        return
    
    top_row = 0
    bottom_row = len(list) - 1
    left_col = 0
    right_col = len(list[0]) - 1
    
    while top_row <= bottom_row and left_col <= right_col:
        # Print top row
        for i in range(left_col, right_col + 1):
            print(list[top_row][i], end=" ")
        top_row += 1
        
        # Print right column
        for i in range(top_row, bottom_row + 1):
            print(list[i][right_col], end=" ")
        right_col -= 1
        
        # Print bottom row
        if top_row <= bottom_row:
            for i in range(right_col, left_col - 1, -1):
                print(list[bottom_row][i], end=" ")
            bottom_row -= 1
        
        # Print left column
        if left_col <= right_col:
            for i in range(bottom_row, top_row - 1, -1):
                print(list[i][left_col], end=" ")
            left_col += 1
    
    print()