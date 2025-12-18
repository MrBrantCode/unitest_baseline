"""
QUESTION:
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.



Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

def find_max_consecutive_ones(nums: list[int]) -> int:
    if not nums:
        return 0
    
    count = 0
    count_max = 0
    
    for num in nums:
        if num == 1:
            count += 1
        else:
            if count > count_max:
                count_max = count
            count = 0
    
    if count > count_max:
        count_max = count
    
    return count_max