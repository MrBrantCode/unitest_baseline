"""
QUESTION:
Square1001 has seen an electric bulletin board displaying the integer 1.
He can perform the following operations A and B to change this value:
 - Operation A: The displayed value is doubled.
 - Operation B: The displayed value increases by K.
Square1001 needs to perform these operations N times in total.
Find the minimum possible value displayed in the board after N operations.

-----Constraints-----
 - 1 \leq N, K \leq 10
 - All input values are integers.

-----Input-----
Input is given from Standard Input in the following format:
N
K

-----Output-----
Print the minimum possible value displayed in the board after N operations.

-----Sample Input-----
4
3

-----Sample Output-----
10

The value will be minimized when the operations are performed in the following order: A, A, B, B.

In this case, the value will change as follows: 1 → 2 → 4 → 7 → 10.
"""

def find_minimum_value_after_operations(N: int, K: int) -> int:
    """
    Calculate the minimum possible value displayed on the board after N operations,
    given that each operation can either double the current value (Operation A)
    or increase it by K (Operation B).

    Parameters:
    N (int): The total number of operations to perform.
    K (int): The increment value for Operation B.

    Returns:
    int: The minimum possible value displayed on the board after N operations.
    """
    value = 1
    for _ in range(N):
        value += min(value, K)
    return value