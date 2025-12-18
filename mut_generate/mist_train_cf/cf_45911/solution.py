"""
QUESTION:
Create a function `tuple_to_dict` that takes a tuple as input and returns a dictionary where each element of the tuple is a key and its corresponding index is the value.
"""

def tuple_to_dict(given_tuple):
    """This function takes a tuple as input and returns a dictionary 
    where each element of the tuple is a key and its corresponding index is the value."""
    
    # Using dict comprehension to create the dictionary
    return {value: index for index, value in enumerate(given_tuple)}