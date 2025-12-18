"""
QUESTION:
Given is a permutation P_1, \ldots, P_N of 1, \ldots, N.
Find the number of integers i (1 \leq i \leq N) that satisfy the following condition:  
 - For any integer j (1 \leq j \leq i), P_i \leq P_j.

-----Constraints-----
 - 1 \leq N \leq 2 \times 10^5
 - P_1, \ldots, P_N is a permutation of 1, \ldots, N.  
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N
P_1 ... P_N

-----Output-----
Print the number of integers i that satisfy the condition.

-----Sample Input-----
5
4 2 5 1 3

-----Sample Output-----
3

i=1, 2, and 4 satisfy the condition, but i=3 does not - for example, P_i > P_j holds for j = 1.

Similarly, i=5 does not satisfy the condition, either. Thus, there are three integers that satisfy the condition.
"""

def count_valid_positions(N, P):
    """
    Counts the number of integers i (1 ≤ i ≤ N) that satisfy the condition:
    For any integer j (1 ≤ j ≤ i), P_i ≤ P_j.

    Parameters:
    N (int): The length of the permutation list.
    P (list of int): The permutation list of integers from 1 to N.

    Returns:
    int: The number of integers i that satisfy the condition.
    """
    ans = 0
    m = P[0]
    for i in range(N):
        m = min(m, P[i])
        if m == P[i]:
            ans += 1
    return ans