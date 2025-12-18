"""
QUESTION:
Write a function `nested_sum` that takes one argument `data` and returns the cumulative sum of all integer values in the given nested dictionary. The dictionary may contain dictionaries, lists, integer values, and strings. The function should ignore non-integer values and handle circular references without entering an infinite loop. If a `seen` set is not provided, the function should create one internally.
"""

def nested_sum(data, seen=None):
    if seen is None:
        seen = set()
    if id(data) in seen:
        return 0
    seen.add(id(data))
    sum_values = 0
    if isinstance(data, dict):
        values = data.values()
    elif isinstance(data, (list, tuple)):
        values = data
    else:
        values = []
    for value in values:
        if isinstance(value, int):
            sum_values += value
        elif isinstance(value, (dict, list, tuple)):
            sum_values += nested_sum(value, seen)
    return sum_values