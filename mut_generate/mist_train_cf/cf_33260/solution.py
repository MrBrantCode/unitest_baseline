"""
QUESTION:
Create a function `update_statistics` that takes in two lists (`stat_names` and `stat_values`) and optional parameters `stat_prefix` (default is `None`) and `always_show_all_stats` (default is `False`). The function should return an ordered dictionary where the keys are the statistic names (with the `stat_prefix` added if provided) and the values are the corresponding statistic values. If the lengths of `stat_names` and `stat_values` do not match, the function should only include the pairs up to the length of the shorter list.
"""

from collections import OrderedDict

def update_statistics(stat_names, stat_values, stat_prefix=None, always_show_all_stats=False):
    statistics = OrderedDict()
    for name, value in zip(stat_names, stat_values):
        if stat_prefix:
            name = f"{stat_prefix} {name}"
        statistics[name] = value
    return statistics