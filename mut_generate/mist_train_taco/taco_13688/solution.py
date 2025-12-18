"""
QUESTION:
Write a function ```x(n)``` that takes in a number ```n``` and returns an ```nxn``` array with an ```X``` in the middle. The ```X``` will be represented by ```1's``` and the rest will be ```0's```. 
E.g.
```python
x(5) ==  [[1, 0, 0, 0, 1],
          [0, 1, 0, 1, 0],
          [0, 0, 1, 0, 0],
          [0, 1, 0, 1, 0],
          [1, 0, 0, 0, 1]];
          
x(6) ==  [[1, 0, 0, 0, 0, 1],
          [0, 1, 0, 0, 1, 0],
          [0, 0, 1, 1, 0, 0],
          [0, 0, 1, 1, 0, 0],
          [0, 1, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 1]];
```
"""

def create_x_matrix(n):
    # Initialize an nxn matrix filled with 0's
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the matrix with 1's to form the X pattern
    for i in range(n):
        matrix[i][i] = 1           # Main diagonal
        matrix[i][n - i - 1] = 1   # Anti-diagonal
    
    return matrix