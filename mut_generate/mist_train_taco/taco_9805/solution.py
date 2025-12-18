"""
QUESTION:
Given are integers L and R. Find the number, modulo 10^9 + 7, of pairs of integers (x, y) (L \leq x \leq y \leq R) such that the remainder when y is divided by x is equal to y \mbox{ XOR } x.What is \mbox{ XOR }?

The XOR of integers A and B, A \mbox{ XOR } B, is defined as follows:

 - When A \mbox{ XOR } B is written in base two, the digit in the 2^k's place (k \geq 0) is 1 if either A or B, but not both, has 1 in the 2^k's place, and 0 otherwise.
For example, 3 \mbox{ XOR } 5 = 6. (In base two: 011 \mbox{ XOR } 101 = 110.)


-----Constraints-----
 - 1 \leq L \leq R \leq 10^{18}

-----Input-----
Input is given from Standard Input in the following format:
L R

-----Output-----
Print the number of pairs of integers (x, y) (L \leq x \leq y \leq R) satisfying the condition, modulo 10^9 + 7.

-----Sample Input-----
2 3

-----Sample Output-----
3

Three pairs satisfy the condition: (2, 2), (2, 3), and (3, 3).
"""

def count_valid_pairs(L, R):
    MOD = 10**9 + 7
    dp = [[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(61)]
    dp[60][0][0][0] = 1
    
    for n in range(60)[::-1]:
        lb = L >> n & 1
        rb = R >> n & 1
        for x in range(2):
            for y in range(2):
                for i in range(2):
                    for j in range(2):
                        for k in range(2):
                            ni = i
                            nj = j
                            nk = k
                            if x > y:
                                continue
                            if k == 0 and x != y:
                                continue
                            if x & y:
                                nk = 1
                            if i == 0 and x < lb:
                                continue
                            if x > lb:
                                ni = 1
                            if j == 0 and y > rb:
                                continue
                            if y < rb:
                                nj = 1
                            dp[n][ni][nj][nk] += dp[n + 1][i][j][k]
                            dp[n][ni][nj][nk] %= MOD
    
    result = (dp[0][1][1][1] + dp[0][0][1][1] + dp[0][1][0][1] + dp[0][0][0][1]) % MOD
    return result