"""
QUESTION:
Create a function `create_dictionary(keys, values)` that takes two lists, `keys` and `values`, as input. The function should return a dictionary where the elements of `keys` are the keys and the elements of `values` are the values. The function should raise an exception if the lengths of the two lists are not equal or if there are duplicate keys. All keys in the resulting dictionary must be unique and of string data type.
"""

def create_dictionary(keys, values):
    # Check if lengths of the two lists are equal
    if len(keys) != len(values):
        raise Exception("The lengths of the two lists are not equal.")
    
    # Create an empty dictionary
    result = {}
    
    # Iterate over the lists
    for i in range(len(keys)):
        # Convert the key to string if it's not already
        key = str(keys[i])
        
        # Check if the key is already present in the dictionary
        if key in result:
            raise Exception("Duplicate keys are not allowed in the dictionary.")
        
        # Add the key-value pair to the dictionary
        result[key] = values[i]
    
    return result