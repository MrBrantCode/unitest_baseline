"""
QUESTION:
Write a function `get_kth_distinct_permutation(nums, k)` that takes a list of integers `nums` and an integer `k` as input, and returns the kth distinct permutation of `nums` without using any built-in sorting functions or libraries. The function should handle duplicate elements in `nums` and not include duplicates in the permutations. The function should return an empty list if `k` is greater than the number of distinct permutations.
"""

def get_kth_distinct_permutation(nums, k):
    def backtrack(path, result, used):
        if len(path) == len(nums):
            result.append(path.copy())
            return
        
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                continue
            
            used[i] = True
            path.append(nums[i])
            backtrack(path, result, used)
            used[i] = False
            path.pop()
    
    nums.sort()  # Sort the list to handle duplicate elements
    result = []
    used = [False] * len(nums)
    backtrack([], result, used)
    
    return result[k-1] if k <= len(result) else []