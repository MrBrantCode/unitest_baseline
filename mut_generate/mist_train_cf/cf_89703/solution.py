"""
QUESTION:
Write a function `filter_and_sort_dict` that takes a dictionary as input, filters out key-value pairs where the value is greater than 10, sorts the filtered pairs in descending order based on the values, and returns the sorted key-value pairs. The function should handle any potential errors or exceptions during the sorting process.
"""

def filter_and_sort_dict(input_dict):
    """
    This function filters out key-value pairs where the value is greater than 10, 
    sorts the filtered pairs in descending order based on the values, 
    and returns the sorted key-value pairs.

    Args:
        input_dict (dict): The input dictionary.

    Returns:
        list: A list of tuples containing the sorted key-value pairs.
    """

    # Filter out key-value pairs where the value is greater than 10
    filtered_pairs = {key: value for key, value in input_dict.items() if value > 10}

    try:
        # Sort the filtered pairs based on the values in descending order
        sorted_pairs = sorted(filtered_pairs.items(), key=lambda x: x[1], reverse=True)
    except Exception as e:
        print("An error occurred during sorting:", e)
    else:
        return sorted_pairs