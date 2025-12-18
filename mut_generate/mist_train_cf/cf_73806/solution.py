"""
QUESTION:
Create a function named `group_by_type` that takes a dictionary as an argument. The function should iterate through the dictionary's key-value pairs and group them into separate dictionaries based on the data type of the values. The function should return a meta-dictionary where the keys are the data types (as strings) and the values are the dictionaries containing the corresponding key-value pairs.
"""

def group_by_type(dictionary):
    results = {}
    for key, value in dictionary.items():
        valueType = type(value).__name__
        if valueType not in results:
            results[valueType] = {}
        results[valueType][key] = value
    return results