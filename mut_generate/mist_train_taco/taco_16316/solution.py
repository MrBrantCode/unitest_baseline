"""
QUESTION:
You are given array A of size n. You need to find the maximum-sum sub-array with the condition that you are allowed to skip at most one element.
Example 1:
Input:
n = 5
A[] = {1,2,3,-4,5}
Output: 11
Explanation: We can get maximum sum
subarray by skipping -4.
Example 2:
Input:
n = 8
A[] = {-2,-3,4,-1,-2,1,5,-3}
Output: 9
Explanation: We can get maximum sum
subarray by skipping -2 as [4,-1,1,5]
sums to 9, which is the maximum
achievable sum.
Your Task:
Your task is to complete the function maxSumSubarray that take array and size as parameters and returns the maximum sum.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
1 <= n <= 100
-10^{3} <= A_{i}<= 10^{3}
"""

def max_sum_subarray_with_skip(arr, n):
    if n == 0:
        return 0
    
    left = [0] * n
    right = [0] * n
    
    # Initialize the first element of left and the last element of right
    left[0] = arr[0]
    right[-1] = arr[-1]
    
    # Fill the left array
    for i in range(1, n):
        left[i] = max(left[i - 1] + arr[i], arr[i])
    
    # Fill the right array
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1] + arr[i], arr[i])
    
    # Initialize the answer with the maximum value in the left array
    ans = max(left)
    
    # Check the maximum sum by skipping at most one element
    for i in range(1, n - 1):
        ans = max(ans, left[i - 1] + right[i + 1])
    
    return ans