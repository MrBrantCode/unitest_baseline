"""
QUESTION:
Peter has a sequence of integers a_1, a_2, ..., a_{n}. Peter wants all numbers in the sequence to equal h. He can perform the operation of "adding one on the segment [l, r]": add one to all elements of the sequence with indices from l to r (inclusive). At that, Peter never chooses any element as the beginning of the segment twice. Similarly, Peter never chooses any element as the end of the segment twice. In other words, for any two segments [l_1, r_1] and [l_2, r_2], where Peter added one, the following inequalities hold: l_1 ≠ l_2 and r_1 ≠ r_2.

How many distinct ways are there to make all numbers in the sequence equal h? Print this number of ways modulo 1000000007 (10^9 + 7). Two ways are considered distinct if one of them has a segment that isn't in the other way.


-----Input-----

The first line contains two integers n, h (1 ≤ n, h ≤ 2000). The next line contains n integers a_1, a_2, ..., a_{n} (0 ≤ a_{i} ≤ 2000).


-----Output-----

Print a single integer — the answer to the problem modulo 1000000007 (10^9 + 7).


-----Examples-----
Input
3 2
1 1 1

Output
4

Input
5 1
1 1 1 1 1

Output
1

Input
4 3
3 2 1 1

Output
0
"""

def count_ways_to_equalize_sequence(n, h, a):
    mod = 10**9 + 7
    
    # Initialize the DP table
    dp = [[0 for _ in range(h + 1)] for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        need = h - a[i - 1]
        if need < 0:
            return 0
        if need == 0:
            dp[i][0] = dp[i - 1][0]
        else:
            dp[i][need] = (dp[i - 1][need] + dp[i - 1][need - 1]) % mod
            dp[i][need - 1] = dp[i][need] * need % mod
    
    return dp[n][0]