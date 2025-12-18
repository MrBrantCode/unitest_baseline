"""
QUESTION:
Find a subset of numbers from 1 to 100 that sums up to exactly 100 using each number only once and at least 10 numbers in the subset. The function should be named `find_subset` and should take a list of numbers, a target sum, and a subset size as input. Implement this function using Python.
"""

def find_subset(numbers, target_sum, subset_size):
    """
    Find a subset of numbers that sums up to target_sum, using each number only once
    and using at least subset_size numbers in the subset.
    """
    def backtrack(start, current_sum, current_subset):
        if len(current_subset) == subset_size and current_sum == target_sum:
            return current_subset
        if current_sum > target_sum or start >= len(numbers):
            return None
        for i in range(start, len(numbers)):
            if numbers[i] in current_subset:
                continue
            result = backtrack(i+1, current_sum+numbers[i], current_subset+[numbers[i]])
            if result:
                return result
        return None
    return backtrack(0, 0, [])