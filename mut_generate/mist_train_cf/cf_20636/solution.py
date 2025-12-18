"""
QUESTION:
Write a function `find_kth_distinct_permutation(nums, k)` that finds the kth distinct permutation of a given list of integers `nums`. The function should handle duplicate elements in the list and return the kth distinct permutation without duplicates. The list `nums` is not guaranteed to be sorted and may contain duplicate elements. The function should return `None` if the kth distinct permutation is not found.
"""

def findKthDistinctPermutation(nums, k):
    nums.sort()
    counter = [0]
    
    def permute(index, permutation):
        if index == len(nums):
            counter[0] += 1
            if counter[0] == k:
                return permutation
        else:
            for i in range(index, len(nums)):
                if i != index and nums[i] == nums[index]:
                    continue
                nums[index], nums[i] = nums[i], nums[index]
                result = permute(index + 1, permutation + [nums[index]])
                nums[index], nums[i] = nums[i], nums[index]
                if result:
                    return result
    
    return permute(0, [])