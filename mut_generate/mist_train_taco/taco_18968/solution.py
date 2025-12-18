"""
QUESTION:
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:


Input: [2,2,1]
Output: 1


Example 2:


Input: [4,1,2,1,2]
Output: 4
"""

def find_single_number(nums: list[int]) -> int:
    """
    Finds the single number in a list where every other element appears twice.

    Parameters:
    nums (list[int]): A non-empty list of integers.

    Returns:
    int: The single number that appears only once in the list.
    """
    if len(nums) == 1:
        return nums[0]
    
    result = 0
    for num in nums:
        result ^= num
    
    return result