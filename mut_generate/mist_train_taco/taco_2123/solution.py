"""
QUESTION:
We have an N×N checkerboard.

From the square at the upper left corner, a square that is i squares to the right and j squares below is denoted as (i, j). Particularly, the square at the upper left corner is denoted as (0, 0).

Each square (i, j) such that i+j is even, is colored black, and the other squares are colored white.

We will satisfy the following condition by painting some of the white squares:

* Any black square can be reached from square (0, 0) by repeatedly moving to a black square that shares a side with the current square.



Achieve the objective by painting at most 170000 squares black.

Constraints

* 1 \leq N \leq 1,000

Input

The input is given from Standard Input in the following format:


N


Output

Print the squares to paint in the following format:


K
x_1 y_1
x_2 y_2
:
x_K y_K


This means that a total of K squares are painted black, the i-th of which is (x_i, y_i).

Judging

The output is considered correct only if all of the following conditions are satisfied:

* 0 \leq K \leq 170000
* 0 \leq x_i, y_i \leq N-1
* For each i, x_i + y_i is odd.
* If i \neq j, then (x_i, y_i) \neq (x_j, y_j).
* The condition in the statement is satisfied by painting all specified squares.

Examples

Input

2


Output

1
1 0


Input

4


Output

3
0 1
2 1
2 3
"""

def paint_checkerboard(N):
    ans = []
    
    # Paint squares in the first (n-1) rows
    for i in range(N - 1):
        if i % 2:
            ans.append((i, 0))
    
    # Paint specific patterns in the first (n-1) rows
    for i in range(N - 1):
        if i % 6 == 1:
            for j in range(2, N):
                if j % 2 == 0:
                    ans.append((i, j))
        if i % 6 == 4:
            for j in range(N):
                if j % 2:
                    ans.append((i, j))
    
    # Paint squares in the last row
    for j in range(N):
        if (N - 1 + j) % 2:
            ans.append((N - 1, j))
    
    K = len(ans)
    return K, ans