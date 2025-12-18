"""
QUESTION:
Find the total number of Squares in a N*N chessboard.
 
Example 1:
Input:
N = 1
Output:
1
Explanation:
A 1*1 chessboard has only 1 square.
Example 2:
Input:
N = 2
Output:
5
Explanation:
A 2*2 chessboard has 5 squares.
4 1*1 squares and a 2*2 square.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function squaresInChessBoard() which takes an Integer N as input and returns the number of squares in a N*N chessboard.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{5}
"""

def squares_in_chessboard(N: int) -> int:
    """
    Calculate the total number of squares in an N*N chessboard.

    Parameters:
    N (int): The size of the N*N chessboard.

    Returns:
    int: The total number of squares in the N*N chessboard.
    """
    return N * (N + 1) * (2 * N + 1) // 6