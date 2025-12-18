"""
QUESTION:
Create a function named `check_solution` that takes a 2-dimensional 9x9 array as input. The function should return `True` if the array represents a valid Sudoku solution, where every row, column, and 3x3 box contains the numbers 1 to 9 without any repetitions. If the array does not meet this condition, the function should return `False`.
"""

def check_solution(arr):
    for i in range(9):
        row = arr[i]
        if sorted(row) != list(range(1,10)):
            return False
        column = [arr[j][i] for j in range(9)]
        if sorted(column) != list(range(1,10)):
            return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            box = [arr[x][y] for x in range(i,i+3) for y in range(j,j+3)]
            if sorted(box) != list(range(1,10)):
                return False
    return True