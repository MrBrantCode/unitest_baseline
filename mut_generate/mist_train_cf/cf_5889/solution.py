"""
QUESTION:
Create a function named `merge_and_sort` that combines two lists, removes duplicates, and returns a new list with unique elements sorted in descending order. The input lists will contain integers.
"""

def merge_and_sort(list_1, list_2):
    """Combine two lists, remove duplicates, and return a new list with unique elements sorted in descending order."""
    final_list = list(set(list_1 + list_2))  # Combine the two lists and remove duplicates
    final_list.sort(reverse=True)  # Sort the list in descending order
    return final_list