"""
QUESTION:
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.  

You need to find the shortest such subarray and output its length.

Example 1:

Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.



Note:

Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means .
"""

def find_shortest_unsorted_subarray_length(nums):
    left = 1
    size = len(nums)
    
    if size == 0:
        return 0
    
    while left < size and nums[left - 1] <= nums[left]:
        left += 1
    
    if left == size:
        return 0
    
    left -= 1
    right = size - 1
    
    while right > 0 and nums[right] >= nums[right - 1]:
        right -= 1
    
    sub = nums[left:right + 1]
    min_ = min(sub)
    max_ = max(sub)
    
    for i in range(left):
        if nums[i] > min_:
            left = i
            break
    
    for i in range(size - 1, right, -1):
        if nums[i] < max_:
            right = i
            break
    
    return right - left + 1