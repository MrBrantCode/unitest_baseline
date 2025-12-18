"""
QUESTION:
Create a function named `generate_invitation` to generate a formal invitation for a networking event in Markdown format. The function should take the following parameters: `event_name`, `date_and_time`, `location`, `rsvp_email`, and `purpose`. The function should return a string representing the Markdown invitation. The invitation should include the event name as a level 1 heading, date and time, location, purpose, and RSVP instructions as level 2 headings.
"""

def generate_invitation(event_name, date_and_time, location, rsvp_email, purpose):
    """
    Generate a formal invitation for a networking event in Markdown format.

    Args:
    event_name (str): The name of the event.
    date_and_time (str): The date and time of the event.
    location (str): The location of the event.
    rsvp_email (str): The email address for RSVPs.
    purpose (str): The purpose of the event.

    Returns:
    str: A string representing the Markdown invitation.
    """
    invitation = f"# {event_name}\n## {date_and_time}\n## {location}\n## Purpose\n{purpose}\n## RSVP\nTo RSVP, please email {rsvp_email}."
    return invitation