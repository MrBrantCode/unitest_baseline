"""
QUESTION:
Takahashi had a pair of two positive integers not exceeding N, (a,b), which he has forgotten.
He remembers that the remainder of a divided by b was greater than or equal to K.
Find the number of possible pairs that he may have had.

-----Constraints-----
 - 1 \leq N \leq 10^5
 - 0 \leq K \leq N-1
 - All input values are integers.

-----Input-----
Input is given from Standard Input in the following format:
N K

-----Output-----
Print the number of possible pairs that he may have had.

-----Sample Input-----
5 2

-----Sample Output-----
7

There are seven possible pairs: (2,3),(5,3),(2,4),(3,4),(2,5),(3,5) and (4,5).
"""

def count_pairs_with_remainder_greater_than_k(N: int, K: int) -> int:
    """
    Counts the number of pairs (a, b) such that 1 <= a, b <= N and the remainder of a divided by b is greater than or equal to K.

    Parameters:
    - N (int): The maximum value for a and b.
    - K (int): The minimum remainder value.

    Returns:
    - int: The number of valid pairs (a, b).
    """
    ans = 0
    if K == 0:
        return N ** 2
    
    for r in range(K, N):
        for q in range((N - r) // (r + 1) + 1):
            if q == 0:
                ans += N - r
            else:
                ans += max(0, (N - r) // q - r)
    
    return ans