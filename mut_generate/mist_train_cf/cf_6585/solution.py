"""
QUESTION:
Generate the function `generate_permutations(nums)` that takes a list of integers `nums` and returns a list of lists containing all unique permutations of `nums` in lexicographic order. The function should not use any built-in functions or libraries for generating permutations and should handle duplicates in the input list by only including unique combinations in the output. The function should be implemented using an iterative approach with a time complexity of O(n!), where n is the length of the input list.
"""

def generate_permutations(nums):
    # Step 1: Sort the input list
    nums.sort()

    # Step 2: Create an empty list and set
    permutations = []
    visited = set()

    # Step 3: Initialize an empty stack
    stack = []

    # Step 4: Push the input list onto the stack
    stack.append((nums, 0))

    # Step 6: Generate permutations iteratively
    while stack:
        currentList, level = stack.pop()

        # Step 6.1: Check if a complete permutation is generated
        if level == len(currentList):
            # Step 6.1.1: Check if the permutation is not a duplicate
            permutation = tuple(currentList)
            if permutation not in visited:
                visited.add(permutation)
                permutations.append(list(permutation))
        else:
            # Step 6.2: Generate permutations by swapping elements
            for i in range(level, len(currentList)):
                # Swap elements at level and i
                currentList[level], currentList[i] = currentList[i], currentList[level]
                # Push the updated list and level onto the stack
                stack.append((list(currentList), level + 1))
                # Swap back elements at level and i to backtrack
                currentList[level], currentList[i] = currentList[i], currentList[level]

    # Step 7: Return the permutations sorted in lexicographic order
    return sorted(permutations)