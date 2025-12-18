"""
QUESTION:
Omkar is creating a mosaic using colored square tiles, which he places in an n × n grid. When the mosaic is complete, each cell in the grid will have either a glaucous or sinoper tile. However, currently he has only placed tiles in some cells. 

A completed mosaic will be a mastapeece if and only if each tile is adjacent to exactly 2 tiles of the same color (2 tiles are adjacent if they share a side.) Omkar wants to fill the rest of the tiles so that the mosaic becomes a mastapeece. Now he is wondering, is the way to do this unique, and if it is, what is it?

Input

The first line contains a single integer n (1 ≤ n ≤ 2000).

Then follow n lines with n characters in each line. The i-th character in the j-th line corresponds to the cell in row i and column j of the grid, and will be S if Omkar has placed a sinoper tile in this cell, G if Omkar has placed a glaucous tile, . if it's empty. 

Output

On the first line, print UNIQUE if there is a unique way to get a mastapeece, NONE if Omkar cannot create any, and MULTIPLE if there is more than one way to do so. All letters must be uppercase.

If you print UNIQUE, then print n additional lines with n characters in each line, such that the i-th character in the j^{th} line is S if the tile in row i and column j of the mastapeece is sinoper, and G if it is glaucous. 

Examples

Input


4
S...
..G.
....
...S


Output


MULTIPLE


Input


6
S.....
....G.
..S...
.....S
....G.
G.....


Output


NONE


Input


10
.S....S...
..........
...SSS....
..........
..........
...GS.....
....G...G.
..........
......G...
..........


Output


UNIQUE
SSSSSSSSSS
SGGGGGGGGS
SGSSSSSSGS
SGSGGGGSGS
SGSGSSGSGS
SGSGSSGSGS
SGSGGGGSGS
SGSSSSSSGS
SGGGGGGGGS
SSSSSSSSSS


Input


1
.


Output


NONE

Note

For the first test case, Omkar can make the mastapeeces

SSSS

SGGS

SGGS

SSSS

and 

SSGG

SSGG

GGSS

GGSS.

For the second test case, it can be proven that it is impossible for Omkar to add tiles to create a mastapeece.

For the third case, it can be proven that the given mastapeece is the only mastapeece Omkar can create by adding tiles.

For the fourth test case, it's clearly impossible for the only tile in any mosaic Omkar creates to be adjacent to two tiles of the same color, as it will be adjacent to 0 tiles total.
"""

def determine_mosaic_status(n, grid):
    o = {'G': 'S', 'S': 'G'}
    d = [list(row) for row in grid]
    f = [1] * (n * n)
    finished = 1
    
    if n % 2:
        return "NONE", None
    
    x = [''] * (n // 2)
    
    def findt(i, j):
        return abs(j - i) // 2 if (j - i) % 2 else min(i + j, 2 * (n - 1) - j - i) // 2
    
    def findr(i, j, t):
        if (j - i) % 2:
            return o[t] if min(i, j) % 2 else t
        elif i + j < n:
            return o[t] if i % 2 else t
        else:
            return t if i % 2 else o[t]
    
    for i in range(n):
        for j in range(n):
            if d[i][j] != '.':
                t = findt(i, j)
                r = findr(i, j, d[i][j])
                if x[t] == o[r]:
                    return "NONE", None
                else:
                    x[t] = r
    
    for i in range(n // 2):
        if not x[i]:
            return "MULTIPLE", None
    
    for i in range(n):
        for j in range(n):
            d[i][j] = findr(i, j, x[findt(i, j)])
    
    completed_grid = [''.join(row) for row in d]
    return "UNIQUE", completed_grid