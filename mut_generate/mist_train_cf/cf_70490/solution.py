"""
QUESTION:
Create a function named `remove_duplicates_and_sort` that takes a list of integers as input, removes duplicates while preserving the original order of unique elements, reports the removed duplicates, and returns the sorted unique elements in descending order. The input list contains integers between -100 and 100. The solution should consider both space and time complexity.
"""

def remove_duplicates_and_sort(numbers):
    # Remove duplicates
    unique_numbers = list(dict.fromkeys(numbers))
    # Report duplicates
    duplicates = [item for item in numbers if numbers.count(item) > 1]
    print('Duplicates:', list(set(duplicates)))
    # Sort in descending order
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers