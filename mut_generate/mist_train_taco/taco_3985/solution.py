"""
QUESTION:
Takahashi has many red balls and blue balls. Now, he will place them in a row.
Initially, there is no ball placed.
Takahashi, who is very patient, will do the following operation 10^{100} times:
 - Place A blue balls at the end of the row of balls already placed. Then, place B red balls at the end of the row.
How many blue balls will be there among the first N balls in the row of balls made this way?

-----Constraints-----
 - 1 \leq N \leq 10^{18}
 - A, B \geq 0
 - 0 < A + B \leq 10^{18}
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N A B

-----Output-----
Print the number of blue balls that will be there among the first N balls in the row of balls.

-----Sample Input-----
8 3 4

-----Sample Output-----
4

Let b denote a blue ball, and r denote a red ball. The first eight balls in the row will be bbbrrrrb, among which there are four blue balls.
"""

def count_blue_balls(N: int, A: int, B: int) -> int:
    """
    Calculate the number of blue balls among the first N balls in a row where balls are placed in cycles of A blue balls followed by B red balls.

    Parameters:
    - N (int): The number of balls to consider from the beginning of the row.
    - A (int): The number of blue balls placed in each cycle.
    - B (int): The number of red balls placed in each cycle.

    Returns:
    - int: The number of blue balls among the first N balls.
    """
    m = N // (A + B)
    return m * A + min(A, N - m * (A + B))