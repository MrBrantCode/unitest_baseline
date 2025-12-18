"""
QUESTION:
Create a function named `spiral_matrix` that takes two parameters: an integer `n` and a list of integers `arr`. The function should return a 2D list representing an n x n matrix, where the numbers from the input list are sorted in ascending order and arranged in a spiral pattern from the center towards the outer layers. The input list should have exactly n^2 elements. If the length of the input list is not equal to n^2, the function should return an error message.
"""

def spiral_matrix(n, arr):
    arr.sort()  
    if len(arr) != n*n:
        return 'Error: incorrect array length'

    matrix = [[0]*n for _ in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]  
    x, y, c = 0, -1, 0  
    
    for i in range(n + n - 1):  
        for _ in range((n + n - i)//2):  
            x += dx[i%4]
            y += dy[i%4]
            matrix[x][y] = arr[c]
            c += 1

    return matrix