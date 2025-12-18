"""
QUESTION:
There is a rectangular grid of n rows of m initially-white cells each.

Arkady performed a certain number (possibly zero) of operations on it. In the i-th operation, a non-empty subset of rows R_{i} and a non-empty subset of columns C_{i} are chosen. For each row r in R_{i} and each column c in C_{i}, the intersection of row r and column c is coloured black.

There's another constraint: a row or a column can only be chosen at most once among all operations. In other words, it means that no pair of (i, j) (i < j) exists such that $R_{i} \cap R_{j} \neq \varnothing$ or $C_{i} \cap C_{j} \neq \varnothing$, where [Image] denotes intersection of sets, and $\varnothing$ denotes the empty set.

You are to determine whether a valid sequence of operations exists that produces a given final grid.


-----Input-----

The first line contains two space-separated integers n and m (1 ≤ n, m ≤ 50) — the number of rows and columns of the grid, respectively.

Each of the following n lines contains a string of m characters, each being either '.' (denoting a white cell) or '#' (denoting a black cell), representing the desired setup.


-----Output-----

If the given grid can be achieved by any valid sequence of operations, output "Yes"; otherwise output "No" (both without quotes).

You can print each character in any case (upper or lower).


-----Examples-----
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



-----Note-----

For the first example, the desired setup can be produced by 3 operations, as is shown below.

 [Image] 

For the second example, the desired setup cannot be produced, since in order to colour the center row, the third row and all columns must be selected in one operation, but after that no column can be selected again, hence it won't be possible to colour the other cells in the center column.
"""

def can_achieve_grid(n: int, m: int, grid: list[str]) -> bool:
    """
    Determines whether a given grid can be achieved by a valid sequence of operations.

    Parameters:
    - n (int): The number of rows in the grid.
    - m (int): The number of columns in the grid.
    - grid (list[str]): A list of strings where each string represents a row in the grid.
                        Each character in the string is either '.' (white) or '#' (black).

    Returns:
    - bool: True if the grid can be achieved by a valid sequence of operations, False otherwise.
    """
    # Convert each row into a set of column indices that contain '#'
    row_sets = [{i for i, c in enumerate(row) if c == '#'} for row in grid]
    processed_sets = []

    for row_set in row_sets:
        if row_set:
            for processed_set in processed_sets:
                intersection = row_set & processed_set
                if intersection and row_set != processed_set:
                    return False
            processed_sets.append(row_set)
    
    return True