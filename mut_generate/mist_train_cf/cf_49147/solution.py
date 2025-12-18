"""
QUESTION:
Create a function called `arrayprobe` that takes an array and an element as input, and returns the index position(s) of the element in the array and the total number of operations performed during the search. If the element is not found, return a message indicating that the element is not found along with the total number of operations. The function should have a time complexity of O(n), where n is the array size.
"""

def arrayprobe(array, element):
    found_indexes = []
    operations = 0
    for i, v in enumerate(array):
        operations += 1
        if v == element:
            found_indexes.append(i)
    if len(found_indexes) > 0:
        return f'Element {element} found at {len(found_indexes)} position(s): {found_indexes}. Total operations: {operations}'
    else:
        return f'Element {element} not found. Total operations: {operations}'