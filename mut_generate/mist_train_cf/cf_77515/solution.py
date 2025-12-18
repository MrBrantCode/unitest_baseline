"""
QUESTION:
Create a function `dict_cumulative_sum` that calculates the cumulative sum of all integers in a multi-tiered dictionary, which may contain other dictionaries, lists, tuples, and integers. The function should handle nested data structures of arbitrary depth.
"""

def dict_cumulative_sum(d):
    total = 0
    for key, val in d.items():
        if isinstance(val, int):
            total += val
        elif isinstance(val, dict):
            total += dict_cumulative_sum(val)
        elif isinstance(val, (list, tuple)):
            for item in val:
                if isinstance(item, int):
                    total += item
                elif isinstance(item, dict):
                    total += dict_cumulative_sum(item)
                elif isinstance(item, (list, tuple)):
                    total += sum(i for i in item if isinstance(i, int))
    return total