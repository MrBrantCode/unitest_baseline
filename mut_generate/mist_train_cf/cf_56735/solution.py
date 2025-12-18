"""
QUESTION:
Design a function `count_event_occurrences` to determine the number of times a certain event occurs in a list of events. The function should take two parameters: a list of events and the event of interest. Return the number of times the event of interest occurs in the list of events. Assume the event of interest is a specific string and the list of events contains strings.
"""

def count_event_occurrences(events, event_of_interest):
    """
    This function determines the number of times a certain event occurs in a list of events.

    Args:
        events (list): A list of events where each event is a string.
        event_of_interest (str): The event of interest.

    Returns:
        int: The number of times the event of interest occurs in the list of events.
    """
    counter = 0
    for event in events:
        if event == event_of_interest:
            counter += 1
    return counter