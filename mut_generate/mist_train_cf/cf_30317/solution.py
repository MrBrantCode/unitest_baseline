"""
QUESTION:
Implement a function `group_events_by_date(events)` that takes a list of event dictionaries as input, where each dictionary contains a 'date' key, and returns a dictionary where the keys are the dates and the values are lists of events that occurred on that date. The function should handle empty input and return an empty dictionary in such cases.
"""

from itertools import groupby

def group_events_by_date(events):
    groups = groupby(sorted(events, key=lambda o: o['date']), lambda o: o['date'])
    grouped_events = {
        date: list(events)
        for date, events in groups
    }
    return grouped_events