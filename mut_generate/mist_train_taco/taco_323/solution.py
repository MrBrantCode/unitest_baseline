"""
QUESTION:
Given an array arr[] of N integers, the task is to find a subsequence of size K whose product is maximum among all possible K sized subsequences of a given array.
Example 1:
Input: N = 4, K = 2
arr[] = {1, 2, 0, 3} 
Output: 6
Explanation: Subsequence containing 
elements {2, 3} gives maximum product: 
2*3 = 6
Example 2:
Input: N = 6, K = 4
arr[] = {1, 2, -1, -3, -6, 4}
Output: 144
Explanation: Subsequence containing 
{2, -3, -6, 4} gives maximum product: 
2*(-3)*(-6)*4 = 144
Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function maxProductSubarrayOfSizeK() that takes array arr[], integer N and integer K as parameters and returns the desired product.
 
Expected Time Complexity: O(NlogN).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{5}
"""

def max_product_subarray_of_size_k(arr, N, K):
    product = 1
    arr.sort()
    
    if K % 2 and arr[-1] < 0:
        for _ in range(K):
            product *= arr.pop()
        return product
    
    if K % 2:
        product *= arr.pop()
        K -= 1
    
    while K:
        if arr[0] * arr[1] > arr[-1] * arr[-2]:
            product *= arr.pop(0) * arr.pop(0)
        else:
            product *= arr.pop() * arr.pop()
        K -= 2
    
    return product