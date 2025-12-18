"""
QUESTION:
Implement a function named `unique_permutations` that takes a list of integers as input and returns a list of unique permutations of the input list. The function should have a time complexity of O(n!*m^n) and a space complexity of O(n!), where n is the length of the input list and m is the maximum value in the list. The function should use a recursive algorithm, avoid duplicate permutations, and handle duplicate integers in the input list correctly. The output permutations should be sorted in ascending order based on the values of the integers in each permutation.
"""

def unique_permutations(nums):
    results = []
    permutation = []
    visited = [False] * len(nums)
    nums.sort()
    def generate_permutations(nums, permutation, visited, results):
        if len(permutation) == len(nums):
            results.append(permutation[:])  
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
    
    generate_permutations(nums, permutation, visited, results)
    return results