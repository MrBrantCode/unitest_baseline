"""
QUESTION:
An array B of length M consisting of only distinct elements is said to be *good* if the following condition holds:
Let i be the index of the maximum element of B.
Then, B[1,i] must be in ascending order, i.e, B_{1} < B_{2} < B_{3} < \ldots < B_{i}.

For example, [1, 2, 3], [1, 4, 3, 2] and [1, 3, 2] are *good* arrays, while [2, 1, 3] and [3, 2, 4, 1] are not.

You are given a permutation P of length N. You have to partition P into some non-empty good [subarrays]. Note that every element of P should be contained in exactly one subarray.

Find the total number of valid partitions. 

Since the answer can be quite large, please print it modulo 998244353.

Note: A permutation of length N is an arrangement of the integers \{1, 2, 3, \ldots, N\}.

------ Input Format ------ 

- The first line of input contains a single integer T denoting the number of test cases. The description of T test cases follows.
- Each test case consists of two lines of input.
- The first line of each test case contains a single integer N, the length of P.
- The second line contains N space-separated distinct integers P_{1}, P_{2}, P_{3} , \ldots, P_{N}.

------ Output Format ------ 

For each test case, output on a new line the number of valid partitions modulo 998244353.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{6}$
$1 ≤ P_{i} ≤ N$ for each $1 ≤ i ≤ N$.
- All elements of $P$ are distinct.
- The sum of $N$ over all test cases won't exceed $10^{6}$.

----- Sample Input 1 ------ 
2
4
2 1 4 3
5
1 2 3 4 5

----- Sample Output 1 ------ 
6
16

----- explanation 1 ------ 
Test case $1$: The $6$ valid partitions are as follows:
- $[2], [1], [4], [3]$
- $[2], [1], [4, 3]$
- $[2], [1, 4], [3]$
- $[2], [1, 4, 3]$
- $[2, 1], [4], [3]$
- $[2, 1], [4, 3]$
"""

def count_valid_partitions(N, P):
    MOD = 998244353
    
    def next_gre(arr):
        stack = []
        n = len(arr)
        next_greater = [n] * n
        for i in range(n):
            x = arr[i]
            while len(stack) and stack[-1][0] < x:
                y = stack.pop(-1)[1]
                next_greater[y] = i
            stack.append((x, i))
        return next_greater
    
    suff = [0] * (N + 1)
    suff[N] = 1
    suff[N - 1] = 2
    next_greater = next_gre(P)
    prev = N
    dp = [0] * (N + 1)
    dp[N - 1] = 1
    dp[N] = 1
    
    for i in range(N - 2, -1, -1):
        if P[i] > P[i + 1]:
            prev = next_greater[i]
        dp[i] = (suff[i + 1] - suff[prev] + dp[prev]) % MOD
        suff[i] = (suff[i + 1] + dp[i]) % MOD
    
    return dp[0] % MOD