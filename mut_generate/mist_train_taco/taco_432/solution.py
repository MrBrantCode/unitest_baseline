"""
QUESTION:
You are given a table consisting of n rows and m columns. Each cell of the table contains a number, 0 or 1. In one move we can choose some row of the table and cyclically shift its values either one cell to the left, or one cell to the right.

To cyclically shift a table row one cell to the right means to move the value of each cell, except for the last one, to the right neighboring cell, and to move the value of the last cell to the first cell. A cyclical shift of a row to the left is performed similarly, but in the other direction. For example, if we cyclically shift a row "00110" one cell to the right, we get a row "00011", but if we shift a row "00110" one cell to the left, we get a row "01100".

Determine the minimum number of moves needed to make some table column consist only of numbers 1.

Input

The first line contains two space-separated integers: n (1 ≤ n ≤ 100) — the number of rows in the table and m (1 ≤ m ≤ 104) — the number of columns in the table. Then n lines follow, each of them contains m characters "0" or "1": the j-th character of the i-th line describes the contents of the cell in the i-th row and in the j-th column of the table.

It is guaranteed that the description of the table contains no other characters besides "0" and "1".

Output

Print a single number: the minimum number of moves needed to get only numbers 1 in some column of the table. If this is impossible, print -1.

Examples

Input

3 6
101010
000100
100000


Output

3


Input

2 3
111
000


Output

-1

Note

In the first sample one way to achieve the goal with the least number of moves is as follows: cyclically shift the second row to the right once, then shift the third row to the left twice. Then the table column before the last one will contain only 1s.

In the second sample one can't shift the rows to get a column containing only 1s.
"""

def min_moves_to_all_ones_column(n, m, table):
    # Initialize a 2D list to store the minimum moves for each cell
    f = [[0 for _ in range(m)] for _ in range(n)]
    
    # Check if any row does not contain '1'
    for i in range(n):
        if '1' not in table[i]:
            return -1
    
    # Calculate the minimum moves for each cell
    for i in range(n):
        # Calculate the distance to the nearest '1' to the left
        tmp = table[i][::-1].find('1') + 1
        for j in range(m):
            if table[i][j] == '1':
                f[i][j] = 0
            else:
                f[i][j] = f[i][j - 1] + 1 if j > 0 else tmp
        
        # Calculate the distance to the nearest '1' to the right
        tmp = table[i].find('1') + 1
        for j in range(m - 1, -1, -1):
            f[i][j] = min(f[i][j], f[i][j + 1] + 1 if j + 1 < m else tmp)
    
    # Find the minimum moves needed to make a column all '1's
    ans = float('inf')
    for j in range(m):
        sm = 0
        for i in range(n):
            sm += f[i][j]
        ans = min(ans, sm)
    
    return ans if ans != float('inf') else -1