"""
QUESTION:
Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.
Example 1:
Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.
Your Task:
You just have to complete the function maxLen() which takes two arguments an array A and n, where n is the size of the array A and returns the length of the largest subarray with 0 sum.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
1 <= N <= 10^{5}
-1000 <= A[i] <= 1000, for each valid i
"""

def max_len_subarray_with_zero_sum(arr, n):
    dic = {}
    sum = 0
    ans = 0
    dic[0] = -1
    for i in range(n):
        sum += arr[i]
        if sum in dic:
            ans = max(ans, i - dic[sum])
        else:
            dic[sum] = i
    return ans