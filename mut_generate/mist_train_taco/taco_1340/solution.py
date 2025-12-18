"""
QUESTION:
Find the number of integers between 1 and N (inclusive) that contains exactly K non-zero digits when written in base ten.

-----Constraints-----
 - 1 \leq N < 10^{100}
 - 1 \leq K \leq 3

-----Input-----
Input is given from Standard Input in the following format:
N
K

-----Output-----
Print the count.

-----Sample Input-----
100
1

-----Sample Output-----
19

The following 19 integers satisfy the condition:
 - 1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100
"""

def count_integers_with_k_non_zero_digits(N: str, K: int) -> int:
    """
    Counts the number of integers between 1 and N (inclusive) that contain exactly K non-zero digits.

    Parameters:
    - N (str): The upper limit as a string (since it can be very large).
    - K (int): The number of non-zero digits required.

    Returns:
    - int: The count of such integers.
    """
    S = N
    N_len = len(S)
    dp = [[[0 for _ in range(2)] for _ in range(K + 1)] for _ in range(N_len + 1)]
    dp[0][0][0] = 1
    
    for i in range(N_len):
        for j in range(K + 1):
            for k in range(2):
                nd = int(S[i])
                for d in range(10):
                    (ni, nj, nk) = (i + 1, j, k)
                    if d != 0:
                        nj += 1
                    if nj > K:
                        continue
                    if k == 0:
                        if d > nd:
                            continue
                        if d < nd:
                            nk += 1
                    dp[ni][nj][nk] += dp[i][j][k]
    
    return dp[N_len][K][0] + dp[N_len][K][1]