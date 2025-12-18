"""
QUESTION:
Given an array Arr of size N containing positive integers. Find the maximum sum that can be formed which has no three consecutive elements present.
Example 1:
Input: arr[] = {1,2,3}
Output: 5
Explanation: All three element present in the array is
consecutive, hence we have to consider just two
element sum having maximum,which is 2+3 = 5
Example 2:
Input: arr[] = {3000,2000,1000,3,10}
Output: 5013
Explanation: 3000 + 2000 + 3 + 10 = 5013.
Here no three elements is consecutive in that subsequence.
Your Task:
You don't need to read input or print anything. Your task is to complete the function findMaxSum() which takes the array of integers arr and n as parameters and returns an integer denoting the answer.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{6}
1 ≤ Arr_{i} ≤ 10^{7}
"""

def find_max_sum(arr, n):
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return arr[0] + arr[1]
    
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(dp[1], arr[1] + arr[2], arr[0] + arr[2])
    
    for i in range(3, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i])
    
    return max(dp)