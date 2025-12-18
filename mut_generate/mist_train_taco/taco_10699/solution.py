"""
QUESTION:
Given an array arr[] of N integers arranged in a circular fashion. Your task is to find the maximum contiguous subarray sum.
Example 1:
Input:
N = 7
arr[] = {8,-8,9,-9,10,-11,12}
Output:
22
Explanation:
Starting from the last element
of the array, i.e, 12, and 
moving in a circular fashion, we 
have max subarray as 12, 8, -8, 9, 
-9, 10, which gives maximum sum 
as 22.
Example 2:
Input:
N = 8
arr[] = {10,-3,-4,7,6,5,-4,-1}
Output:
23
Explanation: Sum of the circular 
subarray with maximum sum is 23
Your Task:
The task is to complete the function circularSubarraySum() which returns a sum of the circular subarray with maximum sum.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
Constraints:
1 <= N <= 10^{6}
-10^{6 }<= Arr[i] <= 10^{6}
"""

def circular_subarray_sum(arr, n):
    if n == 1:
        return arr[0]
    
    total_sum = sum(arr)
    
    # Find the maximum subarray sum using Kadane's algorithm
    maxsum = arr[0]
    currmax = arr[0]
    for i in range(1, n):
        currmax = max(currmax + arr[i], arr[i])
        maxsum = max(maxsum, currmax)
    
    # Find the minimum subarray sum using modified Kadane's algorithm
    minsum = arr[0]
    currmin = arr[0]
    for i in range(1, n):
        currmin = min(currmin + arr[i], arr[i])
        minsum = min(minsum, currmin)
    
    # If all elements are negative, the maximum subarray sum is the maximum element
    if minsum == total_sum:
        return maxsum
    
    # The maximum circular subarray sum is the maximum of the maximum subarray sum
    # and the total sum minus the minimum subarray sum
    return max(maxsum, total_sum - minsum)