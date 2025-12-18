"""
QUESTION:
Write a function `find_kth_largest(nums, k)` that takes a list of integers `nums` and an integer `k` as input. The function should find the kth largest element in the list and return its index in the original list. If there are multiple elements with the same value, the function should return the index of the last occurrence. The length of the list will be between 1 and 10^5, and the elements in the list will be between -10^9 and 10^9. It is assumed that k is always a valid index, i.e., it will always be greater than 0 and less than or equal to the length of the list.
"""

def find_kth_largest(nums, k):
    sorted_nums = sorted(nums, reverse=True)
    kth_largest = sorted_nums[k-1]
    
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == kth_largest:
            return i
    
    return -1