"""
QUESTION:
Write a function `get_kth_distinct_permutation` that takes a list of integers `nums` and an integer `k` as input, and returns the kth distinct permutation of the input list without duplicates. The function should not use any built-in sorting functions or libraries. If `k` is greater than the number of distinct permutations, the function should return an empty list.
"""

def get_kth_distinct_permutation(nums, k):
    def backtrack(nums, k, path, result, used):
        if len(path) == len(nums):
            result.append(path.copy())
            return
        
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                continue
            
            used[i] = True
            path.append(nums[i])
            backtrack(nums, k, path, result, used)
            used[i] = False
            path.pop()
    
    nums.sort()  # Sort the list to handle duplicate elements
    result = []
    used = [False] * len(nums)
    backtrack(nums, k, [], result, used)
    
    return result[k-1] if k <= len(result) else []