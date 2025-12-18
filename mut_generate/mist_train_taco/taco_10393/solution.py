"""
QUESTION:
There are N squares arranged in a row from left to right.
The height of the i-th square from the left is H_i.
You will land on a square of your choice, then repeat moving to the adjacent square on the right as long as the height of the next square is not greater than that of the current square.
Find the maximum number of times you can move.

-----Constraints-----
 - All values in input are integers.
 - 1 \leq N \leq 10^5
 - 1 \leq H_i \leq 10^9

-----Input-----
Input is given from Standard Input in the following format:
N
H_1 H_2 ... H_N

-----Output-----
Print the maximum number of times you can move.

-----Sample Input-----
5
10 4 8 7 3

-----Sample Output-----
2

By landing on the third square from the left, you can move to the right twice.
"""

def max_right_moves(N: int, H: list) -> int:
    """
    Calculate the maximum number of times you can move to the right in a row of squares
    where the height of the next square is not greater than that of the current square.

    Parameters:
    N (int): The number of squares.
    H (list): A list of integers representing the height of each square.

    Returns:
    int: The maximum number of times you can move to the right.
    """
    ans = 0
    x = 0
    for i in range(N - 1):
        if H[i] >= H[i + 1]:
            x += 1
            ans = max(ans, x)
        else:
            x = 0
    return ans