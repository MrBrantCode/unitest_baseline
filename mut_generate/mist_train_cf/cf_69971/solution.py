"""
QUESTION:
You are given two arrays of integers `nums1` and `nums2`, possibly of different lengths. The values in the arrays are between `1` and `6`, inclusive. In one operation, you can change any integer's value in any of the arrays to any value between `1` and `6`, inclusive, but you can only increase or decrease the values by `2` at a time. Return the minimum number of operations required to make the sum of values in `nums1` equal to the sum of values in `nums2`. Return `-1` if it is not possible to make the sum of the two arrays equal.

Constraints: `1 <= nums1.length, nums2.length <= 10^5` and `1 <= nums1[i], nums2[i] <= 6`. Implement the function `minOperations(nums1, nums2)` that takes `nums1` and `nums2` as input and returns the minimum number of operations required.
"""

def minOperations(nums1, nums2):
    if len(nums1) * 6 < len(nums2) or len(nums1) > len(nums2) * 6:
        return -1
    def countArray(nums):
        counter, total = [0]*6, 0
        for num in nums:
            counter[num-1] += 1
            total += num
        return counter, total
    counter1, total1 = countArray(nums1)
    counter2, total2 = countArray(nums2)
    if total1 < total2:
        counter1, counter2 = counter2, counter1
        total1, total2 = total2, total1
    diff, operations, i = total1-total2, 0, 5
    while diff != 0:
        while i > -1 and counter1[i] == 0:
            i -= 1
        if i == -1:
            return -1
        dec = min(diff, i+1)
        operations += (dec + 1) // 2
        if dec == i+1:
            counter1[i] -= 1
        diff -= dec
    return operations