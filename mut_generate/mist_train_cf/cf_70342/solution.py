"""
QUESTION:
Develop a function named `search_insert` that takes a sorted list of integers (`nums`) and a target integer (`target`) as parameters. The function should return the index of the first occurrence of `target` in `nums` if it exists, otherwise return the index where `target` should be inserted to maintain the sorted order of `nums`. The function should handle edge cases where `nums` is empty or contains a single element, and it should be efficient enough to handle large lists of up to 1 million elements.
"""

def search_insert(nums, target):
    if not nums:
        return 0
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low