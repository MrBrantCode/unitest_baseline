"""
QUESTION:
Develop a function called `fetch_max_value` that takes a dictionary as an argument and returns the maximum value among all the values in the dictionary, including nested dictionaries. The dictionary can have multiple levels of nesting and keys can be of any data type. The function should recursively traverse the dictionary to find the maximum value.
"""

def fetch_max_value(d):
    max_value = float('-inf')

    # Iterate through all the values in the dictionary
    for value in d.values():
        # If the value is a dictionary, recursively call the function to find the max value in that dictionary
        if isinstance(value, dict):
            nested_max = fetch_max_value(value)
            max_value = max(max_value, nested_max)
        # Otherwise, update the max_value if the current value is greater
        elif isinstance(value, (int, float)) and value > max_value:
            max_value = value

    return max_value