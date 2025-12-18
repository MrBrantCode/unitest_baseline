"""
QUESTION:
Write a function `organize_events(events)` that takes a list of tuples as input, where each tuple contains a month (integer), a day (integer), and an event name (string). The function should return a dictionary where the keys are the months and the values are lists of event names that occur in that month. If an event occurs in multiple months, it should be listed under each applicable month. The function should handle months that do not exist in the input list, creating a new entry in the dictionary as needed.
"""

def organize_events(events):
    event_dict = {}
    for event in events:
        month = event[0]
        event_name = event[2]
        if month in event_dict:
            event_dict[month].append(event_name)
        else:
            event_dict[month] = [event_name]
    return event_dict