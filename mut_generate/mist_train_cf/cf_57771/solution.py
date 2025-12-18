"""
QUESTION:
Function: `numMagicSquaresInside(grid)`

Given a grid of integers, count the number of 3x3 "magic square" subgrids. A 3x3 magic square is a 3x3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Restrictions:
- The input grid is a 2D list of integers with row and column lengths between 1 and 50.
- Each cell in the grid contains an integer between 0 and 100.
"""

def numMagicSquaresInside(grid):
    def is_magic(sq):
        s = sum(sq[0])
        
        return set(x for row in sq for x in row) == set(range(1, 10)) and \
               all(sum(row) == s for row in sq) and \
               all(sum(sq[i][j] for i in range(3)) == s for j in range(3)) and \
               sum(sq[i][i] for i in range(3)) == s and \
               sum(sq[i][2 - i] for i in range(3)) == s

    return sum(is_magic([[grid[i + dx][j + dy] for dx in range(3)] for dy in range(3)]) 
               for i in range(len(grid) - 2) for j in range(len(grid[0]) - 2))