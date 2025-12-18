"""
QUESTION:
Write a function `suggest_events` that recommends events based on a person's interests and goals. The function should take a list of interests and goals as input, and return a list of recommended events. The events and their corresponding interests and goals should be predefined.
"""

def suggest_events(interests, goals):
    """
    Recommends events based on a person's interests and goals.

    Args:
        interests (list): A list of the person's interests.
        goals (list): A list of the person's goals.

    Returns:
        list: A list of recommended events.
    """

    # Predefined events with their corresponding interests and goals
    events = {
        "TechCrunch Disrupt": ["tech", "entrepreneurship"],
        "CES": ["tech", "innovation"],
        "Google I/O": ["tech", "development"],
        "South by Southwest": ["entrepreneurship", "marketing"],
        "TED Conferences": ["inspiration", "leadership"],
        "World Economic Forum": ["economics", "politics"]
    }

    # Initialize an empty list to store recommended events
    recommended_events = []

    # Iterate over each event
    for event, event_interests in events.items():
        # Check if any of the person's interests or goals match the event's interests
        if any(interest in event_interests for interest in interests + goals):
            # If there's a match, add the event to the recommended events list
            recommended_events.append(event)

    # Return the list of recommended events
    return recommended_events