"""
QUESTION:
Create a function `solve_sudoku` that takes a 9x9 2D grid as input and returns `True` if a valid Sudoku solution exists and `False` otherwise. The grid can contain zeros representing empty cells. The function should fill in the empty cells with numbers from 1 to 9 in such a way that each row, column, and 3x3 sub-grid contains each number exactly once.
"""

def solve_sudoku(arr):
    # 'l' is a list variable that keeps the record of row and col in find_empty_location Function     
    def find_empty_location(arr, l):
        for row in range(9):
            for col in range(9):
                if(arr[row][col]==0):
                    l[0]=row
                    l[1]=col
                    return True
        return False

    def used_in_row(arr, row, num):
        for i in range(9):
            if(arr[row][i] == num):
                return True
        return False

    def used_in_col(arr, col, num):
        for i in range(9):
            if(arr[i][col] == num):
                return True
        return False

    def used_in_box(arr, row, col, num):
        for i in range(3):
            for j in range(3):
                if(arr[i+row - row%3][j+col - col%3] == num):
                    return True
        return False

    def check_location_is_safe(arr, row, col, num):
        return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row, col, num)

    l=[0,0]
    if(not find_empty_location(arr,l)):
        return True
    row=l[0]
    col=l[1]
    for num in range(1,10):
        if(check_location_is_safe(arr,row,col,num)):
            arr[row][col]=num
            if(solve_sudoku(arr)):
                return True
            arr[row][col] = 0
    return False