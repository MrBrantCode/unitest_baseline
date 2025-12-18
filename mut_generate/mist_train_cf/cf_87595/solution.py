"""
QUESTION:
Given a list of integers, implement a function named `unique_permutations` that generates all unique permutations of the list. The function should use a recursive algorithm, handle duplicate integers, and ensure that the output permutations are in ascending order. The function should also avoid generating duplicate permutations by skipping elements that are duplicates of previously unvisited elements.
"""

def unique_permutations(nums):
    def generate_permutations(nums, permutation, visited, results):
        if len(permutation) == len(nums):
            results.append(permutation[:])  # Append a copy of the permutation to the results
            return
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue
            visited[i] = True
            permutation.append(nums[i])
            generate_permutations(nums, permutation, visited, results)
            visited[i] = False
            permutation.pop()

    results = []
    permutation = []
    visited = [False] * len(nums)
    nums.sort()  # Sort the input list to ensure ascending order in output permutations
    generate_permutations(nums, permutation, visited, results)
    return results