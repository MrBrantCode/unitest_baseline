"""
QUESTION:
Write a function called `generate_ics_file` that generates an ICS (iCalendar) file content given the following parameters: 
- `event_title`: the title of the event
- `start_datetime`: the start date and time of the event as a datetime object
- `end_datetime`: the end date and time of the event as a datetime object
- `location`: the location of the event
- `description`: a brief description of the event
- `organizer_email`: the email address of the event organizer
- `attendee_email`: the email address of the attendee (optional)

The function should return the ICS content as a string in the standard ICS format.
"""

import datetime

def generate_ics_file(event_title, start_datetime, end_datetime, location, description, organizer_email, attendee_email=None):
    ics_content = f"BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//hacksw/handcal//NONSGML v1.0//EN\nBEGIN:VEVENT\nSUMMARY:{event_title}\nDTSTART:{start_datetime.strftime('%Y%m%dT%H%M%S')}\nDTEND:{end_datetime.strftime('%Y%m%dT%H%M%S')}\nLOCATION:{location}\nDESCRIPTION:{description}\nORGANIZER;CN=Organizer:mailto:{organizer_email}\n"
    
    if attendee_email:
        ics_content += f"ATTENDEE;RSVP=TRUE:mailto:{attendee_email}\n"
    
    ics_content += "END:VEVENT\nEND:VCALENDAR"
    
    return ics_content