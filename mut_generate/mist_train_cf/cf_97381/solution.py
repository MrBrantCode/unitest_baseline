"""
QUESTION:
Define a recursive function `print_nested(structure, limit, counter=0)` to print out the elements in a nested list or tuple without using a loop, stopping after a specified number of elements. The function should handle both nested lists and tuples and only print integers. The `structure` argument is the nested list or tuple, and the `limit` argument is the maximum number of elements to print.
"""

def entrance(structure, limit, counter=0):
    if counter >= limit:
        return

    if isinstance(structure, (list, tuple)):
        for element in structure:
            entrance(element, limit, counter + (1 if isinstance(element, int) else 0))
    else:
        print(structure)
        counter += 1