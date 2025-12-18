"""
QUESTION:
Implement a function `sort_and_deduplicate(numbers)` that takes a list of integers as input and returns the sorted list in ascending order with duplicates removed. The function should not use any built-in sorting or deduplication functions or methods. It should implement its own sorting and deduplication algorithms from scratch. Additionally, the function should handle any errors or exceptions that may occur during the sorting and deduplication processes.
"""

def sort_and_deduplicate(numbers):
    """
    This function takes a list of integers as input, sorts it in ascending order using Bubble Sort algorithm, 
    removes duplicates, and returns the sorted list.

    Args:
    numbers (list): A list of integers

    Returns:
    list: A sorted list of integers in ascending order with duplicates removed
    """
    # Bubble Sort Algorithm
    n = len(numbers)
    for i in range(n-1):
        for j in range(n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    # Deduplication
    deduplicated_numbers = []
    for number in numbers:
        if number not in deduplicated_numbers:
            deduplicated_numbers.append(number)

    return deduplicated_numbers