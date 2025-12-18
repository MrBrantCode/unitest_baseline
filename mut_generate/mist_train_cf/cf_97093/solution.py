"""
QUESTION:
Create a function named `remove_duplicates` that takes a list as input and returns a new list containing the original elements in the original order but without any duplicates. The function should use only a single loop and not rely on any built-in functions or libraries.
"""

def remove_duplicates(lst):
    unique_list = []
    encountered_set = set()

    for element in lst:
        if element not in encountered_set:
            unique_list.append(element)
            encountered_set.add(element)

    return unique_list