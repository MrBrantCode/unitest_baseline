"""
QUESTION:
Write a function `numberOfArithmeticSlices(A)` that takes a list of integers `A` as input, and returns the total count of arithmetic subsequence slices in the array `A`. 

An arithmetic subsequence slice is a sequence of integers (P0, P1, ..., Pk) where 0 ≤ P0 < P1 < ... < Pk < N and the sequence A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic. 

The input comprises N integers, each of which lies in the range of -231 and 231-1 and 0 ≤ N ≤ 1000. The output is assured to be less than 231-1.
"""

def numberOfArithmeticSlices(A):
    N = len(A)
    ans = 0
    dp = [{} for _ in range(N)]
    for i in range(N):
        for j in range(i):
            diff = A[i] - A[j]
            dp[i][diff] = dp[i].get(diff, 0) + 1  # for the subsequence consisting only of i and j
            if diff in dp[j]:
                ans += dp[j][diff]  # add counts of subsequences ending at j with the same difference
                dp[i][diff] += dp[j][diff]  # for subsequences ending at i
    return ans