"""
QUESTION:
Write a function `find_pairs(numbers, target_sum)` that finds all unique pairs in a sorted list `numbers` that sum up to `target_sum` without using additional space. The function should return the number of such pairs and list them in ascending order. The function should be designed to be executed in a multithreaded environment.
"""

def find_pairs(numbers, target_sum):
    """
    Finds all unique pairs in a sorted list that sum up to target_sum.

    Args:
    numbers (list): A sorted list of numbers.
    target_sum (int): The target sum that pairs should add up to.

    Returns:
    tuple: A tuple containing the number of pairs and a list of pairs.
    """

    left_index = 0
    right_index = len(numbers) - 1
    pairs = []

    while left_index < right_index:
        # Calculate sum of pair
        current_sum = numbers[left_index] + numbers[right_index]

        if current_sum == target_sum:
            pairs.append((numbers[left_index], numbers[right_index]))
            left_index += 1
            right_index -= 1
        elif current_sum < target_sum:
            left_index += 1
        else:
            right_index -= 1

    pairs.sort()  # Ensure pairs are sorted
    return len(pairs), pairs