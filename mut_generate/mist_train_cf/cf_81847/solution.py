"""
QUESTION:
Write a function called `analyze_events` that takes a dictionary of events where keys are names of people and values are lists of event names. The function should return a dictionary where keys are the names of people and values are dictionaries with three keys: 'total_events', 'unique_events', and 'unique_events_count'. The 'total_events' key should map to the total number of events each person attended, the 'unique_events' key should map to a list of unique events that each person attended and no one else did, and the 'unique_events_count' key should map to the count of these unique events.
"""

from collections import Counter

def analyze_events(events):
    # Flatten the list of all events
    all_events = [event for sublist in events.values() for event in sublist]

    # Count the occurrence of each event
    event_counts = Counter(all_events)

    # For each person, find the unique events by getting events that have count 1
    result = {
        person: {
            'total_events': len(person_events),
            'unique_events': [event for event in person_events if event_counts[event]==1],
            'unique_events_count': len([event for event in person_events if event_counts[event]==1])
        }
        for person, person_events in events.items()
    }
    
    return result