"""
QUESTION:
Given an array with n elements. Find length of the largest sub-array having GCD equal to 1. If no such  subarray exist with GCD 1, return -1.
Example 1:
Input: n = 3, arr = [1, 3, 5]
Output: 3 
Explanation: GCD of 1, 3 and 5
is equal to 1.So the length is 3. 
Example 2:
Input: n = 3, arr = [2, 4, 6]
Output: -1
Explanation: No such  subarray exist.
Your Task:  
You dont need to read input or print anything. Complete the function findLargestSubarray() which takes array arr of length n as input parameter and returns the length of the largest subarray and if no such subarray exist
returns -1. 
Expected Time Complexity: O(nlogn)
Expected Auxiliary Space: O(1)
Constraints:
1<= n <=1000
1<= arr[i] <=1000
"""

import math

def find_largest_subarray_with_gcd_one(arr, n):
    if n == 0:
        return -1
    
    gcd = arr[0]
    for i in range(1, n):
        gcd = math.gcd(gcd, arr[i])
    
    if gcd == 1:
        return n
    else:
        return -1