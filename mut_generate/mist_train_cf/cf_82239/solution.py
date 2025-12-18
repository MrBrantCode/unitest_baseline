"""
QUESTION:
Create a function named `sum_elements` that takes a dictionary as an argument. The function should return the total number of key-value pairs in the dictionary, considering both keys and values, including those in nested dictionaries. The dictionary can have an arbitrary level of nesting.
"""

def sum_elements(dictionary):
    # initialize the counter
    total = 0
    # iterate over each item in the dictionary
    for key, value in dictionary.items():
        # if the value is another dictionary, use recursion to count items in it
        if isinstance(value, dict):
            total += sum_elements(value)
        # if the value is not a dictionary, just count it as a single item
        else:
            total += 1
    # also consider each key as a single item
    total += len(dictionary)
    return total