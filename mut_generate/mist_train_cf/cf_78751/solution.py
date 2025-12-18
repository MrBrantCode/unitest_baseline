"""
QUESTION:
Write a function `find_nearest_elements_with_indices` that takes a list of distinct or non-distinct float numbers as input. The function must return a tuple containing a pair of distinct numbers with the smallest absolute difference in the list, along with their corresponding indices. The numbers in the output tuple should be in ascending order, and the indices should be in the order they appear in the list.
"""

from typing import List, Tuple

def find_nearest_elements_with_indices(numbers: List[float]) -> Tuple[float, int, float, int]:
    smallest_difference = float('inf')
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            difference = abs(numbers[i] - numbers[j])
            if difference < smallest_difference:
                smallest_difference = difference
                smallest_pair = (min(numbers[i], numbers[j]), i, max(numbers[i], numbers[j]), j) if numbers[i] < numbers[j] else (min(numbers[i], numbers[j]), j, max(numbers[i], numbers[j]), i)
    return smallest_pair