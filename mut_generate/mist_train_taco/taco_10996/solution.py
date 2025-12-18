"""
QUESTION:
Find total number of Rectangles (excluding squares) in a N*N chessboard.7
Example 1:
Input:
N = 1
Output:
0
Explanation:
There is only 1 square on a 1*1 chess
board. There are no Proper Rectangles.
Example 2:
Input:
N = 2
Output:
4
Explanation:
There are 4 rectangles in a 2*2 chessboard.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function rectanglesInChessBoard() which takes an Integer N as input and returns the number of rectangles in a N*N chess board.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{4}
"""

def rectanglesInChessBoard(N: int) -> int:
    """
    Calculate the total number of rectangles (excluding squares) in an N*N chessboard.

    Parameters:
    N (int): The size of the N*N chessboard.

    Returns:
    int: The total number of rectangles (excluding squares) in the N*N chessboard.
    """
    return (N * (N + 1) // 2) ** 2 - N * (N + 1) * (2 * N + 1) // 6