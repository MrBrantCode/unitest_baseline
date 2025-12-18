"""
QUESTION:
Given an array arr of size N, the task is to modify values of this array in such a way that the sum of absolute differences between two consecutive elements is maximized. If the value of an array element is X, then we can change it to either 1 or X. Find the maximum possible value of the sum of absolute differences between two consecutive elements.
Example 1:
Input: N = 4, arr[] = [3, 2, 1, 4, 5]
Output: 8
Explanation: We can modify above array as
arr[] = [3, 1, 1, 4, 1]
Sum of differences = 
|1-3| + |1-1| + |4-1| + |1-4| = 8
Which is the maximum obtainable value 
among all choices of modification.
Example 2:
Input: N = 2, arr[] = {1, 5}
Output: 4
Explanation: No modification required
Your Task:  
You don't need to read input or print anything. Complete the function maximumDifferenceSum() which takes N and array arr as input parameters and returns the integer value
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
"""

def maximum_difference_sum(arr, N):
    # Initialize a 2D list to store the dynamic programming results
    dp = [[0] * 2 for _ in range(N)]
    
    # Iterate through the array starting from the second element
    for i in range(1, N):
        # Calculate the maximum sum of differences if the current element is not changed to 1
        dp[i][0] = max(dp[i - 1][0] + abs(arr[i] - arr[i - 1]), 
                       dp[i - 1][1] + abs(arr[i] - 1))
        
        # Calculate the maximum sum of differences if the current element is changed to 1
        dp[i][1] = max(dp[i - 1][0] + abs(1 - arr[i - 1]), 
                       dp[i - 1][1])
    
    # Return the maximum value from the last element of the dp array
    return max(dp[-1])