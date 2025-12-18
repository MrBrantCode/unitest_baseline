"""
QUESTION:
Implement a function named `permute` that generates all possible permutations of a given list of numbers, including duplicates. The function should have a time complexity of less than O(n!). The input list can contain duplicate elements, and the output should also include duplicate permutations.
"""

def permute(nums):
    result = []
    backtrack(nums, [], result)
    return result

def backtrack(nums, path, result):
    # Base case: if all numbers have been used, add the permutation to the result
    if len(nums) == 0:
        result.append(path)
        return
    
    # Recursive case: try each number in the remaining list
    for i in range(len(nums)):
        # Skip duplicate numbers to avoid unnecessary swaps
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # Choose the current number and remove it from the list
        num = nums[i]
        nums_new = nums[:i] + nums[i+1:]
        
        # Recursive call with the updated list and path
        backtrack(nums_new, path + [num], result)