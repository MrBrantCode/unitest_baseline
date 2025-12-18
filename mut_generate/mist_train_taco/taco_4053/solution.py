"""
QUESTION:
Given an array arr[] of n integers. Count the total number of sub-array having total distinct elements same as that of total distinct elements of the original array.
 
Example 1:
Input:
N=5
arr[] = {2, 1, 3, 2, 3} 
Output: 5
Explanation:
Total distinct elements in array is 3
Total sub-arrays that satisfy the condition
are:
Subarray from index 0 to 2
Subarray from index 0 to 3
Subarray from index 0 to 4
Subarray from index 1 to 3
Subarray from index 1 to 4
Example 2:
Input:
N=5
arr[] = {2, 4, 4, 2, 4} 
Output: 9
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function countDistinctSubarray() that takes array arr and integer n  as parameters and returns the desired result.
 
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
 
Constraints:
1 ≤ N ≤ 10^{4}
"""

def count_distinct_subarrays(arr, n):
    uniq = 0
    dt = {}
    ds = {}
    
    # Count distinct elements in the original array
    for i in range(n):
        if dt.get(arr[i], 0) == 0:
            uniq += 1
        dt[arr[i]] = 1
    
    start = end = ans = 0
    cnt = 0
    
    # Find the first subarray with all distinct elements
    for i in range(n):
        if ds.get(arr[i], 0) == 0:
            cnt += 1
        ds[arr[i]] = ds.get(arr[i], 0) + 1
        if cnt == uniq:
            end = i
            break
    
    # Count subarrays with the same number of distinct elements
    while end < n:
        if start < n and ds[arr[start]] >= dt[arr[start]] and (cnt == uniq):
            if ds[arr[start]] == dt[arr[start]]:
                cnt -= 1
            ans += n - end
            ds[arr[start]] -= 1
            start += 1
        else:
            end += 1
            if end < n:
                ds[arr[end]] = ds.get(arr[end], 0) + 1
                if ds[arr[end]] == dt[arr[end]]:
                    cnt += 1
    
    return ans