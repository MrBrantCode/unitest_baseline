"""
QUESTION:
Create a function named `list_processing` that takes a list as an input. The function should check if all elements in the list are either integers or strings. If the list only contains integers or strings, convert it to a tuple after removing duplicates, and return the new tuple along with the number of unique elements. If the list contains elements other than integers or strings, return a message indicating this.
"""

def list_processing(my_list):
    # Checks if all elements are either integer or string
    valid_types = [int, str]
    if all(type(x) in valid_types for x in my_list):
        # Convert the list to a set to remove duplicated and then convert it to a tuple
        new_tuple = tuple(set(my_list))
        # Return the new tuple and the number of unique elements
        return new_tuple, len(new_tuple)
    else:
        # In case if there are elements in the list other than integers and strings
        return "List contains non-string or non-integer elements"