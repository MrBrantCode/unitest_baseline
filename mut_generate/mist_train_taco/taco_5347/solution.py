"""
QUESTION:
Let us consider a grid of squares with N rows and N columns. You want to put some domino pieces on this grid. Each domino piece covers two squares that have a common side. Each square can be covered by at most one piece.

For each row of the grid, let's define its quality as the number of domino pieces that cover at least one square in this row. We define the quality of each column similarly.

Find a way to put at least one domino piece on the grid so that the quality of every row is equal to the quality of every column, or determine that such a placement doesn't exist.

Constraints

* 2 \le N \le 1000

Input

Input is given from Standard Input in the following format:


N


Output

If the required domino placement doesn't exist, print a single integer `-1`.

Otherwise, output your placement as N strings of N characters each. If a square is not covered, the corresponding character must be `.` (a dot). Otherwise, it must contain a lowercase English letter. Squares covered by the same domino piece must contain the same letter. If two squares have a common side but belong to different pieces, they must contain different letters.

Examples

Input

6


Output

aabb..
b..zz.
ba....
.a..aa
..a..b
..a..b


Input

2


Output

-1
"""

def find_domino_placement(N):
    """
    Finds a way to place domino pieces on an NxN grid such that the quality of every row is equal to the quality of every column,
    or determines that such a placement doesn't exist.

    Parameters:
    N (int): The size of the grid (N x N).

    Returns:
    list of str: A list of N strings representing the grid configuration if a valid placement exists.
                Returns `-1` if no such placement is possible.
    """
    if N == 2:
        return -1
    
    s3 = ['abb', 'a.d', 'ccd']
    s = [
        ['abcc', 'abdd', 'ddba', 'ccba'],
        ['dccdd', 'daa.c', 'c..bc', 'c..bd', 'ddccd'],
        ['abbc..', 'a.ac..', 'bba.cc', 'a..aab', 'a..b.b', '.aabaa'],
        ['aba....', 'aba....', 'bab....', 'bab....', 'a..bbaa', 'a..aabb', '.aabbaa']
    ]
    
    if N == 3:
        return s3
    
    (d, m) = divmod(N, 4)
    d -= 1
    m += 4
    
    result = []
    for i in range(d):
        result.extend(['.' * 4 * i + x + '.' * (4 * (d - i - 1) + m) for x in s[0]])
    
    result.extend(['.' * 4 * d + x for x in s[m - 4]])
    
    return result