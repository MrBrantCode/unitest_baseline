"""
QUESTION:
There is a plane like Figure 1 with 8 vertical and 8 horizontal squares.
□ | □ | □ | □ | □ | □ | □ | □
--- | --- | --- | --- | --- | --- | --- | ---
□ | □ | □ | □ | □ | □ | □ | □
□ | □ | □ | □ | □ | □ | □ | □
□ | □ | □ | □ | □ | □ | □ | □
□ | □ | □ | □ | □ | □ | □ | □
□ | □ | □ | □ | □ | □ | □ | □
□ | □ | □ | □ | □ | □ | □ | □
□ | □ | □ | □ | □ | □ | □ | □

Figure 1
---



Only one of the following A to G shapes is placed on this plane.

| A
---
■| ■| |
--- | --- | --- | ---
■| ■| |
| | |
| | |
| B
---
| ■| |
--- | --- | --- | ---
| ■| |
| ■| |
| ■| |
| C
---
■| ■| ■| ■
--- | --- | --- | ---
| | |
| | |
| | |

| D
---
| ■| |
--- | --- | --- | ---
■| ■| |
■ | | |
| | |
| E
---
■| ■| |
--- | --- | --- | ---
| ■| ■|
| | |
| | |
| F
---
■ | | |
--- | --- | --- | ---
■| ■| |
| ■| |
| | |
| G
---
| ■| ■|
--- | --- | --- | ---
■| ■| |
| | |
| | |



For example, in the example in Figure 2 below, the shape E is placed.
| □ | □ | □ | □ | □ | □ | □ | □
--- | --- | --- | --- | --- | --- | --- | ---
□ | □ | □ | □ | □ | □ | □ | □
□ | ■| ■| □ | □ | □ | □ | □
□ | □ | ■| ■| □ | □ | □ | □
□ | □ | □ | □ | □ | □ | □ | □
□ | □ | □ | □ | □ | □ | □ | □
□ | □ | □ | □ | □ | □ | □ | □
□ | □ | □ | □ | □ | □ | □ | □

Figure 2
---



Create a program that reads a sequence of numbers that expresses the squares occupied by figures by 1 and the cells that do not occupy 0 in the plane, and outputs the types (A to G) of the placed figures. ..

However, there is always one figure placed on one plane, and multiple figures cannot be placed. In addition, there is nothing other than the figures represented by A to G.



Input

The input consists of multiple datasets.

One dataset is given eight strings of eight characters, with the squares occupied by the shape in the plane represented by 1 and the squares not occupied by 0 represented by 0. For example, the sequence of strings corresponding to Figure 2 is as follows:

| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
--- | --- | --- | --- | --- | --- | --- | ---
0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
0 | 1 | 1 | 0 | 0 | 0 | 0 | 0
0 | 0 | 1 | 1 | 0 | 0 | 0 | 0
0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
0 | 0 | 0 | 0 | 0 | 0 | 0 | 0
0 | 0 | 0 | 0 | 0 | 0 | 0 | 0



The datasets are separated by a single blank line. The number of datasets does not exceed 50.

Output

For each data set, output the type of figure (any of A to G) given to the plane on one line.

Example

Input

00000000
00000000
01100000
00110000
00000000
00000000
00000000
00000000

00011110
00000000
00000000
00000000
00000000
00000000
00000000
00000000

00000000
00000000
00110000
00110000
00000000
00000000
00000000
00000000


Output

E
C
A
"""

def identify_shape(grid: list[str]) -> str:
    """
    Identifies the type of shape (A to G) placed on a 8x8 grid.

    Parameters:
    grid (list[str]): A list of 8 strings, each representing a row in the 8x8 grid.
                      Each character in the string is either '0' (empty) or '1' (occupied).

    Returns:
    str: The type of shape (A to G) placed on the grid.
    """
    B = [771, 16843009, 15, 66306, 1539, 131841, 774]
    C = 'ABCDEFG'
    N = 8
    su = 0

    for i in range(N):
        for j in range(N):
            if grid[i][j] == '1':
                su |= 1 << (i * N + j)

    for i in range(N * N):
        for k in range(7):
            b = B[k] << i
            if su & b == b:
                return C[k]

    return ""