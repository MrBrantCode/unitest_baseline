"""
QUESTION:
Create a function named `remove_duplicates_and_sort` that takes a list as input, removes non-numeric elements, removes duplicate numbers, sorts the remaining numbers in descending order, and returns the sorted list. The function should be able to handle large input lists with up to 10,000,000 elements efficiently. The input list can contain integers and floats, but the function should treat them as numbers and perform the operations accordingly.
"""

def remove_duplicates_and_sort(lst):
    numbers = [element for element in lst if isinstance(element, (int, float))]
    return sorted(set(numbers), reverse=True)