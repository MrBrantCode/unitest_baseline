"""
QUESTION:
Create a function `eliminate_non_even(tup)` that takes a nested heterogeneous tuple `tup` as input and returns a new tuple with all non-even elements removed. The function should recursively handle tuples embedded within other tuples. It should retain integers and numeric strings that are even, but discard non-numeric strings and non-even numbers. The function should not include floating-point numbers in the output.
"""

def eliminate_non_even(tup):
    result = []

    for elem in tup:
        if isinstance(elem, tuple):  
            result.append(eliminate_non_even(elem))  
        else: 
            if isinstance(elem, str) and elem.isdigit():  
                elem = int(elem)
            if isinstance(elem, int) and elem % 2 == 0:  
                result.append(elem)
    
    return tuple(result)