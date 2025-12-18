"""
QUESTION:
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.
(Note that backslash characters are escaped, so a \ is represented as "\\".)
Return the number of regions.
 













Example 1:
Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:



Example 2:
Input:
[
  " /",
  "  "
]
Output: 1
Explanation: The 2x2 grid is as follows:



Example 3:
Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:



Example 4:
Input:
[
  "/\\",
  "\\/"
]
Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
The 2x2 grid is as follows:



Example 5:
Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:


 
Note:

1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.
"""

def count_regions_by_slashes(grid):
    def convert_grid(grid):
        new_grid = [[0] * len(grid[0]) * 2 for _ in range(len(grid) * 2)]
        for (x, y, v) in ((x, y, v) for y in range(len(grid)) for (x, v) in enumerate(grid[y]) if v in '\\\\/'):
            new_grid[y * 2 + 0][x * 2 + (1 if v == '/' else 0)] = v
            new_grid[y * 2 + 1][x * 2 + (0 if v == '/' else 1)] = v
        return new_grid

    def destroy_island(x, y, grid):
        grid[y][x] = 1
        for c in search(x, y, grid):
            destroy_island(c[0], c[1], grid)

    def search(x, y, grid):
        in_bounds = lambda c: 0 <= c[1] < len(grid) and 0 <= c[0] < len(grid[c[1]])
        check_orthog = lambda c: in_bounds(c) and grid[c[1]][c[0]] == 0

        def check_diag(c):
            if not in_bounds(c) or grid[c[1]][c[0]] != 0:
                return False
            (d_x, d_y) = (c[0] - x, c[1] - y)
            sep = '\\\\' if d_x > 0 > d_y or d_x < 0 < d_y else '/'
            return not (grid[y + d_y][x] == sep and grid[y][x + d_x] == sep)
        
        yield from chain(filter(check_orthog, ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))), filter(check_diag, ((x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1))))

    grid = convert_grid(grid)
    return len([destroy_island(x, y, grid) for y in range(len(grid)) for (x, v) in enumerate(grid[y]) if v == 0])