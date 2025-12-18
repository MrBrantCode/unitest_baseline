"""
QUESTION:
Create a function `find_distinct` that takes two lists, `first_array` and `second_array`, as input. The function should return a list of distinct elements that are present in exactly one of the input lists. Note that the order of elements in the output list may vary.
"""

def find_distinct(first_array, second_array):
    # Convert the arrays into sets
    first_set = set(first_array)
    second_set = set(second_array)
    
    # Find the distinct elements in both sets.
    # By using the symmetric difference (^) operator here, we get all elements that are in exactly one of the sets.
    distinct_elements = first_set ^ second_set
    
    # Convert the set back into a list
    distinct_list = list(distinct_elements)
    
    # Return the list of distinct elements
    return distinct_list