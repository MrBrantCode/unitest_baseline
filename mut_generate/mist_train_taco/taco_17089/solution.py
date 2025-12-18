"""
QUESTION:
Given two integers N and K, the task is to count the number of ways to divide N into groups of positive integers. Such that each group shall have K elements and their sum is N. Also the number of elements in the groups follows a non-decreasing order (i.e. group[i] <= group[i+1]). Find the number of such groups
Example 1:
Input:
N = 8
K = 4
Output:
5
Explanation:
There are 5 groups such that their sum is 8 
and the number of positive integers in each 
group is 4. The 5 groups are [1, 1, 1, 5], 
[1, 1, 2, 4], [1, 1, 3, 3], [1, 2, 2, 3] and 
[2, 2, 2, 2].
Example 2:
Input: 
N = 4
K = 3
Output:
1
Explanation: 
The only possible grouping is {1, 1, 2}. Hence,
the answer is 1 in this case.
Your Task:
Complete the function countWaystoDivide() which takes the integers N and K as the input parameters, and returns the number of ways to divide the sum N into K groups.
Expected Time Complexity: O(N^{2}*K)
Expected Auxiliary Space: O(N^{2}*K)
Constraints:
1 ≤ K ≤ N ≤ 100
"""

def count_ways_to_divide(N, K):
    dp = [[[0 for _ in range(K + 1)] for _ in range(N + 1)] for _ in range(N + 1)]
    
    # Base case: There's one way to make a sum of 0 with 0 groups
    for i in range(1, N + 1):
        dp[i][0][0] = 1
    
    # Fill the DP table
    for max_value in range(1, N + 1):
        for remaining_sum in range(1, N + 1):
            for remaining_groups in range(1, K + 1):
                dp[max_value][remaining_sum][remaining_groups] = dp[max_value - 1][remaining_sum][remaining_groups]
                if remaining_sum >= max_value:
                    dp[max_value][remaining_sum][remaining_groups] += dp[max_value][remaining_sum - max_value][remaining_groups - 1]
    
    # Calculate the final answer
    ans = 0
    for i in range(1, N + 1):
        ans += dp[i][N - i][K - 1]
    
    return ans