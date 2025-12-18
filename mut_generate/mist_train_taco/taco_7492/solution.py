"""
QUESTION:
# Task
 Given a rectangular matrix containing only digits, calculate the number of different `2 × 2` squares in it.

# Example

 For
```
matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
```
the output should be `6`.

 Here are all 6 different 2 × 2 squares:
 
 ```
 1 2
 2 2

 2 1
 2 2

 2 2
 2 2

 2 2
 1 2

 2 2
 2 3

 2 3
 2 1
 ```

# Input/Output


 - `[input]` 2D integer array `matrix`

    Constraints: 
    
    `1 ≤ matrix.length ≤ 100,`
    
    `1 ≤ matrix[i].length ≤ 100,`
    
    `0 ≤ matrix[i][j] ≤ 9.`


 - `[output]` an integer

    The number of different `2 × 2` squares in matrix.
"""

def count_unique_2x2_squares(matrix):
    unique_squares = set()
    rows = len(matrix)
    cols = len(matrix[0])
    
    for row in range(rows - 1):
        for col in range(cols - 1):
            square = (
                matrix[row][col], matrix[row][col + 1],
                matrix[row + 1][col], matrix[row + 1][col + 1]
            )
            unique_squares.add(square)
    
    return len(unique_squares)