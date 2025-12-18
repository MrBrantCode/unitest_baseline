"""
QUESTION:
Write a function `analyze_data` that takes a list of dictionaries as input, groups the values by their corresponding keys, and returns a dictionary where each key is mapped to a list of its values across all input dictionaries. The function should then be used to calculate the average, minimum, and maximum of each key's values. The input list of dictionaries is obtained from parsing a list of JSON files.

The function should have a time complexity of O(n), where n is the total number of key-value pairs across all input dictionaries, and a space complexity of O(n), where n is the total number of keys and values stored in the output dictionary.
"""

from collections import defaultdict

def analyze_data(data):
    """
    This function takes a list of dictionaries as input, groups the values by their corresponding keys, 
    and returns a dictionary where each key is mapped to a list of its values across all input dictionaries.

    Args:
    data (list): A list of dictionaries.

    Returns:
    dict: A dictionary where each key is mapped to a list of its values.
    """

    # Initialize a dictionary with default values as empty lists
    results = defaultdict(list)

    # Iterate over each dictionary in the input list
    for dictionary in data:
        # Iterate over each key-value pair in the dictionary
        for key, value in dictionary.items():
            # Append the value to the list of the corresponding key in the results dictionary
            results[key].append(value)

    # Calculate the average, minimum, and maximum of each key's values
    summary = {}
    for key, values in results.items():
        summary[key] = {
            'average': sum(values) / len(values),
            'minimum': min(values),
            'maximum': max(values)
        }

    return summary