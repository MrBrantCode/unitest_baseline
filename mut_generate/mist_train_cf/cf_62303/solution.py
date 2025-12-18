"""
QUESTION:
Given a numerical array and a target integer, write a function called `find_combinations` that returns all unique combinations of elements in the array that sum up to the target, ignoring the order of the elements in each combination. The function should take two parameters: `arr` (the numerical array) and `target` (the target integer). The function should return a list of combinations, where each combination is a list of numbers and duplicates are not allowed.
"""

from itertools import combinations

# Function to find unique combinations that sum up to target
def find_combinations(arr, target):
    # Create a list to store unique valid combinations
    unique_combinations = []

    # Go through array to find combinations of each length
    for r in range(1, len(arr) + 1):
        # Find all combinations of current length
        temp_combinations = list(combinations(arr, r))

        # For each combination
        for combination in temp_combinations:
            # If it sums up to desired target
            if sum(combination) == target:
                # Ensure that this combination doesn't already exist in the result list
                # For this, sort the combinations to ensure they look the same in the list
                if sorted(list(combination)) not in unique_combinations:
                    unique_combinations.append(sorted(list(combination)))

    # Return the list of unique valid combinations
    return unique_combinations