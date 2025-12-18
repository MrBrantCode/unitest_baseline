"""
QUESTION:
You are given a chessboard consisting of $n$ rows and $n$ columns. Rows are numbered from bottom to top from $1$ to $n$. Columns are numbered from left to right from $1$ to $n$. The cell at the intersection of the $x$-th column and the $y$-th row is denoted as $(x, y)$. Furthermore, the $k$-th column is a special column. 

Initially, the board is empty. There are $m$ changes to the board. During the $i$-th change one pawn is added or removed from the board. The current board is good if we can move all pawns to the special column by the followings rules:  Pawn in the cell $(x, y)$ can be moved to the cell $(x, y + 1)$, $(x - 1, y + 1)$ or $(x + 1, y + 1)$;  You can make as many such moves as you like;  Pawns can not be moved outside the chessboard;  Each cell can not contain more than one pawn. 

The current board may not always be good. To fix it, you can add new rows to the board. New rows are added at the top, i. e. they will have numbers $n+1, n+2, n+3, \dots$.

After each of $m$ changes, print one integer — the minimum number of rows which you have to add to make the board good.


-----Input-----

The first line contains three integers $n$, $k$ and $m$ ($1 \le n, m \le 2 \cdot 10^5; 1 \le k \le n$) — the size of the board, the index of the special column and the number of changes respectively.

Then $m$ lines follow. The $i$-th line contains two integers $x$ and $y$ ($1 \le x, y \le n$) — the index of the column and the index of the row respectively. If there is no pawn in the cell $(x, y)$, then you add a pawn to this cell, otherwise — you remove the pawn from this cell.


-----Output-----

After each change print one integer — the minimum number of rows which you have to add to make the board good.


-----Example-----
Input
5 3 5
4 4
3 5
2 4
3 4
3 5

Output
0
1
2
2
1
"""

import math

def calculate_min_rows_to_add(n, k, m, changes):
    l = math.ceil(math.log(2 * n) / math.log(2))
    p = 2 ** l
    memo = [0] * (2 * p)
    allres = [0] * (2 * p)
    exist = set()
    results = []
    
    for (x, y) in changes:
        l = abs(x - k) + y
        index = l + p
        
        if (x, y) in exist:
            exist.remove((x, y))
            while index != 0:
                memo[index] -= 1
                index = index // 2
        else:
            exist.add((x, y))
            while index != 0:
                memo[index] += 1
                index = index // 2
        
        index = (l + p) // 2
        allres[l + p] = l + memo[l + p] - 1
        if memo[l + p] == 0:
            allres[l + p] = 0
        
        while index != 0:
            allres[index] = max(allres[index * 2] + memo[index * 2 + 1], allres[index * 2 + 1])
            index = index // 2
        
        results.append(max(allres[1] - n, 0))
    
    return results