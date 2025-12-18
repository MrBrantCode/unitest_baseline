"""
QUESTION:
Write a function `sort_elements` that sorts a list of chemical elements based on their atomic numbers. The input is a list of dictionaries where each dictionary contains 'name' and 'atomic_number' keys. The function should return a list of elements sorted in increasing order of atomic number.
"""

def sort_elements(elements):
    """Sorts a list of chemical elements based on their atomic numbers."""
    sorted_elements = sorted(elements, key=lambda x: x['atomic_number'])
    return sorted_elements