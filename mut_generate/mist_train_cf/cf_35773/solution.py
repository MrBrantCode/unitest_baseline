"""
QUESTION:
Write a function `max_hourglass_sum(matrix)` that takes a 4x4 matrix of integers as input and returns the maximum sum of an hourglass shape in the matrix. The hourglass shape is defined as a subset of values in the matrix arranged in the following pattern:
```
a b c
  d
e f g
```
Where a, b, c, d, e, f, and g are distinct values in the matrix. The function should only consider hourglass shapes that fit entirely within the 4x4 matrix.
"""

def max_hourglass_sum(matrix):
    max_sum = None
    for i in range(4):
        for j in range(4):
            if j + 2 < 4 and i + 2 < 4:
                s = sum(matrix[i][j:j+3]) + matrix[i+1][j+1] + sum(matrix[i+2][j:j+3])
                if max_sum is None or s > max_sum:
                    max_sum = s
    return max_sum