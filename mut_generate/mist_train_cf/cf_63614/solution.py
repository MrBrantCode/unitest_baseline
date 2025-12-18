"""
QUESTION:
Design a function `find_element_positions` that takes in a list and an element as parameters. The function should return the index of the first occurrence of the element and a list of tuples, where each tuple contains the index and value of every occurrence of the element in the list. If the element is not found in the list, return an informative message. The function should work with lists containing any type of elements, including integers and strings.
"""

def find_element_positions(lst, element):
    if element not in lst:
        return f"The specified element is not found in the list."
    else:
        first_index = lst.index(element)
        all_positions = [(i, element) for i, el in enumerate(lst) if el == element]
        return first_index, all_positions