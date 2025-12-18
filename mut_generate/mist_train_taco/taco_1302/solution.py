"""
QUESTION:
You are given an array nums. Your task is to complete the function getXor to return the XOR of the given range a and b.
 
Example 1:
Input: nums = {1, 3, 5, 7, 9, 11}
,a = 1, b = 3
Output: 1
Explanation: 3^5^7 = 1
Example 2:
Input: nums = {1, 2, 3, 4, 5}
a = 0, b = 4
Output: 1
 
Your Task:
You don't need to read or print anyhting. Your task is to comlplete the function getXor() which takes nums, a and b as input parameter and returns the xor from a to b.
 
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)
 
Constraints:
1 ≤ n ≤ 10^{5}
0 ≤ a ≤ b < n
1 ≤ nums[i] ≤ 100
"""

def calculate_range_xor(nums: list[int], a: int, b: int) -> int:
    """
    Calculate the XOR of all elements in the range [a, b] in the array nums.

    Parameters:
    - nums (list[int]): The array of integers.
    - a (int): The starting index of the range (inclusive).
    - b (int): The ending index of the range (inclusive).

    Returns:
    - int: The XOR of all elements in the range [a, b].
    """
    result = 0
    for i in range(a, b + 1):
        result ^= nums[i]
    return result