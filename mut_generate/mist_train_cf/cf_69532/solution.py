"""
QUESTION:
We need to write a function `largestSumOfAverages(A, K)` where `A` is a sequence of numbers and `K` is the maximum number of contiguous clusters. The function should return the maximum achievable sum of averages when `A` is divided into at most `K` contiguous clusters. The restrictions are: `1 <= len(A) <= 100`, `1 <= A[i] <= 10000`, and `1 <= K <= len(A)`. Responses within `10^-6` of the accurate answer will be deemed correct.
"""

def largestSumOfAverages(A, K):
    P = [0]
    for x in A: P.append(P[-1] + x)
    dp = [P[-1]/len(A) for _ in A] + [0]
    for k in range(K-1):
        for i in range(len(A)-1):
            dp[i] = max(dp[i], max((P[j]-P[i]) / (j-i) + dp[j] for j in range(i+1,len(A)+1)))
    return dp[0]