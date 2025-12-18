"""
QUESTION:
Sarthak got an empty magic grid of size N \times N on his birthday. The grid can only be filled with positive integers such that the [bitwise XOR] of all numbers from any row, any column, or any of the two main diagonals must all be the same! Can you help Sarthak fill this grid using only positive integers no more than 10^{9}?

------ Input Format ------ 

- The first line of each input contains T - the number of test cases. The test cases then follow.
- The only line of each test case contains an integer N - the size of the grid.

------ Output Format ------ 

For each test case, output N lines, each containing N space-separated integers, such that the grid satisfies the condition given in the statement.

Each integer should be positive and ≤ 10^{9}.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ N ≤ 100$

----- Sample Input 1 ------ 
1
3
----- Sample Output 1 ------ 
1 1 1
1 1 1
1 1 1

----- explanation 1 ------ 
The bitwise XOR of all rows, columns and main diagonals in the grid is $1$. Therefore, this satisfies the condition.
"""

def generate_magic_grids(T, N):
    """
    Generates magic grids for given test cases.

    Parameters:
    - T (int): The number of test cases.
    - N (list of int): A list of integers where each integer represents the size of the grid for each test case.

    Returns:
    - list of list of list of int: A list where each element is a 2D list representing the magic grid for a test case.
    """
    results = []
    for n in N:
        grid = [['1'] * n for _ in range(n)]
        results.append(grid)
    return results