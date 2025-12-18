"""
QUESTION:
Write a function `find_pairs(nums, target_sum, start_index=0, end_index=None)` that finds all pairs in a list `nums` whose sum equals `target_sum` within a given range of indices `[start_index, end_index]`. The function should handle large input lists efficiently and output the pairs in ascending order based on the first element of each pair. Note that `nums` may contain negative numbers and duplicate elements, and `end_index` defaults to the last index of `nums` if not provided. The function should use constant space complexity.
"""

def find_pairs(nums, target_sum, start_index=0, end_index=None):
    if end_index is None:
        end_index = len(nums) - 1
        
    pairs = []
    
    # Sort the list in ascending order
    nums.sort()
    
    left = start_index
    right = end_index
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target_sum:
            pairs.append((nums[left], nums[right]))
            left += 1
            right -= 1
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1
    
    return pairs