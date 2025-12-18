"""
QUESTION:
Given a list of integers `nums` and an integer `L`, write a function `min_moves` to find the minimum number of moves required to make all elements in `nums` equal. A move increments `n - 1` elements by 1, but no element can exceed `L`. The function should return -1 if it's impossible to make all elements equal without exceeding the limit. 

Restrictions: 
- `1 <= len(nums) <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= L <= 10^9`
"""

from typing import List

def min_moves(nums: List[int], L: int) -> int:
    """
    This function calculates the minimum number of moves required to make all elements in 'nums' equal.
    A move increments 'n - 1' elements by 1, but no element can exceed 'L'.
    The function returns -1 if it's impossible to make all elements equal without exceeding the limit.
    
    Parameters:
    nums (List[int]): A list of integers
    L (int): The maximum limit for the elements in 'nums'
    
    Returns:
    int: The minimum number of moves required, or -1 if it's impossible
    """
    high = max(max(nums), L)
    low = min(nums)

    while low <= high:
        mid = low + (high - low) // 2
        total = sum((mid - num) for num in nums)

        if total > mid or mid > L:
            return -1
        if total <= mid:
            high = mid - 1
        else:
            low = mid + 1
    return high