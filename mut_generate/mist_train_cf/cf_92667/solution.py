"""
QUESTION:
Given a list of numbers that may contain duplicates, write a function called `permute` that generates all possible permutations of the list, including duplicates. The function should have a time complexity less than O(n!) and should be able to handle duplicate elements in the input list. The function should return a list of all permutations.
"""

def permute(nums):
    def backtrack(nums, path, result):
        # Base case: if all numbers have been used, add the permutation to the result
        if len(nums) == 0:
            result.append(path)
            return
        
        # Sort the remaining list to group duplicate numbers together
        nums.sort()
        
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

    # Sort the input list to group duplicate numbers together
    nums.sort()
    result = []
    backtrack(nums, [], result)
    return result