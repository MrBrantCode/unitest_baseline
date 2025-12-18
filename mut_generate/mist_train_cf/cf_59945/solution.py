"""
QUESTION:
Write a function `remove_duplicates` that takes a list as input and returns the list with all repeated elements removed, while maintaining the original order of the remaining elements. The function should work correctly with lists containing both integers and strings, and should treat a string representation of a number and the number itself as different entities. The input list can be modified, but the original list should not be modified directly during iteration.
"""

def remove_duplicates(elements_list):
    checked = []
    for element in elements_list:
        if element not in checked:
            checked.append(element)
    return checked