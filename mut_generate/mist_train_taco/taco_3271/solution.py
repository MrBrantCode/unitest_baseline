"""
QUESTION:
Given an array Arr[], the task is to find the maximum sum of all the elements which are not a part of the longest increasing subsequence.
Example 1:
Input:
n = 6
Arr = {4, 6, 1, 2, 4, 6}
Output: 10
Explaination: Elements are 4 and 6.
Example 2:
Input:
n = 5
Arr = {5, 4, 3, 2, 1}
Output: 14
Explaination: Elements are 5,4,3 and 2.
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxSumLis() which takes the array Arr[] and its size n as input parameters and returns maximum sum of elements not part of LIS.
Expected Time Complexity: O(n^{2})
Expected Auxiliary Space: O(n)
Constraints:
1 ≤ N ≤ 1000
1 ≤ Arr[i] ≤ 10^{5}
"""

from bisect import bisect_left

def max_sum_not_in_lis(Arr, n):
    lis = []
    total_sum = 0
    lis_sum = [0] * (n + 1)
    
    for i in range(n):
        total_sum += Arr[i]
        index = bisect_left(lis, Arr[i])
        if index == len(lis):
            lis.append(Arr[i])
        else:
            lis[index] = Arr[i]
        lis_sum[index + 1] = lis_sum[index] + Arr[i]
    
    return total_sum - lis_sum[len(lis)]