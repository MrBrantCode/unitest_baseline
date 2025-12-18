"""
QUESTION:
Write a function `purge_uneven(input_tuple)` that takes a nested tuple of heterogeneous elements (integers, floating-point numbers, and strings) as input, and returns a new tuple with the same structure but containing only the elements that are evenly divisible. For strings, only those that represent even integers are retained. All other elements, including non-numeric strings, uneven integers, and non-integer floating-point numbers, are discarded.
"""

def purge_uneven(input_tuple):
    output_list = []
    for item in input_tuple:
        if isinstance(item, tuple):
            output_list.append(purge_uneven(item))
        elif isinstance(item, str):
            try:
                if int(item) % 2 == 0:
                    output_list.append(item)
            except ValueError:
                pass
                
        elif isinstance(item, int) or isinstance(item, float):
            if item % 2 == 0:
                output_list.append(item)
    return tuple(output_list)