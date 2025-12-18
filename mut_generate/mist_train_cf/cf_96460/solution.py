"""
QUESTION:
Write a function named `generate_permutations` that generates all unique permutations of a given list of integers in lexicographic order, without using any built-in permutation functions or libraries. The function should handle duplicate elements in the input list by only including unique combinations in the output. The output should be a list of lists, where each inner list represents a permutation. The function should use an iterative approach instead of recursion.
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