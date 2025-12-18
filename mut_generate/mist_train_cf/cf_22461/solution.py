"""
QUESTION:
Create a function named `remove_duplicates` that takes a list as an argument. The function should return a new list with duplicate elements removed, while maintaining the original order of elements. The function should only use a single loop and not use any built-in functions or libraries other than the `set` data structure.
"""

def remove_duplicates(lst):
    unique_list = []
    encountered_set = set()

    for element in lst:
        if element not in encountered_set:
            unique_list.append(element)
            encountered_set.add(element)

    return unique_list