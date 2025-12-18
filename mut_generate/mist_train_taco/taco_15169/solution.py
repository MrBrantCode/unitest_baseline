"""
QUESTION:
Consider a table of size $n \times m$, initially fully white. Rows are numbered $1$ through $n$ from top to bottom, columns $1$ through $m$ from left to right. Some square inside the table with odd side length was painted black. Find the center of this square.


-----Input-----

The first line contains two integers $n$ and $m$ ($1 \le n, m \le 115$) — the number of rows and the number of columns in the table.

The $i$-th of the next $n$ lines contains a string of $m$ characters $s_{i1} s_{i2} \ldots s_{im}$ ($s_{ij}$ is 'W' for white cells and 'B' for black cells), describing the $i$-th row of the table.


-----Output-----

Output two integers $r$ and $c$ ($1 \le r \le n$, $1 \le c \le m$) separated by a space — the row and column numbers of the center of the black square.


-----Examples-----
Input
5 6
WWBBBW
WWBBBW
WWBBBW
WWWWWW
WWWWWW

Output
2 4

Input
3 3
WWW
BWW
WWW

Output
2 1
"""

def find_black_square_center(n, m, table):
    # Find the first occurrence of 'B'
    fir = []
    for i in range(n):
        for j in range(m):
            if table[i][j] == 'B':
                fir = [i, j]
                break
        if fir:
            break
    
    # Calculate the width of the black square
    cnt = 0
    for j in range(fir[1], m):
        if table[fir[0]][j] == 'B':
            cnt += 1
        else:
            break
    finy = fir[1] + cnt // 2
    
    # Calculate the height of the black square
    cnt = 0
    for i in range(fir[0], n):
        if table[i][fir[1]] == 'B':
            cnt += 1
        else:
            break
    finx = fir[0] + cnt // 2
    
    # Return the 1-based indices of the center
    return (finx + 1, finy + 1)