"""
QUESTION:
Snuke has decided to play with N cards and a deque (that is, a double-ended queue).
Each card shows an integer from 1 through N, and the deque is initially empty.
Snuke will insert the cards at the beginning or the end of the deque one at a time, in order from 1 to N.
Then, he will perform the following action N times: take out the card from the beginning or the end of the deque and eat it.
Afterwards, we will construct an integer sequence by arranging the integers written on the eaten cards, in the order they are eaten. Among the sequences that can be obtained in this way, find the number of the sequences such that the K-th element is 1. Print the answer modulo 10^{9} + 7.

-----Constraints-----
 - 1 ≦ K ≦ N ≦ 2{,}000

-----Input-----
The input is given from Standard Input in the following format:
N K

-----Output-----
Print the answer modulo 10^{9} + 7.

-----Sample Input-----
2 1

-----Sample Output-----
1

There is one sequence satisfying the condition: 1,2. One possible way to obtain this sequence is the following:
 - Insert both cards, 1 and 2, at the end of the deque.
 - Eat the card at the beginning of the deque twice.
"""

def count_sequences_with_one_at_k(N: int, K: int) -> int:
    mod = 1000000007
    
    if K == 1:
        if N == 1:
            return 1
        else:
            return pow(2, N - 2, mod)
    
    dp = [[0] * (N + 1) for _ in range(K - 1)]
    
    for j in range(2, N + 1):
        dp[0][j] = 1
    
    for i in range(1, K - 1):
        cs = [0] * (N + 1)
        for j in range(1, N + 1):
            cs[j] = (cs[j - 1] + dp[i - 1][j]) % mod
        for j in range(2, N + 1):
            if j != N - i + 1:
                dp[i][j] = (dp[i][j] + dp[i - 1][j]) % mod
            dp[i][j] = (dp[i][j] + cs[-1] - cs[j]) % mod
    
    ans = 0
    for j in range(2, N + 1):
        ans = (ans + dp[-1][j]) % mod
    
    if K != N:
        ans = ans * pow(2, N - K - 1, mod) % mod
    
    return ans