"""
QUESTION:
Given an array of N integers, you have to find if it is possible to partition the array with following rules:
	Each element should belong to exactly one partition.
	Each partition should have atleast K elements.
	Absolute difference between any pair of elements in the same partition should not exceed M.
Example 1:
Input:
N = 5
K = 2
M = 3
A[] = {8, 3, 9, 1, 2}
Output:
YES
Explanation:
We can partition the array into two 
partitions: {8, 9} and {3, 1, 2} such that
all rules are satisfied.
Your Task:
You don't need to read input or print anything. Your task is to complete the function partitionArray() which takes the number of elements N, integer K, integer M and array A[ ] as input parameters and returns true if we can partition the array such that all rules are satisfied, else returns false.
Expected Time Complexity: O(N * Log(N))
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 2*10^{5}
1 ≤ K ≤ N
1 ≤ M ≤ 10^{9}
1 ≤ A[i] ≤ 10^{9}
"""

def can_partition_array(N, K, M, A):
    A.sort()
    dp = [False] * N
    
    for i in range(K - 1, N):
        n = i - (K - 1) + 1
        lo, hi = 0, n
        
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if A[i] - A[mi] <= M:
                hi = mi
            else:
                lo = mi + 1
        
        for j in range(lo, n):
            if j == 0 or dp[j - 1]:
                dp[i] = True
                break
    
    return dp[-1]