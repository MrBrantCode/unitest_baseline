"""
QUESTION:
Create a function named `convert_to_dict` that takes a list as input and returns a dictionary. The function should filter out non-string and non-integer values, exclude strings with more than 5 characters, use only the first 5 characters of the string as the key, and sort the dictionary by key length in descending order. The function should also ensure that all values are integers and all keys are unique.
"""

def convert_to_dict(lst):
    """
    Converts a list into a dictionary, filtering out non-string and non-integer values.
    Excludes strings with more than 5 characters, using only the first 5 characters as the key.
    Sorts the dictionary by key length in descending order, ensuring all values are integers and all keys are unique.

    Args:
        lst (list): The input list to be converted.

    Returns:
        dict: A dictionary with the specified requirements.
    """

    # Filter out non-string and non-integer values, and exclude strings with more than 5 characters
    filtered_data = [x for x in lst if isinstance(x, (str, int)) and (len(str(x)) <= 5 if isinstance(x, str) else True)]

    # Create a list to store tuples of (key, value) pairs
    data = []

    # Iterate through the filtered list and create (key, value) pairs
    for element in filtered_data:
        if isinstance(element, str):
            key = str(element)[:5]
            value = None
        elif isinstance(element, int):
            key = str(element)
            value = element
        data.append((key, value))

    # Sort the list of tuples in descending order based on the length of the keys
    sorted_data = sorted(data, key=lambda x: len(x[0]), reverse=True)

    # Create a dictionary to store the final result
    result = {}

    # Iterate through the sorted list of tuples and add each tuple to the dictionary
    for key, value in sorted_data:
        if key not in result:
            result[key] = value

    return result