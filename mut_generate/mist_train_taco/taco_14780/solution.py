"""
QUESTION:
Given a Sudoku data structure with size `NxN, N > 0 and √N == integer`, write a method to validate if it has been filled out correctly.


The data structure is a multi-dimensional Array, i.e:
```
[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],
  
  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],
  
  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]
```

**Rules for validation**

- Data structure dimension: `NxN` where `N > 0` and `√N == integer`
- Rows may only contain integers: `1..N (N included)`
- Columns may only contain integers: `1..N (N included)`
- *'Little squares'* (`3x3` in example above) may also only contain integers: `1..N (N included)`
"""

import math

def is_valid_sudoku(board):
    if not isinstance(board, list):
        return False
    
    n = len(board)
    rootN = int(round(math.sqrt(n)))
    
    if rootN * rootN != n:
        return False
    
    isValidRow = lambda r: isinstance(r, list) and len(r) == n and all([type(x) == int for x in r])
    
    if not all(map(isValidRow, board)):
        return False
    
    oneToN = set(range(1, n + 1))
    isOneToN = lambda l: set(l) == oneToN
    
    transpose = [[board[j][i] for i in range(n)] for j in range(n)]
    squares = [[board[p + x][q + y] for x in range(rootN) for y in range(rootN)] for p in range(0, n, rootN) for q in range(0, n, rootN)]
    
    return all(map(isOneToN, board)) and all(map(isOneToN, transpose)) and all(map(isOneToN, squares))