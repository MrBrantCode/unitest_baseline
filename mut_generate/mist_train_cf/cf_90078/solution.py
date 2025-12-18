"""
QUESTION:
Create a function named "remove_duplicates_and_sort" that takes a list of elements as input. The function should remove any non-numeric elements from the list, eliminate duplicate numbers, sort the remaining numbers in descending order, and return the sorted list. The function must handle large input lists efficiently (up to 10,000,000 elements) and support both integer and floating-point numbers.
"""

def remove_duplicates_and_sort(lst):
    numbers = [element for element in lst if isinstance(element, (int, float))]
    numbers = sorted(set(numbers), reverse=True)
    return numbers