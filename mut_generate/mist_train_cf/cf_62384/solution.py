"""
QUESTION:
Create a function named `transform_tuple_to_dict` that takes an input tuple of strings and returns a dictionary where the keys are the strings from the tuple and the values are the counts of each string's occurrence in the tuple. The function should handle duplicate strings in the tuple by incrementing their corresponding count in the dictionary.
"""

def transform_tuple_to_dict(input_tuple):
    # Create an empty dictionary
    output_dict = {}

    # Loop over each item in the tuple
    for item in input_tuple:
        # Add the item to the dictionary and increase the count
        output_dict[item] = output_dict.get(item, 0) + 1

    # Return the created dictionary  
    return output_dict