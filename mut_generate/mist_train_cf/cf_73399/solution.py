"""
QUESTION:
Develop a Python function named `sort_and_remove_duplicates` that takes a list of numerical values as input, removes any duplicate values, sorts the remaining values in increasing order, and returns the sorted list along with the count of unique elements. Ensure the function raises an error if the input list contains non-numeric elements. The input list may contain integers or floating-point numbers.
"""

def sort_and_remove_duplicates(lst):
    # Ensure all elements are numbers (integers or floating point numbers)
    try:
        new_list = [float(i) for i in lst]
    except ValueError:
        return "Error: List contains non-numeric elements"
    # Remove duplicates by converting the list to a set, then convert back to a list
    new_list = list(set(new_list))
    # Sort the list in increasing order
    new_list.sort()
    # Return the sorted list and the count of unique elements
    return new_list, len(new_list)