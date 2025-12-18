"""
QUESTION:
Create a function called `sort_unique_values` that takes a 2D list `dataset` as input, where each sublist contains a value and a number. The function should return a list of unique values in descending order based on their frequency of occurrence in the dataset. If two values have the same frequency, they should be returned in ascending alphabetical order.
"""

def sort_unique_values(dataset):
    """
    Returns a list of unique values in descending order based on their frequency of occurrence in the dataset.
    If two values have the same frequency, they are returned in ascending alphabetical order.

    Args:
        dataset (list): A 2D list where each sublist contains a value and a number.

    Returns:
        list: A list of unique values in descending order based on frequency.
    """
    frequency_dict = {}
    for item in dataset:
        value = item[0]
        if value in frequency_dict:
            frequency_dict[value] += 1
        else:
            frequency_dict[value] = 1

    sorted_keys = sorted(frequency_dict.keys(), key=lambda k: (-frequency_dict[k], k))
    return sorted_keys