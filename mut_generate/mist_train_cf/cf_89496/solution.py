"""
QUESTION:
Generate all possible permutations of a list of distinct integers with possible duplicates, stored in a list of lists and returned in lexicographic order, without using built-in functions or libraries for generating permutations. The function should be implemented using an iterative approach and have a time complexity of O(n!), where n is the length of the input list.

Implement the function `generate_permutations(nums)` to achieve this.
"""

def generate_permutations(nums):
    # Sort the input list
    nums.sort()

    # Create an empty list and set
    permutations = []
    visited = set()

    # Initialize an empty stack
    stack = []

    # Push the input list onto the stack
    stack.append((nums, 0))

    # Generate permutations iteratively
    while stack:
        currentList, level = stack.pop()

        # Check if a complete permutation is generated
        if level == len(currentList):
            # Check if the permutation is not a duplicate
            permutation = tuple(currentList)
            if permutation not in visited:
                visited.add(permutation)
                permutations.append(list(permutation))
        else:
            # Generate permutations by swapping elements
            for i in range(level, len(currentList)):
                # Swap elements at level and i
                currentList[level], currentList[i] = currentList[i], currentList[level]
                # Push the updated list and level onto the stack
                stack.append((list(currentList), level + 1))
                # Swap back elements at level and i to backtrack
                currentList[level], currentList[i] = currentList[i], currentList[level]

    # Return the permutations sorted in lexicographic order
    return sorted(permutations)