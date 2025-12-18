"""
QUESTION:
You are given a square matrix consisting of n rows and n columns. We assume that the rows are numbered from 1 to n from top to bottom and the columns are numbered from 1 to n from left to right. Some cells (n - 1 cells in total) of the the matrix are filled with ones, the remaining cells are filled with zeros. We can apply the following operations to the matrix:

  1. Swap i-th and j-th rows of the matrix; 
  2. Swap i-th and j-th columns of the matrix. 



You are asked to transform the matrix into a special form using these operations. In that special form all the ones must be in the cells that lie below the main diagonal. Cell of the matrix, which is located on the intersection of the i-th row and of the j-th column, lies below the main diagonal if i > j.

Input

The first line contains an integer n (2 ≤ n ≤ 1000) — the number of rows and columns. Then follow n - 1 lines that contain one's positions, one per line. Each position is described by two integers xk, yk (1 ≤ xk, yk ≤ n), separated by a space. A pair (xk, yk) means that the cell, which is located on the intersection of the xk-th row and of the yk-th column, contains one.

It is guaranteed that all positions are distinct.

Output

Print the description of your actions. These actions should transform the matrix to the described special form.

In the first line you should print a non-negative integer m (m ≤ 105) — the number of actions. In each of the next m lines print three space-separated integers t, i, j (1 ≤ t ≤ 2, 1 ≤ i, j ≤ n, i ≠ j), where t = 1 if you want to swap rows, t = 2 if you want to swap columns, and i and j denote the numbers of rows or columns respectively.

Please note, that you do not need to minimize the number of operations, but their number should not exceed 105. If there are several solutions, you may print any of them.

Examples

Input

2
1 2


Output

2
2 1 2
1 1 2


Input

3
3 1
1 3


Output

3
2 2 3
1 1 3
1 1 2


Input

3
2 1
3 2


Output

0
"""

def transform_matrix_to_special_form(n, ones_positions):
    row = [0] * n
    col = [0] * n
    a = [[0 for j in range(n)] for i in range(n)]
    
    for x, y in ones_positions:
        row[x - 1] += 1
        col[y - 1] += 1
        a[x - 1][y - 1] = 1
    
    ans = []
    
    for i in range(n):
        zci = -1
        for j in range(n - i):
            if col[j] == 0:
                zci = j
                break
        if zci == -1:
            break
        if zci != n - i - 1:
            ans.append((2, zci + 1, n - i))
            col[n - i - 1], col[zci] = col[zci], col[n - i - 1]
            for j in range(n - i):
                a[j][zci], a[j][n - i - 1] = a[j][n - i - 1], a[j][zci]
        
        nzri = -1
        for j in range(n - i):
            if row[j] != 0:
                nzri = j
                break
        if nzri == -1:
            break
        if nzri != n - i - 1:
            ans.append((1, nzri + 1, n - i))
            row[nzri], row[n - i - 1] = row[n - i - 1], row[nzri]
        for j in range(n - i):
            if a[nzri][j] == 1:
                col[j] -= 1
            a[nzri][j], a[n - i - 1][j] = a[n - i - 1][j], a[nzri][j]
    
    return ans