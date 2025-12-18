"""
QUESTION:
Given an array A of n non-negative integers. Find the number of ways to partition/divide the array into subarrays, such that  mex in each subarray is not more than k. For example, mex of the arrays [1, 2] will be 0, and that of [0, 2] will be 1, and that of [0, 1, 2] will be 3. Due to the fact that the answer can turn out to be quite large, calculate it modulo 109 + 7.

-----Input-----
- The first line of the input contains two integers n, k denoting the number of elements and limit of mex.
- The second line contains n space-separated integers A1, A2, ... , An .

-----Output-----
- Output a single integer corresponding to the answer of the problem.

-----Constraints-----
- 1 ≤ n ≤ 5 * 105
- 0 ≤ k, A[i] ≤ 109

-----Example-----
Input:
3 1
0 1 2

Output:
2

Input:
10 3
0 1 2 3 4 0 1 2 5 3

Output:
379

-----Explanation-----
Example 1. The valid ways of partitioning will be [[0], [1, 2]] (mex of first subarray is 1, while that of the second is zero), and [[0], [1], [2]] (mex of first subarray is 1, and that of others is 0). There is no other way to partition the array such that mex is less than or equal to 1. For example, [[0, 1], [2]] is not a valid partitioning as mex of first subarray is 2 which is more than 1.
"""

def count_partitions_with_mex_limit(n, k, A):
    mod = 10**9 + 7
    cons = 500001  # 5 * 10^5 + 1
    
    # Precompute the powers of 2 modulo mod
    tpa = [1] * cons
    for i in range(1, cons):
        tpa[i] = tpa[i - 1] * 2 % mod
    
    if k > n:
        return tpa[n - 1]
    
    # Initialize index list for each value in A that is <= k
    il = [[] for _ in range(k + 1)]
    for i in range(n):
        if A[i] <= k:
            il[A[i]].append(i)
    
    # Check if any value in il is empty
    for i in range(k + 1):
        if len(il[i]) == 0:
            return tpa[n - 1]
    
    # Initialize dp array and other variables
    dp = [-1] * n
    dp[0] = 1
    si = max(il, key=lambda x: x[0])[0]
    s = 1
    
    # Fill dp array for the first segment
    for i in range(1, si):
        dp[i] = tpa[i]
        s = (s + dp[i]) % mod
    
    # Initialize current index array
    ci = [0] * (k + 1)
    j = si
    i = 0
    
    # Fill dp array for the rest of the array
    while j < n:
        if A[i] > k:
            s = (s - dp[i]) % mod
            i += 1
        elif ci[A[i]] + 1 < len(il[A[i]]) and il[A[i]][ci[A[i]] + 1] <= j:
            s = (s - dp[i]) % mod
            ci[A[i]] += 1
            i += 1
        else:
            dp[j] = s
            s = (s + dp[j]) % mod
            j += 1
    
    return dp[n - 1]