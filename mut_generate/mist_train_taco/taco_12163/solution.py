"""
QUESTION:
As a token of his gratitude, Takahashi has decided to give his mother an integer sequence.
The sequence A needs to satisfy the conditions below:
 - A consists of integers between X and Y (inclusive).
 - For each 1\leq i \leq |A|-1, A_{i+1} is a multiple of A_i and strictly greater than A_i.
Find the maximum possible length of the sequence.

-----Constraints-----
 - 1 \leq X \leq Y \leq 10^{18}
 - All input values are integers.

-----Input-----
Input is given from Standard Input in the following format:
X Y

-----Output-----
Print the maximum possible length of the sequence.

-----Sample Input-----
3 20

-----Sample Output-----
3

The sequence 3,6,18 satisfies the conditions.
"""

def max_sequence_length(X: int, Y: int) -> int:
    """
    Calculate the maximum possible length of a sequence A where:
    - A consists of integers between X and Y (inclusive).
    - For each 1 ≤ i ≤ |A|-1, A_{i+1} is a multiple of A_i and strictly greater than A_i.

    Parameters:
    - X (int): The lower bound of the integer sequence (inclusive).
    - Y (int): The upper bound of the integer sequence (inclusive).

    Returns:
    - int: The maximum possible length of the sequence.
    """
    for t in range(1, 100):
        if 2 ** (t - 1) * X <= Y:
            out = t
        else:
            break
    return out