"""
QUESTION:
Write a function `get_size_of_tuple` that calculates the size in bytes of a given tuple, including nested tuples, while excluding the size of any string or integer elements.
"""

import sys

def get_size_of_tuple(t):
    size = sys.getsizeof(t)

    for el in t:
        if isinstance(el, tuple):
            size += get_size_of_tuple(el) # recursively call to measure nested tuples
        elif not isinstance(el, (str, int)): 
            # add the size of non-str, non-int objects
            size += sys.getsizeof(el)
            
    return size