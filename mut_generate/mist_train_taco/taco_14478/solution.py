"""
QUESTION:
Find the number of sequences of length K consisting of positive integers such that the product of any two adjacent elements is at most N, modulo 10^9+7.

-----Constraints-----
 - 1\leq N\leq 10^9
 - 1 2\leq K\leq 100 (fixed at 21:33 JST)
 - N and K are integers.

-----Input-----
Input is given from Standard Input in the following format:
N K

-----Output-----
Print the number of sequences, modulo 10^9+7.

-----Sample Input-----
3 2

-----Sample Output-----
5

(1,1), (1,2), (1,3), (2,1), and (3,1) satisfy the condition.
"""

def count_sequences(N: int, K: int) -> int:
    mod = 10 ** 9 + 7
    
    # Generate the data list
    data = [i for i in range(1, int(N ** 0.5) + 1)] + [N // i for i in range(int(N ** 0.5), 0, -1)]
    L = len(data)
    
    # Initialize the dp array
    dp = [1] * L
    for i in range(1, L):
        dp[i] = data[i] - data[i - 1]
    
    # Update the dp array for k-1 times
    for _ in range(K - 1):
        h = dp[:]
        for i in range(1, L):
            h[i] = (h[i] + h[i - 1]) % mod
        h = h[::-1]
        for i in range(1, L):
            h[i] = h[i] * (data[i] - data[i - 1]) % mod
        dp = h
    
    # Calculate the final answer
    ans = 0
    for u in dp:
        ans = (ans + u) % mod
    
    return ans