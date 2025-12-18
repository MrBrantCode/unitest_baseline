"""
QUESTION:
Create a function named `sum_of_evens` that calculates the sum of unique even numbers in a given list. The function should ignore non-numeric elements and duplicates of even numbers, only considering the first occurrence of each even number for the sum calculation. The input list can contain a mix of numeric and non-numeric elements.
"""

def sum_of_evens(lst):
    """
    Calculates the sum of unique even numbers in a given list, 
    ignoring non-numeric elements and duplicates of even numbers.

    Args:
    lst (list): A list containing a mix of numeric and non-numeric elements.

    Returns:
    int: The sum of unique even numbers in the list.
    """
    even_numbers = set()
    total_sum = 0
    for element in lst:
        if isinstance(element, int) and element % 2 == 0 and element not in even_numbers:
            even_numbers.add(element)
            total_sum += element
    return total_sum