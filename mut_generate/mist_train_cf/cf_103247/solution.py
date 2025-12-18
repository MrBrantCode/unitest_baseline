"""
QUESTION:
Write a function `sort_and_filter_by_age` that sorts a list of dictionary objects by the value of the "age" field in descending order, excluding any objects where the "age" is less than 30.
"""

def sort_and_filter_by_age(data):
    """
    Sorts a list of dictionary objects by the value of the "age" field in descending order, 
    excluding any objects where the "age" is less than 30.

    Args:
        data (list): A list of dictionary objects.

    Returns:
        list: A list of dictionary objects sorted by the "age" field in descending order, 
              excluding objects with an age less than 30.
    """
    return [obj for obj in sorted(data, key=lambda x: x["age"], reverse=True) if obj["age"] >= 30]