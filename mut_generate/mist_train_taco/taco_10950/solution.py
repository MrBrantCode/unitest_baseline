"""
QUESTION:
You are given N non-negative integers A_1, A_2, ..., A_N and another non-negative integer K.
For a integer X between 0 and K (inclusive), let f(X) = (X XOR A_1) + (X XOR A_2) + ... + (X XOR A_N).
Here, for non-negative integers a and b, a XOR b denotes the bitwise exclusive OR of a and b.
Find the maximum value of f.
What is XOR?
The bitwise exclusive OR of a and b, X, is defined as follows:
 - When X is written in base two, the digit in the 2^k's place (k \geq 0) is 1 if, when written in base two, exactly one of A and B has 1 in the 2^k's place, and 0 otherwise.
For example, 3 XOR 5 = 6. (When written in base two: 011 XOR 101 = 110.)

-----Constraints-----
 - All values in input are integers.
 - 1 \leq N \leq 10^5
 - 0 \leq K \leq 10^{12}
 - 0 \leq A_i \leq 10^{12}

-----Input-----
Input is given from Standard Input in the following format:
N K
A_1 A_2 ... A_N

-----Output-----
Print the maximum value of f.

-----Sample Input-----
3 7
1 6 3

-----Sample Output-----
14

The maximum value is: f(4) = (4 XOR 1) + (4 XOR 6) + (4 XOR 3) = 5 + 2 + 7 = 14.
"""

def find_max_f_value(N, K, A):
    BMAX = 40
    d = [0] * BMAX
    
    for a in A:
        for i in range(BMAX):
            if a & 1 << i:
                d[i] += 1
    
    dp = [[-1 for _ in range(2)] for _ in range(BMAX + 1)]
    dp[0][0] = 0
    
    for i in range(BMAX):
        now = BMAX - 1 - i
        p0 = 2 ** now * d[now]
        p1 = 2 ** now * (N - d[now])
        
        is_one = (K & 1 << now) != 0
        
        if dp[i][1] != -1:
            dp[i + 1][1] = dp[i][1] + max(p1, p0)
        
        if dp[i][0] != -1 and is_one:
            dp[i + 1][1] = max(dp[i + 1][1], dp[i][0] + p0)
        
        if dp[i][0] != -1:
            dp[i + 1][0] = dp[i][0] + (p1 if is_one else p0)
    
    return max(dp[-1])