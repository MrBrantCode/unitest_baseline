"""
QUESTION:
Write a function `oddCells(m, n, indices)` that takes as input two integers `m` and `n` representing the dimensions of a matrix initialized to all zeros, and a 2D array `indices` where each `indices[i] = [ri, ci]` represents a 0-indexed location to perform some increment operations on the matrix. For each location `indices[i]`, increment all the cells on row `ri` and all the cells on column `ci`. Return the number of odd-valued cells in the matrix after applying the increment to all locations in `indices` and the final matrix. The function should run in `O(n + m + indices.length)` time and use only `O(n + m)` extra space. 

Constraints: `1 <= m, n <= 50` and `1 <= indices.length <= 100`.
"""

def oddCells(m: int, n: int, indices: list[list[int]]) -> int:
    matrix = [[0]*n for _ in range(m)]
    for index in indices:
        for i in range(n):
            matrix[index[0]][i] += 1
        for i in range(m):
            matrix[i][index[1]] += 1
    
    return sum([1 for row in matrix for num in row if num % 2 == 1])