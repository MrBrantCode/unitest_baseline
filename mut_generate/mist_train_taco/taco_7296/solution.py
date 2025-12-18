"""
QUESTION:
Given an integer array arr, return the number of longest increasing subsequences.
Notice that the sequence has to be strictly increasing.
Example:
Input:
n = 5
arr = [1,3,5,4,7]
Output:
2
Explanation:
The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Your Task:
You don't have to read input or print anything. Your task is to complete the function NumberofLIS() which takes the integer n and array arr and returns the number of the Longest Increasing Subsequences.
Expected Time Complexity: O(n^{2})
Expected Space Complexity: O(n^{2})
Constraint:
1 <= n <= 2000
1 <= arr[i] <= 10^{5}
"""

def number_of_lis(arr, n):
    if n == 0:
        return 0
    
    # Initialize variables to store the length of LIS and count of LIS
    dp = [1] * n  # dp[i] will store the length of LIS ending at index i
    cnt = [1] * n  # cnt[i] will store the count of LIS ending at index i
    
    max_len = 1  # Variable to store the maximum length of LIS found
    
    # Dynamic programming to find the length and count of LIS
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    cnt[i] = cnt[j]
                elif dp[j] + 1 == dp[i]:
                    cnt[i] += cnt[j]
        
        max_len = max(max_len, dp[i])
    
    # Count the number of LIS with the maximum length
    result = 0
    for i in range(n):
        if dp[i] == max_len:
            result += cnt[i]
    
    return result