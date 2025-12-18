"""
QUESTION:
Write a function named `find_nearest_elements_with_indices` that takes a list of float numbers as input and returns a tuple containing the two non-repetitive elements with the smallest difference between them, including their original indices. The output tuple should contain the lower value first, then its index, followed by the higher value and its index. If the two closest numbers have the same value, find the next pair of smallest distance. The function should handle lists with at least two distinct numbers.
"""

from typing import List, Tuple

def find_nearest_elements_with_indices(numbers: List[float]) -> Tuple[float, int, float, int]:
    # Pair the numbers with their original indices
    numbers_with_indices = [(num, idx) for idx, num in enumerate(numbers)]
    # Sort the numbers, but keep the original indices
    numbers_with_indices.sort()
    # Initialize variables for the two closest non-repetitive numbers and their distance
    num1, idx1, num2, idx2, min_distance = None, -1, None, -1, float('inf')
    for i in range(1, len(numbers_with_indices)):
        # If current pair of consecutive numbers have different values
        if numbers_with_indices[i][0] != numbers_with_indices[i-1][0]:
            distance = numbers_with_indices[i][0] - numbers_with_indices[i-1][0]
            if distance < min_distance:
                num1, idx1 = numbers_with_indices[i-1]
                num2, idx2 = numbers_with_indices[i]
                min_distance = distance
    return (num1, idx1, num2, idx2)