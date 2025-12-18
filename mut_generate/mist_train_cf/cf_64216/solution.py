"""
QUESTION:
Design a function `nested_sum` that calculates the cumulative sum of all integer values within a multi-layered dictionary. The function should be able to handle dictionaries that contain other dictionaries, lists, and integer values, and ignore non-integer values. The function should return the total sum of all integer values encountered in the dictionary.
"""

def nested_sum(dic):
    total = 0
    for key, value in dic.items():
        if isinstance(value, dict):          # if value is a dictionary
            total += nested_sum(value)       # recursively call the function
        elif isinstance(value, list):        # if value is a list
            total += sum([i for i in value if isinstance(i, int)])    # sum only integer values
        elif isinstance(value, int):         # if value is an integer
            total += value
    return total