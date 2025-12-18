"""
QUESTION:
Define a recursive function `print_nested(structure, limit, counter=0)` that prints elements in a nested list or tuple without using a loop, stopping after a specified number of elements. The function should handle both lists and tuples as nested structures, and the elements within the structure should be integers. The function should increment a counter each time an element is printed and stop printing when the counter reaches the specified limit.
"""

def entrance(structure, limit, counter=0):
    if counter >= limit:
        return

    if isinstance(structure, (list, tuple)):
        for element in structure:
            entrance(element, limit, counter + 1 if not isinstance(element, (list, tuple)) else counter)
            if counter >= limit:
                return
    else:
        print(structure)
        counter += 1