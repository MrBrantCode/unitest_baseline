"""
QUESTION:
Given an array arr and target sum k, check whether there exists a subsequence such that the sum of all elements in the subsequence equals the given target sum(k).
Example:
Input:  arr = [10,1,2,7,6,1,5], k = 8.
Output:  Yes
Explanation:  Subsequences like [2, 6], [1, 7] sum upto 8
Input:  arr = [2,3,5,7,9], k = 100. 
Output:  No
Explanation:  No subsequence can sum upto 100
Your Task:
You don't need to read or print anything. Your task is to complete the boolean function checkSubsequenceSum() which takes N, arr and K as input parameter and returns true/false based on the whether any subsequence with sum K could be found.
Expected Time Complexity: O(N * K).
Expected Auxiliary Space: O(N * K).
Constraints:
1 <= arr.length <= 2000.
1 <= arr[i] <= 1000.
1 <= target <= 2000.
"""

def check_subsequence_sum(arr, k):
    dp = [0] * (k + 1)
    dp[0] = 1
    for a in arr:
        for i in range(k, -1, -1):
            if i - a >= 0:
                dp[i] += dp[i - a]
    return dp[k] >= 1