"""
QUESTION:
You received as a gift a very clever robot walking on a rectangular board. Unfortunately, you understood that it is broken and behaves rather strangely (randomly). The board consists of N rows and M columns of cells. The robot is initially at some cell on the i-th row and the j-th column. Then at every step the robot could go to some another cell. The aim is to go to the bottommost (N-th) row. The robot can stay at it's current cell, move to the left, move to the right, or move to the cell below the current. If the robot is in the leftmost column it cannot move to the left, and if it is in the rightmost column it cannot move to the right. At every step all possible moves are equally probable. Return the expected number of step to reach the bottommost row.

Input

On the first line you will be given two space separated integers N and M (1 ≤ N, M ≤ 1000). On the second line you will be given another two space separated integers i and j (1 ≤ i ≤ N, 1 ≤ j ≤ M) — the number of the initial row and the number of the initial column. Note that, (1, 1) is the upper left corner of the board and (N, M) is the bottom right corner.

Output

Output the expected number of steps on a line of itself with at least 4 digits after the decimal point.

Examples

Input

10 10
10 4


Output

0.0000000000


Input

10 14
5 14


Output

18.0038068653
"""

def calculate_expected_steps(n, m, i, j):
    if i == n:
        return 0.0
    if m == 1:
        return 2.0 * (n - i)
    
    e = [0.0] * m
    a = [0] * m
    b = [0] * m
    
    for l in range(n - 1, 0, -1):
        a[0], b[0] = 0.5, 0.5 * (3 + e[0])
        for k in range(1, m - 1):
            a[k] = 1 / (3 - a[k - 1])
            b[k] = a[k] * (b[k - 1] + 4 + e[k])
        e[m - 1] = (3 + b[m - 2] + e[m - 1]) / (2 - a[m - 2])
        for k in range(m - 2, -1, -1):
            e[k] = a[k] * e[k + 1] + b[k]
        if l == i:
            return e[j - 1]
    
    return e[j - 1]