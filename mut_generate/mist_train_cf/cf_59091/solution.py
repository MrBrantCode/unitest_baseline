"""
QUESTION:
Write a recursive function `find_smallest` that finds the smallest integer in a list of integers or nested lists of varying depths. The function should return the smallest integer and its depth, with the depth of the outermost list considered as 0. The function should handle the possibility of empty lists or sublists.
"""

def find_smallest(input_list, depth=0):
    smallest = None
    smallest_depth = None

    for element in input_list:
        if isinstance(element, list):
            if element:  
                s, d = find_smallest(element, depth+1)
                if smallest is None or (s is not None and s < smallest):
                    smallest = s
                    smallest_depth = d
        else: 
            if smallest is None or element < smallest:
                smallest = element
                smallest_depth = depth

    return smallest, smallest_depth