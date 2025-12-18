"""
QUESTION:
Given an array arr[] of N elements and a number K. Split the given array into K subarrays such that the maximum subarray sum achievable out of K subarrays formed is minimum possible. Find that possible subarray sum.
Example 1:
Input:
N = 4, K = 3
arr[] = {1, 2, 3, 4}
Output: 4
Explanation:
Optimal Split is {1, 2}, {3}, {4}.
Maximum sum of all subarrays is 4,
which is minimum possible for 3 splits. 
Example 2:
Input:
N = 3, K = 2
A[] = {1, 1, 2}
Output:
2
Explanation:
Splitting the array as {1,1} and {2} is optimal.
This results in a maximum sum subarray of 2.
 
Your Task:
The task is to complete the function splitArray() which returns the maximum sum subarray after splitting the array into K subarrays such that maximum sum subarray is minimum possible.
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ K ≤ N
1 ≤ arr[i] ≤ 10^{4}
Expected Time Complexity: O(N*log(sum(arr))).
Expected Auxiliary Space: O(1).
"""

def find_min_max_subarray_sum(arr, K):
    def can_split_with_max_sum(mid):
        subarray_count = 0
        current_sum = 0
        for num in arr:
            current_sum += num
            if current_sum > mid:
                subarray_count += 1
                current_sum = num
        return subarray_count + 1 <= K

    left, right = max(arr), sum(arr)
    result = right

    while left <= right:
        mid = (left + right) // 2
        if can_split_with_max_sum(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result