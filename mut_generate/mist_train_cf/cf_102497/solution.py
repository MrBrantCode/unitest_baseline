"""
QUESTION:
Write a function `compute_mode_and_range` that takes a list of integers as input and returns a tuple containing the mode (most frequently occurring number(s)) and the range (difference between the maximum and minimum numbers) of the list. The function should be able to handle duplicates in the list.
"""

def compute_mode_and_range(numbers):
    """
    This function calculates the mode and range of a given list of integers.

    Args:
    numbers (list): A list of integers.

    Returns:
    tuple: A tuple containing the mode and the range of the input list.
    """
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]

    mode = modes[0] if len(modes) == 1 else modes
    range_ = max(numbers) - min(numbers)
    
    return mode, range_