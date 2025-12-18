"""
QUESTION:
Given a sorted array 'nums' of length 'n' where 1 <= n <= 3 * 10^4 and -10^4 <= nums[i] <= 10^4, modify 'nums' in-place to contain at most two occurrences of each element. The function 'removeDuplicates(nums)' should return an integer representing the length of the modified array, and the first 'k' elements of 'nums' should be the modified array, where 'k' is the returned length. The operation should be performed with O(1) extra memory.
"""

def entance(nums):
    if len(nums) < 3:
        return len(nums)
    
    i = 2
    for j in range(2, len(nums)):
        if nums[i - 2] != nums[j]:
            nums[i] = nums[j]
            i += 1
            
    return i