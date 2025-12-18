"""
QUESTION:
The beauty of a sequence a of length n is defined as a_1 \oplus \cdots \oplus a_n, where \oplus denotes the bitwise exclusive or (XOR).

You are given a sequence A of length N. Snuke will insert zero or more partitions in A to divide it into some number of non-empty contiguous subsequences.

There are 2^{N-1} possible ways to insert partitions. How many of them divide A into sequences whose beauties are all equal? Find this count modulo 10^{9}+7.

Constraints

* All values in input are integers.
* 1 \leq N \leq 5 \times 10^5
* 0 \leq A_i < 2^{20}

Input

Input is given from Standard Input in the following format:


N
A_1 A_2 \ldots A_{N}


Output

Print the answer.

Examples

Input

3
1 2 3


Output

3


Input

3
1 2 2


Output

1


Input

32
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0


Output

147483634


Input

24
1 2 5 3 3 6 1 1 8 8 0 3 3 4 6 6 4 0 7 2 5 4 6 2


Output

292
"""

def count_equal_beauty_partitions(N, A):
    mod = 10**9 + 7
    
    # Calculate the prefix XOR array
    b = [0] * N
    b[0] = A[0]
    for n in range(1, N):
        b[n] = A[n] ^ b[n - 1]
    
    # Find the maximum value in the prefix XOR array
    m = max(b)
    
    # Initialize dp arrays
    dp = [[0] * (m + 1) for _ in range(2)]
    dp[0] = [1] * (m + 1)
    
    cnt = [0] * (m + 1)
    z = 0
    
    for i in range(N):
        if b[i] == 0:
            z += 1
        dp[0][b[i]] += dp[1][b[i]] * (z - cnt[b[i]])
        dp[0][b[i]] %= mod
        dp[1][b[i]] += dp[0][b[i]]
        dp[1][b[i]] %= mod
        cnt[b[i]] = z
    
    if b[N - 1] != 0:
        return dp[0][b[N - 1]]
    else:
        ans = pow(2, z - 1, mod)
        for i in range(1, m + 1):
            ans += dp[1][i]
            ans %= mod
        return ans