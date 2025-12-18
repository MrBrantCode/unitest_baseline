"""
QUESTION:
Write a function `find_subset` that finds a subset of a given list of numbers that sums up to a target sum. The function should use each number in the list at most once and return the subset as a list. If no such subset exists, the function should return `None`. The function should be optimized to minimize time complexity.
"""

def find_subset(numbers, target_sum):
    for i in range(len(numbers)):
        remaining_sum = target_sum - numbers[i]
        if remaining_sum == 0:
            return [numbers[i]]
        else:
            subset = find_subset(numbers[i+1:], remaining_sum)
            if subset:
                return [numbers[i]] + subset
    return None