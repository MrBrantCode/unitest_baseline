"""
QUESTION:
Develop a function named `two_smallest_unique_numbers` that takes a list of twenty numbers as input. The list may contain integers, floating point numbers, and may also include negative numbers. The function should return the two smallest unique values within the list without using pre-existing minimum functions. The function should handle cases where the list contains duplicate numbers and cases where all numbers are the same.
"""

def two_smallest_unique_numbers(numbers):
    # First sort the list
    sorted_numbers = sorted(numbers)

    # Find the first two unique numbers
    results = []
    i = 0
    while len(results) < 2 and i < len(sorted_numbers):
        if sorted_numbers[i] not in results:
            results.append(sorted_numbers[i])
        i += 1

    return results