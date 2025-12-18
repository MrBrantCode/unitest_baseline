"""
QUESTION:
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:


Input: [3,2,1,5,6,4] and k = 2
Output: 5


Example 2:


Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

def find_kth_largest(nums, k):
    """
    Find the kth largest element in an unsorted array.

    Parameters:
    - nums (list of int): The unsorted array of integers.
    - k (int): The position of the kth largest element to find.

    Returns:
    - int: The kth largest element in the sorted order of the array.
    """
    nums = sorted(nums, reverse=True)
    return nums[k - 1]