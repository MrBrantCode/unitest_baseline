"""
QUESTION:
Given are integers N and K.
How many quadruples of integers (a,b,c,d) satisfy both of the following conditions?
 - 1 \leq a,b,c,d \leq N
 - a+b-c-d=K

-----Constraints-----
 - 1 \leq N \leq 10^5
 - -2(N-1) \leq K \leq 2(N-1)
 - All numbers in input are integers.

-----Input-----
Input is given from standard input in the following format:
N K

-----Output-----
Print the answer.

-----Sample Input-----
2 1

-----Sample Output-----
4

Four quadruples below satisfy the conditions:
 - (a,b,c,d)=(2,1,1,1)
 - (a,b,c,d)=(1,2,1,1)
 - (a,b,c,d)=(2,2,2,1)
 - (a,b,c,d)=(2,2,1,2)
"""

def count_quadruples(N: int, K: int) -> int:
    """
    Counts the number of quadruples (a, b, c, d) that satisfy the conditions:
    - 1 <= a, b, c, d <= N
    - a + b - c - d = K

    Parameters:
    - N (int): The upper limit for a, b, c, and d.
    - K (int): The target difference.

    Returns:
    - int: The number of valid quadruples.
    """
    
    def num_pair(m):
        if m <= N:
            return m - 1
        return 2 * N - m + 1
    
    K = abs(K)
    ans = 0
    for i in range(K + 2, 2 * N + 1):
        ans += num_pair(i) * num_pair(i - K)
    
    return ans