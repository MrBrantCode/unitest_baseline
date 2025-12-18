"""
QUESTION:
Develop a function `find_pairs(nums, target_sum, start_index=0, end_index=None)` that takes a list of integers `nums`, an integer `target_sum`, and optional parameters `start_index` and `end_index` as input, and returns a list of tuples, where each tuple contains a pair of integers whose sum is equal to the `target_sum`. The function should find all pairs within the given range of indices in the list that sum up to the target sum, handle large input lists efficiently, output the pairs in ascending order based on the first element of each pair, and only use constant space complexity, without using any additional data structures.
"""

def find_pairs(nums, target_sum, start_index=0, end_index=None):
    if end_index is None:
        end_index = len(nums) - 1
        
    nums.sort()
    
    left = start_index
    right = end_index
    
    pairs = []
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