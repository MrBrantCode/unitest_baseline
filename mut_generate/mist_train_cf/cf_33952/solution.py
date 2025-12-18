"""
QUESTION:
Write a function `earliest_comparisons(comparisons)` where comparisons is a list of database comparisons with attributes `id`, `state`, `time` (a `datetime` object), and `comparison_type_id`. The function returns a list of comparisons, each representing the comparison with the earliest time for each unique `comparison_type_id`.
"""

from datetime import datetime

def earliest_comparisons(comparisons):
    earliest_times = {}
    for comp in comparisons:
        if comp.comparison_type_id not in earliest_times or comp.time < earliest_times[comp.comparison_type_id].time:
            earliest_times[comp.comparison_type_id] = comp

    return list(earliest_times.values())