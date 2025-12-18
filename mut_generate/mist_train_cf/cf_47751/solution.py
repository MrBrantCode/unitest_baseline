"""
QUESTION:
Create a function `get_events_for_month` that takes a user ID and a month (year and month) as input, and returns a list of all events for the given month, including both single and recurring events.

The events table has columns for event ID, user ID, event type, start date, and recurrence period (in days). Recurring events have a non-null recurrence period, while single events have a null recurrence period.

The function should handle recurring events that start before the given month but still occur within it, as well as recurring events that start within the given month and continue beyond it.
"""

from datetime import datetime, timedelta

def get_events_for_month(user_id, year, month):
    # Define events table
    events = [
        {'event_id': 1, 'user_id': 1, 'event_type': 'single', 'start_date': datetime(2022, 3, 1), 'recurrence_period': None},
        {'event_id': 2, 'user_id': 1, 'event_type': 'recurring', 'start_date': datetime(2022, 2, 15), 'recurrence_period': 7},
        {'event_id': 3, 'user_id': 1, 'event_type': 'recurring', 'start_date': datetime(2022, 3, 1), 'recurrence_period': 14},
        {'event_id': 4, 'user_id': 1, 'event_type': 'single', 'start_date': datetime(2022, 3, 15), 'recurrence_period': None},
    ]

    # Filter events by user ID
    user_events = [event for event in events if event['user_id'] == user_id]

    # Initialize result list
    result = []

    # Iterate over each event
    for event in user_events:
        # Check if event is a single event in the given month
        if event['recurrence_period'] is None and event['start_date'].year == year and event['start_date'].month == month:
            result.append(event)

        # Check if event is a recurring event
        elif event['recurrence_period'] is not None:
            # Calculate the first occurrence of the event in the given month
            first_occurrence = datetime(year, month, 1)
            while first_occurrence < event['start_date']:
                first_occurrence += timedelta(days=1)

            # Calculate the last occurrence of the event in the given month
            last_occurrence = datetime(year, month, 28)  # Assuming a 28-day month
            while last_occurrence.month == month:
                last_occurrence += timedelta(days=1)
            last_occurrence -= timedelta(days=1)

            # Add recurring event occurrences to the result list
            current_occurrence = event['start_date']
            while current_occurrence <= last_occurrence:
                if current_occurrence.month == month:
                    result.append({'event_id': event['event_id'], 'user_id': event['user_id'], 'event_type': event['event_type'], 'start_date': current_occurrence, 'recurrence_period': event['recurrence_period']})
                current_occurrence += timedelta(days=event['recurrence_period'])

    return result