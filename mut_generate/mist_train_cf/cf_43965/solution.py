"""
QUESTION:
Create a Python function named `morph_tuple_to_dict` that takes a tuple of strings as input. The function should convert the tuple into a dictionary where each string is a key and its value is its frequency in the tuple. The function should also return a separate dictionary with unique keys from the original tuple, where each value is 1.
"""

from collections import Counter

def morph_tuple_to_dict(input_tuple):
    # Create a Counter object to count the frequency of each item in the tuple
    count_obj = Counter(input_tuple)
    # Create a dictionary from the counter object
    my_dict = dict(count_obj)
    # Get the keys from the dictionary to create a new dictionary with unique items
    unique_dict = {key: 1 for key in my_dict.keys()}
    
    return unique_dict, my_dict