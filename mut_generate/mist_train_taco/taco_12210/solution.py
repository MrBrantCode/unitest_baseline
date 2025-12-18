"""
QUESTION:
Read problem statements in [Mandarin Chinese] and [Bengali].

Given n (n is even), determine the number of black cells in an n \times n chessboard. 

------ Input Format ------ 

The only line of the input contains a single integer n.

------ Output Format ------ 

Output the number of black cells in an n \times n chessboard.

------ Constraints ------ 

$2 ≤ n ≤ 100$
$n$ is even

----- Sample Input 1 ------ 
8
----- Sample Output 1 ------ 
32
----- explanation 1 ------ 

There are $32$ black cells and $32$ white cells in an $8 \times 8$ chessboard. So the answer is $32$.
"""

def count_black_cells(n: int) -> int:
    """
    Calculate the number of black cells in an n x n chessboard.

    Parameters:
    n (int): The size of the chessboard (n x n).

    Returns:
    int: The number of black cells in the chessboard.
    """
    return pow(n, 2) // 2