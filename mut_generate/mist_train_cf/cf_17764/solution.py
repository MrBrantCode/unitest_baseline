"""
QUESTION:
Write a function called `remove_element` that takes a list and an element as input. The function should remove all instances of the element from the list while preserving the order of the remaining elements and return the updated list along with the number of elements removed. If the input list is empty, the function should return an error message. If the element to be removed is not present in the list, the function should return -1 as the number of elements removed.
"""

def remove_element(lst, element):
    if len(lst) == 0:
        return "Error: The input list is empty."

    if element not in lst:
        return -1

    count_removed = 0
    new_lst = []

    for i in lst:
        if i != element:
            new_lst.append(i)
        else:
            count_removed += 1

    return new_lst, count_removed