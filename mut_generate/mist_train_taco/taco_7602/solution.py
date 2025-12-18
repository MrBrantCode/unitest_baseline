"""
QUESTION:
Given an array of positive integers. Find the maximum sum of strictly increasing subarrays.
 
Example 1:
Input : 
arr[] = {1, 2, 3, 2, 5, 1, 7}
Output : 
8
Explanation :
Some Strictly increasing subarrays are -
{1, 2, 3} sum = 6,
{2, 5} sum = 7,
{1, 7} sum = 8,
maximum sum = 8
 
Example 2:
Input:
arr[] = {1, 2, 2, 4}
Output:
6
Your Task:  
You don't need to read input or print anything. Your task is to complete the function maxsum_SIS() which takes the array arr[] and its size N as inputs and returns the required result.
 
Expected Time Complexty: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ A[i] ≤ 1000
"""

def maxsum_SIS(arr, n):
    if n == 0:
        return 0
    
    curr = arr[0]
    max1 = arr[0]
    
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            curr += arr[i]
            if curr > max1:
                max1 = curr
        else:
            curr = arr[i]
    
    return max1