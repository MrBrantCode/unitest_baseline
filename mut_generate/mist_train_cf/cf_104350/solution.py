"""
QUESTION:
Create a function named `classify_elements` that takes a list of elements as input and returns a new list where each element appears only once and is sorted in alphabetical order. The function should also return the count of unique elements in the list.
"""

def classify_elements(elements):
    """
    This function takes a list of elements, removes duplicates, 
    sorts them in alphabetical order, and returns the sorted list along with the count of unique elements.

    Args:
        elements (list): A list of elements

    Returns:
        tuple: A tuple containing the sorted list of unique elements and the count of unique elements
    """
    unique_elements = sorted(set(elements))
    return unique_elements, len(unique_elements)