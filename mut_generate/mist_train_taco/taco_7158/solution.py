"""
QUESTION:
Given two positive integer N and M. The task is to find the number of arrays of size N that can be formed such that:
1. Each element is in the range [1, M].
2. All adjacent element are such that one of them divide the another i.e element A_{i} divides A_{i + 1 }or A_{i+1} divides A_{i}.
Example 1:
Input: 
N = 3
M = 3
Output : 
17
Explanation:
{1,1,1}, {1,1,2}, {1,1,3}, {1,2,1}, 
{1,2,2}, {1,3,1}, {1,3,3}, {2,1,1},
{2,1,2}, {2,1,3}, {2,2,1}, {2,2,2},
{3,1,1}, {3,1,2}, {3,1,3}, {3,3,1}, 
{3,3,3} are possible arrays.
Example 2:
Input: 
N = 1
M = 10 
Output: 
10
Explanation: 
{1}, {2}, {3}, {4}, {5}, 
{6}, {7}, {8}, {9}, {10}
are possible arrays.
Your Task:
You don't need to read input or print anything. Your task is to complete the function count() which take integers N and M as input parameter and returns the total the number of arrays of size N that can be formed with given constraints. The return value may long so take modulo 10^{9}+7. 
Expected Time Complexity: O(N*M*Log M) 
Expected Space Complexity: O(N*M) 
Constraints:
1<=N,M<=100
"""

def count_valid_arrays(N: int, M: int) -> int:
    MAX = 1001
    dp = [[0 for _ in range(MAX)] for _ in range(MAX)]
    di = [[] for _ in range(MAX)]
    mu = [[] for _ in range(MAX)]
    
    # Precompute divisors and multiples
    for i in range(1, M + 1):
        for j in range(2 * i, M + 1, i):
            di[j].append(i)
            mu[i].append(j)
        di[i].append(i)
    
    # Initialize base case for dp
    for i in range(1, M + 1):
        dp[1][i] = 1
    
    # Fill dp table
    for i in range(2, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = 0
            for x in di[j]:
                dp[i][j] += dp[i - 1][x]
            for x in mu[j]:
                dp[i][j] += dp[i - 1][x]
    
    # Calculate the final answer
    ans = 0
    for i in range(1, M + 1):
        ans += dp[N][i]
    
    # Clear the lists to free up space
    for i in range(1, M + 1):
        di[i].clear()
        mu[i].clear()
    
    # Return the answer modulo 10^9 + 7
    mod = 1000000007
    return ans % mod