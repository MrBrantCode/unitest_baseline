"""
QUESTION:
Given an array Arr of size N, each element of the array represents the amount of calories, the task is to calculate the maximum of amount of calories you can get remembering the fact that you cannot take three consecutive calories.
Example 1:
Input: N = 5, arr[] = {3, 2, 1, 10, 3}
Output: 18
Explanation: You can take 1st, 2nd, 4th 
and 5th calories (3 + 2 + 10 + 3) = 18
Example 2:
Input: N = 2, arr[] = {8, 15}
Output: 23
Explanation: You can take 1st and 2nd
calories (8 + 15) = 23
Your Task:  
You don't need to read input or print anything. Complete the function maxCalories() which takes N  and array Arr as input parameter and returns an integer value.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ Arr[i] ≤ 10^{4}
"""

def max_calories(arr, n):
    if n < 3:
        return sum(arr)
    
    dp = [0] * n
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(dp[1], arr[2] + dp[0], arr[2] + arr[1])
    
    for i in range(3, n):
        dp[i] = max(dp[i - 1], arr[i] + dp[i - 2], arr[i] + arr[i - 1] + dp[i - 3])
    
    return dp[n - 1]