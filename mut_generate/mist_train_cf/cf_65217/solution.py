"""
QUESTION:
Write a function named `find_pair` that takes a list of integers `numbers` and an integer `target_sum` as input. The function should return a tuple containing a pair of numbers from the list that add up to `target_sum` if such a pair exists, otherwise return `None`. Assume that there is at most one pair of numbers in the list that sum up to `target_sum`.
"""

def find_pair(numbers, target_sum):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                return (numbers[i], numbers[j])
    return None