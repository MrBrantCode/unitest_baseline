"""
QUESTION:
We have an H \times W grid whose squares are painted black or white. The square at the i-th row from the top and the j-th column from the left is denoted as (i, j).
Snuke would like to play the following game on this grid. At the beginning of the game, there is a character called Kenus at square (1, 1). The player repeatedly moves Kenus up, down, left or right by one square. The game is completed when Kenus reaches square (H, W) passing only white squares.
Before Snuke starts the game, he can change the color of some of the white squares to black. However, he cannot change the color of square (1, 1) and (H, W). Also, changes of color must all be carried out before the beginning of the game.
When the game is completed, Snuke's score will be the number of times he changed the color of a square before the beginning of the game. Find the maximum possible score that Snuke can achieve, or print -1 if the game cannot be completed, that is, Kenus can never reach square (H, W) regardless of how Snuke changes the color of the squares.  
The color of the squares are given to you as characters s_{i, j}. If square (i, j) is initially painted by white, s_{i, j} is .; if square (i, j) is initially painted by black, s_{i, j} is #.
"""

from queue import Queue

def calculate_max_score(h, w, grid):
    # Count the number of initially black squares
    num_w = sum(row.count('#') for row in grid)
    
    # Add borders to the grid to simplify boundary checks
    for i in range(h):
        grid[i] = ['#'] + grid[i] + ['#']
    grid.insert(0, ['#' for _ in range(w + 2)])
    grid.append(['#' for _ in range(w + 2)])
    
    # Initialize BFS queue and variables
    q = Queue()
    q.put([1, 1, 0])  # Starting position (1, 1) with 0 changes
    grid[1][1] = '#'  # Mark the starting position as visited
    Z = -1  # Variable to store the result
    
    # Perform BFS
    while not q.empty():
        x, y, cnt = q.get()
        if (x, y) == (h, w):
            Z = cnt
            break
        for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if grid[i][j] != '#':
                grid[i][j] = '#'
                q.put([i, j, cnt + 1])
    
    # If Z is -1, the game cannot be completed
    if Z == -1:
        return -1
    else:
        return h * w - Z - 1 - num_w