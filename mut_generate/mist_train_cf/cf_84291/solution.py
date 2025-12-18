"""
QUESTION:
Construct the function `maxNumber(nums1, nums2, k)` that takes two integer arrays `nums1` and `nums2` and an integer `k` as input, and returns an array of the `k` digits that represent the largest possible number of length `k` utilizing the digits from the two numbers while preserving the relative order of the digits from the same array. 

Restrictions: 
`m == nums1.length`
`n == nums2.length`
`1 <= m, n <= 500`
`0 <= nums1[i], nums2[i] <= 9`
`1 <= k <= m + n`
"""

def maxNumber(nums1, nums2, k):
    def pick_max(nums, k):
        drop = len(nums) - k
        out = []
        for num in nums:
            while drop and out and out[-1] < num:
                out.pop()
                drop -= 1
            out.append(num)
        return out[:k]

    def merge(a, b):
        ans = []
        while a or b:
            bigger = a if a > b else b
            ans.append(bigger[0])
            bigger.pop(0)
        return ans

    return max(merge(pick_max(nums1, i), pick_max(nums2, k-i))
               for i in range(k+1)
               if i <= len(nums1) and k-i <= len(nums2))