"""
QUESTION:
Create a function `enhanced_func` that takes two parameters: a list of lists `info` and a string `y`. The function should return a list of tuples where `y` is found in `info`. If `y` is found in a sublist, the tuple should contain the index of the sublist and the index of `y` within the sublist. If `y` is a key in a dictionary within a sublist, the tuple should contain the index of the sublist and the key `y`. The function should return the list of tuples sorted in ascending order.
"""

def enhanced_func(info, y):
    indices = []
    for i, sublist in enumerate(info):
        for j, value in enumerate(sublist):
            # check if the value is a list or a dictionary
            if isinstance(value, dict):
                # check if 'y' is a key in the dictionary
                if y in value:
                    indices.append((i, y))
            elif value == y:
                indices.append((i, j))
    return sorted(indices)