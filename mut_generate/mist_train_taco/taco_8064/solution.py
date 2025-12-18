"""
QUESTION:
There is a plan view consisting of 12 vertical and 12 horizontal squares showing the terrain. Each square is painted white or black. White represents the sea and black represents the land. When two black squares touch each other vertically or horizontally, they are said to be continuous. In this plan view, the area created by only one black square or a continuous black square is called an "island". For example, in the figure below, there are five islands.


■■■■ □□□□ ■■■■
■■■ □□□□□ ■■■■
■■ □□□□□□ ■■■■
■ □□□□□□□ ■■■■
□□□ ■ □□□ ■ □□□□
□□□□□□ ■■■ □□□
□□□□□ ■■■■■ □□
■ □□□ ■■■■■■■ □
■■ □□□ ■■■■■ □□
■■■ □□□ ■■■ □□□
■■■■ □□□ ■ □□□□
□□□□□□□□□□□□


Create a program that reads the mass data and outputs the number of islands.

Hint

The following shows the sample inputs with ■ and □.


■■■■ □□□□ ■■■■ □ ■ □□□ ■■■■■ □□ □□□□□□□□□□□□
■■■ □□□□□ ■■■■ ■■ □□ ■ □□□□□ ■ □ ■■■■■■■■■■■■
■■ □□□□□□ ■■■■ □ ■ □□ ■ □□□□□□ ■ ■ □□□ ■ □ ■ □□□□ ■
■ □□□□□□□ ■■■■ □ ■ □□□□□□□□□ ■ ■ □□□ ■ □ ■ □□□□ ■
□□□ ■ □□□ ■ □□□□ □ ■ □□□□□□□ ■■ □ ■ □□□ ■ □ ■ □□□□ ■
□□□□□□ ■■■ □□□ □ ■ □□□□ ■■■ □□□ ■ □□□ ■ □ ■ □□□□ ■
□□□□□ ■■■■■ □□ □ ■ □□□□□□□ ■ □□ ■ □□ ■ □□ ■ □□ ■ □ ■
■ □□□ ■■■■■■■ □ □ ■ □□□□□□□□ ■ □ ■ □ ■ □□□□ ■■■ □ ■
■■ □□□ ■■■■■ □□ □ ■ □□□□□□□□□ ■ ■ □□□□□□□□□□ ■
■■■ □□□ ■■■ □□□ □ ■ □□ ■ □□□□□□ ■ ■ □□□□□□□□□□ ■
■■■■ □□□ ■ □□□□ □ ■ □□ ■ □□□□□ ■ □ ■■■■■■■■■■■■
□□□□□□□□□□□□ ■■■ □□ ■■■■■ □□ ■ □□□□□□□□□□ ■




Input

The input consists of multiple datasets. One plan view is given for each dataset. A plan view is represented by 12 rows of 12 number columns, with black squares represented by 1 and white squares represented by 0. The datasets are separated by a single blank line.

The number of datasets does not exceed 20.

Output

Outputs the number of islands on one line for each dataset.

Example

Input

111100001111
111000001111
110000001111
100000001111
000100010000
000000111000
000001111100
100011111110
110001111100
111000111000
111100010000
000000000000

010001111100
110010000010
010010000001
010000000001
010000000110
010000111000
010000000100
010000000010
010000000001
010010000001
010010000010
111001111100

000000000000
111111111111
100010100001
100010100001
100010100001
100010100001
100100100101
101000011101
100000000001
100000000001
111111111111
100000000001


Output

5
13
4
"""

def count_islands(grid):
    def dfs(x, y):
        if 0 <= x < 12 and 0 <= y < 12 and grid[y][x] == '1':
            grid[y][x] = '0'
            for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(x + dx, y + dy)

    island_count = 0
    for i in range(12):
        for j in range(12):
            if grid[j][i] == '1':
                island_count += 1
                dfs(i, j)
    
    return island_count