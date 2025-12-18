"""
QUESTION:
Given an array of n elements, update all elements of given array to some minimum value x i.e, arr[i] = x (0 <= i < n), such that product of all elements of this new array is strictly greater than the product of all elements of the initial array.
Example 1:
Input:
N=5
arr[] = {4, 2, 1, 10, 6} 
Output: 4
Explanation:
4 is the smallest value such that  
4 * 4 * 4 * 4 * 4 > 4 * 2 * 1 * 10 * 6.  
Example 2:
Input:
N=5
arr[] = {100, 150, 10000, 123458, 90980454} 
Output: 17592
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function findMinValue() that takes array arr and n as parameters and return the desired minimum value.
 
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{5}
 1 <= arr[i] <= 10^{10}
"""

import math

def binarysearch(n, l, r, k):
    if l <= r:
        mid = (l + r) // 2
        if math.log(mid) * n > k:
            return binarysearch(n, l, mid - 1, k)
        return binarysearch(n, mid + 1, r, k)
    return l

def find_min_value(arr, n):
    val = 0
    for i in range(n):
        val += math.log(arr[i])
    return binarysearch(n, min(arr), max(arr), val)