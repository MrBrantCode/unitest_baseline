"""
QUESTION:
Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.
NOTE*: A subarray is a contiguous part of any given array.
Example 1:
Input:
N = 4, K = 2
Arr = [100, 200, 300, 400]
Output:
700
Explanation:
Arr_{3 } + Arr_{4} =700,
which is maximum.
 
Example 2:
Input:
N = 4, K = 4
Arr = [100, 200, 300, 400]
Output:
1000
Explanation:
Arr_{1} + Arr_{2} + Arr_{3 } 
+ Arr_{4} =1000,
which is maximum.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function maximumSumSubarray() which takes the integer k, vector Arr with size N, containing the elements of the array and returns the maximum sum of a subarray of size K.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1<=N<=10^{6}
1<=K<=N
"""

def maximum_sum_subarray(k: int, arr: list) -> int:
    i = j = 0
    mx = sums = 0
    while j < len(arr):
        sums += arr[j]
        if j - i + 1 < k:
            j += 1
        else:
            mx = max(mx, sums)
            sums -= arr[i]
            i += 1
            j += 1
    return mx