"""
QUESTION:
Write a function `sort_unique_values` that takes a list of lists as input, where each sublist contains a value and an integer. The function should return a list of unique values in descending order based on their frequency of occurrence. If two values have the same frequency, they should be returned in ascending alphabetical order.
"""

def sort_unique_values(dataset):
    # Count the frequency of each unique value
    frequency_dict = {}
    for item in dataset:
        value = item[0]
        if value in frequency_dict:
            frequency_dict[value] += 1
        else:
            frequency_dict[value] = 1

    # Sort the keys of the frequency dictionary based on their values
    sorted_keys = sorted(frequency_dict.keys(), key=lambda k: (-frequency_dict[k], k))

    # Create a list of unique values in descending order based on frequency
    result = []
    for key in sorted_keys:
        result.append(key)

    return result