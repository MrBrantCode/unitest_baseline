"""
QUESTION:
You are given two arrays of positive integers `nums1` and `nums2` of the same length. The task is to replace at most one element of `nums1` with any other element from the same array in order to minimize the absolute sum difference between `nums1` and `nums2`. Return the smallest possible absolute sum difference after replacement, modulo `10^9 + 7`.

Constraints:
- `n == nums1.length`
- `n == nums2.length`
- `1 <= n <= 10^5`
- `1 <= nums1[i], nums2[i] <= 10^5`

Implement a function `minAbsoluteSumDiff(nums1, nums2)` to solve the problem.
"""

def minAbsoluteSumDiff(nums1, nums2):
    mod = 10**9 + 7
    sorted_nums1 = sorted(nums1)
    maxn, totalDif = 0, 0

    for i in range(len(nums1)):
        diff = abs(nums1[i] - nums2[i])
        totalDif = (totalDif + diff) % mod
        j = binary_search(sorted_nums1, nums2[i])
        if j < len(nums1):
            maxn = max(maxn, diff - (sorted_nums1[j] - nums2[i]))
        if j > 0:
            maxn = max(maxn, diff - (nums2[i] - sorted_nums1[j-1]))        
    return (totalDif - maxn) % mod

def binary_search(arr, target):
    left, right = 0, len(arr)-1
    if arr[right] < target:
        return right + 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left