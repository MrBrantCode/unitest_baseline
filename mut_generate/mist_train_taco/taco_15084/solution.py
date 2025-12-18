"""
QUESTION:
Given an array arr[] of N positive integers. Select values from the array such that their sum is minimum. You must pick at least 1 value from each group of 4 consecutive elements. 
Example 1:
Input:
N = 5
Arr[] = {1, 2, 3, 1, 2}
Output: 1
Explanation: There are 2 groups of 4
in the given array. The 1st group is
[1 2 3 1] and 2nd is [2 3 1 2].
Selecting the 4th element in the 
array will give the least sum as 
it belongs to both groups.
Example 2:
Input:
N = 6
Arr[] = {8, 6, 9, 10, 6, 7}
Output: 9
Explanation: There are 3 groups of 4
consecutive elements. 9 at index 2 
is the smallest element that is 
present in all 3 groups. 
Your Task:
You don't need to read input or print anything. Your task is to complete the function pickValues() which takes the array of integers arr[] and its size n as input parameters and returns an integer denoting the minimum sum.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ Arr[i] ≤ 10^{3}
"""

def minimum_sum_from_groups(arr, n):
    if n <= 4:
        return min(arr)
    
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = arr[1]
    dp[2] = arr[2]
    dp[3] = arr[3]
    
    for i in range(4, n):
        dp[i] = min(dp[i - 1], dp[i - 2], dp[i - 3], dp[i - 4]) + arr[i]
    
    return min(dp[n - 1], dp[n - 2], dp[n - 3], dp[n - 4])