"""
QUESTION:
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:

Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.



Example 2:

Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.



Example 3:

Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""

def find_third_max(nums: list[int]) -> int:
    # Convert the list to a set to remove duplicates, then back to a list and sort it
    nums = sorted(list(set(nums)))
    
    # Check the length of the sorted list
    if len(nums) < 3:
        # If there are less than 3 distinct numbers, return the maximum number
        return max(nums)
    else:
        # Otherwise, return the third maximum number
        return nums[-3]