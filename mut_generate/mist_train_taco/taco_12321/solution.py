"""
QUESTION:
Create an identity matrix of the specified size( >= 0).

Some examples:

```
(1)  =>  [[1]]

(2) => [ [1,0],
         [0,1] ]

       [ [1,0,0,0,0],
         [0,1,0,0,0],
(5) =>   [0,0,1,0,0],
         [0,0,0,1,0],
         [0,0,0,0,1] ]   

```
"""

def generate_identity_matrix(size: int) -> list[list[int]]:
    return [[1 if i == j else 0 for i in range(size)] for j in range(size)]