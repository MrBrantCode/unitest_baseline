"""
QUESTION:
Write a function `find_kth_largest` that takes a list of integers `nums` and an integer `k` as input, and returns the kth largest element in the list. The function should have a time complexity of O(n) and a space complexity of O(1), and should not use any built-in sorting functions or modify the original list. If there are multiple elements with the same value as the kth largest element, the function can return any one of them.
"""

def find_kth_largest(nums, k):
    """
    Find the kth largest element in a list of integers.
    
    Args:
    nums (list): A list of integers.
    k (int): The position of the largest element to find (1-indexed).
    
    Returns:
    int: The kth largest element in the list.
    """
    kth_largest = float('-inf')
    for i in range(k):
        max_num = float('-inf')
        for num in nums:
            if num > max_num and (i == 0 or num < kth_largest):
                max_num = num
        kth_largest = max_num
    return kth_largest