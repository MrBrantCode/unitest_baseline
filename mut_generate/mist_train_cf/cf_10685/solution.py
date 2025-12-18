"""
QUESTION:
Write a function named `get_names` that takes a list of dictionaries as input where each dictionary contains information about an individual, including their name and age. Using recursion, return a list of names of individuals whose age is greater than 25.
"""

def get_names(data):
    # Base case: if data is empty, return an empty list
    if not data:
        return []
    
    # Recursive case
    result = []
    if "name" in data and "age" in data and data["age"] > 25:
        result.append(data["name"])
    
    # Recursively call get_names on the remaining data items
    if isinstance(data, dict) and "data" in data:
        result += get_names(data["data"])
    elif isinstance(data, list):
        for item in data:
            result += get_names(item)
    
    return result