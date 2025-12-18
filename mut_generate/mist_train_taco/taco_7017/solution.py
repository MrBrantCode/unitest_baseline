"""
QUESTION:
A mouse encountered a nice big cake and decided to take a walk across it, eating the berries on top of the cake on its way. The cake is rectangular, neatly divided into squares; some of the squares have a berry in them, and some don't.

The mouse is in a bit of a hurry, though, so once she enters the cake from its northwest corner (the top left cell in the input data), she will only go east (right) or south (down), until she reaches the southeast corner (the bottom right cell). She will eat every berry in the squares she passes through, but not in the other squares.

The mouse tries to choose her path so as to maximize the number of berries consumed. However, her haste and hunger might be clouding her judgement, leading her to suboptimal decisions...

Input

The first line of input contains two integers H and W (1 ≤ H, W ≤ 5), separated by a space, — the height and the width of the cake.

The next H lines contain a string of W characters each, representing the squares of the cake in that row: '.' represents an empty square, and '*' represents a square with a berry.

Output

Output the number of berries the mouse will eat following her strategy.

Examples

Input


4 3
*..
.*.
..*
...


Output


3


Input


4 4
.*..
*...
...*
..*.


Output


2


Input


3 4
..**
*...
....


Output


1


Input


5 5
..*..
.....
**...
**...
**...


Output


1
"""

def max_berries_eaten(H, W, grid):
    (r, c) = (0, 0)
    ans = 0
    
    for i in range(H + W - 2):
        if grid[r][c] == '*':
            ans += 1
        if r == H - 1:
            c += 1
            continue
        if c == W - 1:
            r += 1
            continue
        
        right = (float('inf'), float('inf'))
        for row in range(r, H):
            if '*' in grid[row][c + 1:]:
                right = min(right, (grid[row][c + 1:].index('*'), row - r))
        
        down = (float('inf'), float('inf'))
        for col in range(c, W):
            column = [grid[r][col] for r in range(r + 1, H)]
            if '*' in column:
                down = min(down, (column.index('*'), col - c))
        
        if down < right:
            r += 1
        else:
            c += 1
    
    if grid[r][c] == '*':
        ans += 1
    
    return ans