"""
QUESTION:
Given an array sequence [A1 , A2 ...An], the task is to find the maximum possible sum of increasing subsequence S of length K such that Si1<=Si2<=Si3.........<=Sin.
 
Example 1:
Input:
N = 8 K = 3
A[] = {8 5 9 10 5 6 19 8}
Output: 38
Explanation:
Possible increasing subsequence of
length 3 with maximum possible
sum is 9 10 19.
Example 2:
Input:
N = 2,K = 2
A[] = {10 5}
Output: -1
Explanation:
Can't make any increasing subsequence 
of length 2.
Your Task:
You don't need to read or print anything. Your task is to complete the function max_sum() which takes sequence A as the first parameter and K as the second parameter and returns the maximum possible sum of K-length increasing subsequnece. If not possible return -1.
Expected Time Complexity: O(max(Ai) * n * log(max(Ai)))
Expected Space Complexity: O(max(Ai))
Contraints:
1 <= n <= 100
1 <= A_{i} <= 100000
"""

def max_sum_of_increasing_subsequence(A, K):
    n = len(A)
    if K > n:
        return -1
    
    # Initialize dp array with -1
    dp = [[-1 for _ in range(K)] for _ in range(n)]
    
    # Fill the dp array
    for i in range(n):
        dp[i][0] = A[i]
        for j in range(1, K):
            for l in range(i):
                if A[l] <= A[i] and dp[l][j - 1] != -1:
                    dp[i][j] = max(dp[i][j], dp[l][j - 1] + A[i])
    
    # Find the maximum sum of K-length increasing subsequence
    max_sum = -1
    for i in range(n):
        max_sum = max(max_sum, dp[i][K - 1])
    
    return max_sum