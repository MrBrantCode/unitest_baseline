"""
QUESTION:
Create a function called `sort_and_filter_by_age` that sorts a list of dictionaries in descending order by the "age" field and excludes any dictionaries where the "age" is less than 30. The function should take a list of dictionaries as input and return a new list of sorted and filtered dictionaries.
"""

def sort_and_filter_by_age(data):
    """
    Sorts a list of dictionaries in descending order by the "age" field and 
    excludes any dictionaries where the "age" is less than 30.

    Args:
    data (list): A list of dictionaries, each containing an "age" field.

    Returns:
    list: A new list of sorted and filtered dictionaries.
    """
    # Sort the dictionary objects by the value of the "age" field in descending order
    sorted_data = sorted(data, key=lambda x: x["age"], reverse=True)
    
    # Filter out objects where age is less than 30
    return [obj for obj in sorted_data if obj["age"] >= 30]