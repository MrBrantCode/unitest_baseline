"""
QUESTION:
Extract all values from a list of dictionaries while maintaining the original order, considering nested dictionaries and lists.

Create a function named `extract_values` that takes an element as input. The element can be a dictionary, a list, or a single value. The function should handle nested dictionaries and lists, and return a list of extracted values in the original order.
"""

def extract_values(element):
    """
    Function to extract values from an element which could be dictionary, list or a single value
    """

    # Create an empty list to store values
    values = []

    # Case if the element is a list
    if isinstance(element, list):
        for item in element:
            # Recursion to handle nested lists or dictionaries
            values.extend(extract_values(item))

    # Case if the element is a dictionary
    elif isinstance(element, dict):
        for key, value in element.items():
            # Recursion to handle nested lists or dictionaries
            values.extend(extract_values(value))

    else:
        # add the value to the list if it's neither dict or list
        values.append(element)

    return values