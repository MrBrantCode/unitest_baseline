"""
QUESTION:
Design a function named `revised_function` that takes a tuple of float values as input. The function should return a semicolon-separated string representation of these float values. If the input tuple is NULL or contains non-float elements, the function should return a specific error message. The input tuple can be empty or contain any number of float values.
"""

def revised_function(input_tuple):
    # Checks if the tuple is None or empty 
    if not input_tuple:
        return "Error: input is NULL or empty."

    # Initiating an empty list to hold string representations of the float values
    str_list = []

    # Iterate over the elements in the tuple
    for element in input_tuple:
        # Confirm that each element is a float. If not, return an error message.
        if not isinstance(element, float):
            return "Error: all elements in the tuple should be floats."
            
        # Convert the float to a string and append to the list
        str_list.append(str(element))
    
    # Join all elements in the list with a semicolon
    result = "; ".join(str_list)
    
    return result