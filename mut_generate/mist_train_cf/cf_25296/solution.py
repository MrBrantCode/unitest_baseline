"""
QUESTION:
Write a function named `permute(nums)` that generates all distinct permutations of the input list `nums`. The function should return a list of lists, where each sublist is a unique permutation of the input list.
"""

def permute(nums):
    # base case when only one element in the list
    if len(nums) == 1:
        return [nums] 
  
    permutations = []
    for i in range(len(nums)): 
        m = nums[i] 
 
        # extract remaining list 
        remain = nums[:i] + nums[i+1:] 
  
        # Iterate over remaining list and 
        # generate all permutations 
        for p in permute(remain): 
            permutations.append([m] + p) 
  
    return permutations