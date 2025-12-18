"""
QUESTION:
Create a function named `strange_sort_list_bst` that takes a list of numbers as input, which can contain both integers and floating-point numbers. The function must return a new list where the elements are ordered in a sequence that starts with the smallest value, followed by the maximum value from the remaining elements, then the smallest value from the remaining elements, and so on. The function should handle empty lists and lists with duplicate values.
"""

def strange_sort_list_bst(lst):
    # Sort the list ascendingly by value
    lst.sort()

    # Initialize an empty list 
    new_lst = []
    while lst:
        # Alternately remove and append the smallest and largest values to the new list
        new_lst.append(lst.pop(0))
        if lst:
            new_lst.append(lst.pop(-1))

    return new_lst