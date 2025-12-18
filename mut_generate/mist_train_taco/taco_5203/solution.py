"""
QUESTION:
We have a grid with N rows and M columns of squares. Initially, all the squares are white.

There is a button attached to each row and each column. When a button attached to a row is pressed, the colors of all the squares in that row are inverted; that is, white squares become black and vice versa. When a button attached to a column is pressed, the colors of all the squares in that column are inverted.

Takahashi can freely press the buttons any number of times. Determine whether he can have exactly K black squares in the grid.

Constraints

* 1 \leq N,M \leq 1000
* 0 \leq K \leq NM

Input

Input is given from Standard Input in the following format:


N M K


Output

If Takahashi can have exactly K black squares in the grid, print `Yes`; otherwise, print `No`.

Examples

Input

2 2 2


Output

Yes


Input

2 2 1


Output

No


Input

3 5 8


Output

Yes


Input

7 9 20


Output

No
"""

def can_have_exactly_k_black_squares(N, M, K):
    for i in range(N + 1):
        for j in range(M + 1):
            if j * (N - i) + i * (M - j) == K:
                return 'Yes'
    return 'No'