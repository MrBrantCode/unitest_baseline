"""
QUESTION:
There is a rectangular grid of n rows of m initially-white cells each.

Arkady performed a certain number (possibly zero) of operations on it. In the i-th operation, a non-empty subset of rows Ri and a non-empty subset of columns Ci are chosen. For each row r in Ri and each column c in Ci, the intersection of row r and column c is coloured black.

There's another constraint: a row or a column can only be chosen at most once among all operations. In other words, it means that no pair of (i, j) (i < j) exists such that <image> or <image>, where <image> denotes intersection of sets, and <image> denotes the empty set.

You are to determine whether a valid sequence of operations exists that produces a given final grid.

Input

The first line contains two space-separated integers n and m (1 ≤ n, m ≤ 50) — the number of rows and columns of the grid, respectively.

Each of the following n lines contains a string of m characters, each being either '.' (denoting a white cell) or '#' (denoting a black cell), representing the desired setup.

Output

If the given grid can be achieved by any valid sequence of operations, output "Yes"; otherwise output "No" (both without quotes).

You can print each character in any case (upper or lower).

Examples

Input

5 8
.#.#..#.
.....#..
.#.#..#.
#.#....#
.....#..


Output

Yes


Input

5 5
..#..
..#..
#####
..#..
..#..


Output

No


Input

5 9
........#
#........
..##.#...
.......#.
....#.#.#


Output

No

Note

For the first example, the desired setup can be produced by 3 operations, as is shown below.

<image>

For the second example, the desired setup cannot be produced, since in order to colour the center row, the third row and all columns must be selected in one operation, but after that no column can be selected again, hence it won't be possible to colour the other cells in the center column.
"""

def can_achieve_grid(n: int, m: int, grid: list) -> str:
    def findInArray(c, arr):
        ind = []
        for i in range(len(arr)):
            if arr[i] == c:
                ind.append(i)
        return ind

    rows = [0] * n
    cols = [0] * m
    counter = 1

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                if rows[i] == 0 and cols[j] == 0:
                    rows[i] = counter
                    cols[j] = counter
                    counter += 1
                else:
                    if (rows[i] != 0 and cols[j] != 0) and rows[i] != cols[j]:
                        return 'No'
                    c = max(rows[i], cols[j])
                    rows[i] = c
                    cols[j] = c

    for c in range(1, counter):
        rowsEqualToC = findInArray(c, rows)
        colsEqualToC = findInArray(c, cols)
        for i in rowsEqualToC:
            for j in colsEqualToC:
                if grid[i][j] != '#':
                    return 'No'

    return 'Yes'