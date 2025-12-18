"""
QUESTION:
Create a function named `sort_dict` that takes a dictionary as input, sorts its key-value pairs in descending order based on the keys, and returns the sorted list of tuples. The function should not use built-in sorting functions; instead, it should implement a custom sorting algorithm.
"""

def sort_dict(dictionary):
    # Get the keys from the dictionary
    keys = list(dictionary.keys())

    # Implement the sorting algorithm
    for i in range(len(keys)-1):
        for j in range(i+1, len(keys)):
            if keys[i] < keys[j]:
                keys[i], keys[j] = keys[j], keys[i]

    # Create a list of key-value pairs in descending order
    sorted_list = []
    for key in keys:
        sorted_list.append((key, dictionary[key]))

    return sorted_list