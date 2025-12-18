"""
QUESTION:
You are given a permutation p_1,p_2,...,p_N consisting of 1,2,..,N.
You can perform the following operation any number of times (possibly zero):
Operation: Swap two adjacent elements in the permutation.
You want to have p_i ≠ i for all 1≤i≤N.
Find the minimum required number of operations to achieve this.

-----Constraints-----
 - 2≤N≤10^5
 - p_1,p_2,..,p_N is a permutation of 1,2,..,N.

-----Input-----
The input is given from Standard Input in the following format:
N
p_1 p_2 .. p_N

-----Output-----
Print the minimum required number of operations

-----Sample Input-----
5
1 4 3 5 2

-----Sample Output-----
2

Swap 1 and 4, then swap 1 and 3. p is now 4,3,1,5,2 and satisfies the condition.
This is the minimum possible number, so the answer is 2.
"""

def minimum_operations_to_avoid_identity(N, p):
    """
    Calculate the minimum number of adjacent swaps required to ensure that no element
    in the permutation p is in its original position.

    Parameters:
    N (int): The length of the permutation.
    p (list of int): The permutation list.

    Returns:
    int: The minimum number of adjacent swaps required.
    """
    cnt = 0
    for i in range(N - 1):
        if p[i] == i + 1:
            cnt += 1
            p[i + 1] = i + 1
    if p[N - 1] == N:
        cnt += 1
    return cnt