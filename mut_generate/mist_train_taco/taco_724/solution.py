"""
QUESTION:
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
	answer[i] % answer[j] == 0, or
	answer[j] % answer[i] == 0
If there are multiple sequences with the largest size, return any of them.
Example 1:
Input:
n = 3
arr = [1,2,3]
Output:
[1,2]
Explanation:
Largest Divisble Subset is [1,2].
Example 2:
Input:
n = 4
arr = [1,2,4,8]
Output:
[1,2,4,8]
Your Task:
You don't have to read input or print anything. Your task is to complete the function LargestSubset() which takes the integer n and array arr and returns the Largest Divisible Subset.
Expected Time Complexity: O(n^{2})
Expected Space Complexity: O(n^{2})
Constraint:
1 <= n <= 1000
1  <= arr[i] <= 2 * 10^{9}
"""

def largest_divisible_subset(arr, n):
    if n == 0:
        return []
    
    arr.sort()
    dp = [1] * n
    p = [-1] * n
    val = 0
    pos = 0
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] % arr[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                p[i] = j
        if val < dp[i]:
            val = dp[i]
            pos = i
    
    ans = []
    while pos != -1:
        ans.append(arr[pos])
        pos = p[pos]
    
    return ans[::-1]  # Reverse the list to maintain the original order