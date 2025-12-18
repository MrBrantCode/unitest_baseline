"""
QUESTION:
Implement a function named `get_data` that retrieves data from a deeply nested JSON array within a deeply nested JSON object. The function should take two parameters: `json_data` (the JSON object or array to search) and `index` (the index of the desired element in the array). The function should return the data at the specified index if found, or `None` otherwise. The solution should be efficient in terms of memory usage and number of iterations.
"""

def get_data(json_data, index):
    if isinstance(json_data, list):  # Check if the current data is an array
        if index < len(json_data):  # Check if the index is within the array bounds
            return json_data[index]
        else:
            return None
    elif isinstance(json_data, dict):  # Check if the current data is an object
        for key, value in json_data.items():
            result = get_data(value, index)  # Recursively call the function for nested objects
            if result is not None:
                return result
    return None