"""
QUESTION:
You have an n × m rectangle table, its cells are not initially painted. Your task is to paint all cells of the table. The resulting picture should be a tiling of the table with squares. More formally:  each cell must be painted some color (the colors are marked by uppercase Latin letters);  we will assume that two cells of the table are connected if they are of the same color and share a side; each connected region of the table must form a square. 

Given n and m, find lexicographically minimum coloring of the table that meets the described properties.


-----Input-----

The first line contains two integers, n and m (1 ≤ n, m ≤ 100).


-----Output-----

Print lexicographically minimum coloring of the table that meets the described conditions. 

One coloring (let's call it X) is considered lexicographically less than the other one (let's call it Y), if:  consider all the table cells from left to right and from top to bottom (first, the first cell in the first row, then the second cell in the first row and so on);  let's find in this order the first cell that has distinct colors in two colorings;  the letter that marks the color of the cell in X, goes alphabetically before the letter that marks the color of the cell in Y. 


-----Examples-----
Input
1 3

Output
ABA

Input
2 2

Output
AA
AA

Input
3 4

Output
AAAB
AAAC
AAAB
"""

def lexicographically_minimum_coloring(n, m):
    ANS = [[-1] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if ANS[i][j] == -1:
                for koma in ['A', 'B', 'C', 'D', 'E', 'F']:
                    for (k, l) in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                        if 0 <= k < n and 0 <= l < m and (ANS[k][l] == koma):
                            break
                    else:
                        nkoma = koma
                        break
                MAXlength = 1
                if nkoma == 'A':
                    for length in range(1, 101):
                        if i + length >= n or j + length >= m:
                            break
                        for (k, l) in [(i - 1, j + length), (i + length, j - 1)]:
                            if 0 <= k < n and 0 <= l < m and (ANS[k][l] == nkoma):
                                break
                            if 0 <= i < n and ANS[i][j + length] != -1:
                                break
                        else:
                            MAXlength = length + 1
                elif nkoma == 'B':
                    for length in range(1, 101):
                        if i + length >= n or j + length >= m:
                            break
                        flag = 0
                        if 0 <= i - 1 < n and ANS[i - 1][j + length] == 'A':
                            flag = 1
                        if 0 <= j - 1 < m and ANS[i + length][j - 1] == nkoma:
                            break
                        if 0 <= i < n and ANS[i][j + length] != -1:
                            break
                        if flag == 1:
                            MAXlength = length + 1
                        else:
                            break
                for k in range(i, i + MAXlength):
                    for l in range(j, j + MAXlength):
                        ANS[k][l] = nkoma
    
    return [''.join(row) for row in ANS]