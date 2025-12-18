"""
QUESTION:
You are given an array of n positive integers a_1, a_2, …, a_n. Your task is to calculate the number of arrays of n positive integers b_1, b_2, …, b_n such that: 

  * 1 ≤ b_i ≤ a_i for every i (1 ≤ i ≤ n), and 
  * b_i ≠ b_{i+1} for every i (1 ≤ i ≤ n - 1). 



The number of such arrays can be very large, so print it modulo 998 244 353.

Input

The first line contains a single integer n (1 ≤ n ≤ 2 ⋅ 10^5) — the length of the array a.

The second line contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ 10^9).

Output

Print the answer modulo 998 244 353 in a single line.

Examples

Input


3
2 2 2


Output


2

Input


2
2 3


Output


4

Input


3
1 1 1


Output


0

Note

In the first test case possible arrays are [1, 2, 1] and [2, 1, 2].

In the second test case possible arrays are [1, 2], [1, 3], [2, 1] and [2, 3].
"""

def count_valid_arrays(n, a):
    mod = 998244353
    dp = [0] * (n + 1)
    dp[0] = 1
    s = []
    sm = 0
    
    for i in range(n):
        x = a[i]
        c = dp[i]
        if i & 1:
            c = -dp[i]
        
        while len(s) and s[-1][0] >= x:
            (v, cc) = s.pop()
            c += cc
            c %= mod
            sm -= v * cc
            sm %= mod
        
        s.append((x, c))
        sm += x * c
        sm %= mod
        
        if i & 1:
            dp[i + 1] -= sm
        else:
            dp[i + 1] += sm
        
        dp[i + 1] %= mod
    
    return dp[-1]