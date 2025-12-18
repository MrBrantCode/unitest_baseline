"""
QUESTION:
Alice has a grid with $2$ rows and $n$ columns. She fully covers the grid using $n$ dominoes of size $1 \times 2$ — Alice may place them vertically or horizontally, and each cell should be covered by exactly one domino.

Now, she decided to show one row of the grid to Bob. Help Bob and figure out what the other row of the grid looks like!


-----Input-----

The input consists of multiple test cases. The first line contains an integer $t$ ($1 \leq t \leq 5000$) — the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer $n$ ($1 \leq n \leq 100$) — the width of the grid.

The second line of each test case contains a string $s$ consisting of $n$ characters, each of which is either L, R, U, or D, representing the left, right, top, or bottom half of a domino, respectively (see notes for better understanding). This string represents one of the rows of the grid.

Additional constraint on the input: each input corresponds to at least one valid tiling.


-----Output-----

For each test case, output one string — the other row of the grid, using the same format as the input string. If there are multiple answers, print any.


-----Examples-----

Input
4
1
U
2
LR
5
LRDLR
6
UUUUUU
Output
D
LR
LRULR
DDDDDD


-----Note-----

In the first test case, Alice shows Bob the top row, the whole grid may look like:

In the second test case, Alice shows Bob the bottom row, the whole grid may look like:

In the third test case, Alice shows Bob the bottom row, the whole grid may look like:

In the fourth test case, Alice shows Bob the top row, the whole grid may look like:
"""

def reconstruct_other_row(t, test_cases):
    """
    Reconstructs the other row of a grid covered by 1x2 dominoes based on one shown row.

    Parameters:
    t (int): The number of test cases.
    test_cases (list of tuples): A list where each tuple contains an integer n (width of the grid) and a string s (one row of the grid).

    Returns:
    list of str: A list of strings where each string represents the other row of the grid for each corresponding test case.
    """
    result = []
    for n, s in test_cases:
        other_row = []
        for char in s:
            if char == 'U':
                other_row.append('D')
            elif char == 'D':
                other_row.append('U')
            elif char == 'L':
                other_row.append('L')
            elif char == 'R':
                other_row.append('R')
        result.append(''.join(other_row))
    return result