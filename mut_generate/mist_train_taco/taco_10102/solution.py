"""
QUESTION:
Given an array arr[] of n integers. Check whether it contains a triplet that sums up to zero. 
Note: Return 1, if there is at least one triplet following the condition else return 0.
Example 1:
Input: n = 5, arr[] = {0, -1, 2, -3, 1}
Output: 1
Explanation: 0, -1 and 1 forms a triplet
with sum equal to 0.
Example 2:
Input: n = 3, arr[] = {1, 2, 3}
Output: 0
Explanation: No triplet with zero sum exists. 
Your Task:
You don't need to read input or print anything. Your task is to complete the boolean function findTriplets() which takes the array arr[] and the size of the array (n) as inputs and print 1 if the function returns true else print 0 if the function returns false. 
Expected Time Complexity: O(n^{2})
Expected Auxiliary Space: O(1)
Constrains:
1 <= n <= 10^{4}
-10^{6} <= A_{i} <= 10^{6}
"""

def has_zero_sum_triplet(arr, n):
    arr.sort()
    for i in range(n):
        left = i + 1
        right = n - 1
        while left < right:
            sum_triplet = arr[i] + arr[left] + arr[right]
            if sum_triplet == 0:
                return 1
            elif sum_triplet > 0:
                right -= 1
            else:
                left += 1
    return 0