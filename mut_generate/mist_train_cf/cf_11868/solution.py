"""
QUESTION:
Write a function called `count_occurrences` that takes a list and an element as input. The function should return the number of occurrences of the given element in the list, excluding any occurrences within nested sublists, and only considering elements of the same data type as the given element.
"""

def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if type(item) == list:
            count += count_occurrences(item, element)
        elif type(item) == element.__class__ and item == element:
            count += 1
    return count