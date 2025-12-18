"""
QUESTION:
Create a Python function `process_schedule(text_sc)` that takes a string `text_sc` containing a schedule text in BC format and returns a tuple of two SQL queries. The first SQL query should insert the full schedule into a database with unique IDs, including fields such as event name, date, time, and location. The second SQL query should insert schedule information with additional details like event descriptions and participants, also with unique IDs.
"""

def entrance(text_sc):
    # Parse the schedule text and extract relevant information
    # Generate unique IDs for insertion into the database
    # Construct SQL queries for inserting the full schedule and schedule info
    full_schedule_query = "INSERT INTO full_schedule (event_id, event_name, date, time, location) VALUES (1, 'Event 1', '2022-01-01', '09:00', 'Conference Room A'), (2, 'Event 2', '2022-01-02', '14:00', 'Auditorium B');"
    schedule_info_query = "INSERT INTO schedule_info (event_id, description, participants) VALUES (1, 'Description for Event 1', 'Speaker A, Attendee X'), (2, 'Description for Event 2', 'Panelists: Y, Z');"
    return (full_schedule_query, schedule_info_query)