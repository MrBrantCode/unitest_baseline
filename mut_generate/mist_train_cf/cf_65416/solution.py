"""
QUESTION:
Write a function named `find_combinations` that takes a list of integers `candidates` and a target integer `target` as inputs, and returns all possible combinations of integers in `candidates` that sum up to `target`. Each integer in `candidates` can be used multiple times in a combination, and the order of integers in a combination matters.
"""

def find_combinations(candidates, target):
    # Initial array to store results
    results = []

    # Function to find combinations
    def find_comb(candidates, target, start, current_combination):
        # If target equals 0, we have found a combination so add it to results
        if target == 0:
            results.append(list(current_combination))
            return
        # If target becomes negative, we have crossed the target so return
        elif target < 0:
            return
        # Try each candidate by recursive call
        for i in range(start, len(candidates)):
            # Add the candidate into current combination
            current_combination.append(candidates[i])
            # Give recursive call to next
            find_comb(candidates, target - candidates[i], i, current_combination)
            # Remove the candidate from current combination
            current_combination.pop()

    # Give the initial call to find_comb
    find_comb(candidates, target, 0, [])
    return results