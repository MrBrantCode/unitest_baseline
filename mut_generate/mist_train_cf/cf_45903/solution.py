"""
QUESTION:
Design a better approach for a web service to handle CRUD operations. Implement a function that takes a data object as an argument and returns a simplified representation of the data, suitable for transmission over a network. The function should not use strongly typed datasets and should be platform-independent. It should also minimize data transmission by only sending the necessary fields.
"""

def simplify_data(data_object):
    """
    This function simplifies a data object for transmission over a network.
    
    Args:
    data_object (dict): A dictionary containing data to be simplified.
    
    Returns:
    dict: A simplified representation of the data object.
    """
    # Initialize an empty dictionary to store simplified data
    simplified_data = {}
    
    # Iterate over each key-value pair in the data object
    for key, value in data_object.items():
        # Check if the value is not None or empty
        if value is not None and value != "":
            # Add the key-value pair to the simplified data dictionary
            simplified_data[key] = value
    
    # Return the simplified data
    return simplified_data