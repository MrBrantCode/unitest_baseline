"""
QUESTION:
For an integer N, we will choose a permutation \{P_1, P_2, ..., P_N\} of \{1, 2, ..., N\}.
Then, for each i=1,2,...,N, let M_i be the remainder when i is divided by P_i.
Find the maximum possible value of M_1 + M_2 + \cdots + M_N.

-----Constraints-----
 - N is an integer satisfying 1 \leq N \leq 10^9.

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print the maximum possible value of M_1 + M_2 + \cdots + M_N.

-----Sample Input-----
2

-----Sample Output-----
1

When the permutation \{P_1, P_2\} = \{2, 1\} is chosen, M_1 + M_2 = 1 + 0 = 1.
"""

def calculate_max_remainder_sum(N: int) -> int:
    """
    Calculate the maximum possible value of the sum of remainders M_1 + M_2 + ... + M_N
    for a permutation {P_1, P_2, ..., P_N} of {1, 2, ..., N}.

    Parameters:
    N (int): The upper limit of the permutation range.

    Returns:
    int: The maximum possible value of the sum of remainders.
    """
    return N * (N - 1) // 2