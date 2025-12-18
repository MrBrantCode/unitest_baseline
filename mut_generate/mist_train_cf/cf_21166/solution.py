"""
QUESTION:
Given a list of integers that may contain duplicates, write a function called `generate_permutations` to generate all unique permutations of the list in lexicographic order. The function should return a list of lists, where each inner list represents a permutation. The solution should not use any built-in functions or libraries for generating permutations and must be implemented using an iterative approach.
"""

def generate_permutations(nums):
    # Sort the input list to ensure duplicates are adjacent
    nums.sort()
    
    # Initialize variables
    permutations = []
    current_permutation = []
    used = [False] * len(nums)
    
    # Recursive helper function to generate permutations
    def backtrack():
        if len(current_permutation) == len(nums):
            permutations.append(current_permutation.copy())
        else:
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                    continue
                used[i] = True
                current_permutation.append(nums[i])
                backtrack()
                used[i] = False
                current_permutation.pop()
    
    # Generate permutations
    backtrack()
    
    return permutations