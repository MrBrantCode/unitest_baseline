"""
QUESTION:
Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.
An array A is a zigzag array if either:

Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...

Return the minimum number of moves to transform the given array nums into a zigzag array.
 
Example 1:
Input: nums = [1,2,3]
Output: 2
Explanation: We can decrease 2 to 0 or 3 to 1.

Example 2:
Input: nums = [9,6,1,6,2]
Output: 4

 
Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
"""

def min_moves_to_zigzag(nums: list[int]) -> int:
    n = len(nums)
    
    # Calculate moves for even-indexed zigzag pattern
    res0 = 0
    for i in range(0, n, 2):
        nei = min((nums[j] for j in [i - 1, i + 1] if 0 <= j < n), default=float('inf'))
        if nums[i] >= nei:
            res0 += nums[i] - nei + 1
    
    # Calculate moves for odd-indexed zigzag pattern
    res1 = 0
    for i in range(1, n, 2):
        nei = min((nums[j] for j in [i - 1, i + 1] if 0 <= j < n), default=float('inf'))
        if nums[i] >= nei:
            res1 += nums[i] - nei + 1
    
    # Return the minimum of the two calculated moves
    return min(res0, res1)