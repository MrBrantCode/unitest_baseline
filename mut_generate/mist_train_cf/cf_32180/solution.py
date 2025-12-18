"""
QUESTION:
Implement a function `search_celestial_events(query: str, events: List[Dict[str, Any]]) -> List[Dict[str, Any]]` that takes a search query and a list of celestial event dictionaries as input. The function should return a list of event dictionaries that match the query based on the following search fields: `name`, `radiant_ra`, `radiant_dec`, `start_date`, `peak_date`, `end_date`, and `zhr`. The search should be case-insensitive and should match any part of the field value.
"""

from typing import List, Dict, Any

def entance(query: str, events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    list_display = ['name', 'radiant_ra', 'radiant_dec', 'start_date', 'peak_date', 'end_date', 'zhr']
    matching_events = []
    query = query.lower()  # Convert query to lowercase for case-insensitive search
    for event in events:
        for field in event:
            if field in list_display and query in str(event[field]).lower():
                matching_events.append(event)
                break  # Once a match is found, move to the next event
    return matching_events