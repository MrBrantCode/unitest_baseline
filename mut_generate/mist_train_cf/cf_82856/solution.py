"""
QUESTION:
Develop a function named `cumulative_sum` that calculates the cumulative sum of all numerical values (integers and floats) contained within a provided list of tuples. The function should be able to navigate nested tuple structures and disregard any non-numeric entities. It should also be able to handle tuples that contain other data structures such as lists, sets, and dictionaries, and should be able to navigate these structures to find and sum all numeric values.
"""

def cumulative_sum(data):
    total = 0
    if isinstance(data, (list, tuple, set)):
        for item in data:
            total += cumulative_sum(item)
    elif isinstance(data, dict):
        for item in data.values():
            total += cumulative_sum(item)
    elif isinstance(data, (int, float)):
        total += data
    return total