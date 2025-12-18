"""
QUESTION:
Implement a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. The function should maintain the original order of positive and negative integers separately, and the resulting list should be sorted in ascending order with positive integers first, followed by negative integers. The function should not use any built-in methods, loops, or additional data structures, and must have a time complexity of O(n) and space complexity of O(1). The function should be implemented recursively.
"""

def remove_duplicates(nums):
    def remove_duplicates_helper(nums, index, result, seen_pos, seen_neg):
        if index == len(nums):
            return result
        
        if nums[index] not in seen_pos and nums[index] >= 0:
            seen_pos.add(nums[index])
            result.append(nums[index])
        elif nums[index] not in seen_neg and nums[index] < 0:
            seen_neg.add(nums[index])
            result.append(nums[index])
        
        return remove_duplicates_helper(nums, index + 1, result, seen_pos, seen_neg)
    
    pos = remove_duplicates_helper([num for num in nums if num >= 0], 0, [], set(), set())
    neg = remove_duplicates_helper([num for num in nums if num < 0], 0, [], set(), set())
    
    return sorted(pos) + sorted(neg)