"""
QUESTION:
Write a function named `sort_descending_no_duplicates` that takes a list as input, reorders it in descending order, removes any duplicate values, and returns the resulting list. The function must not use built-in Python list or sorting functions. The function should also handle the case where the input list is empty and return an empty list in this case. If the list contains non-comparable types, the function should return an error message "Error: List contains non-comparable types."
"""

def sort_descending_no_duplicates(lst):
    sorted_list = []
    while len(lst) != 0:
        maximum = None
        for value in lst:
            try:
                if not maximum:
                    maximum = value
                elif value > maximum:
                    maximum = value
            except TypeError:
                return "Error: List contains non-comparable types."
        while maximum in lst:
            lst.remove(maximum)
        sorted_list.append(maximum)
    return sorted_list