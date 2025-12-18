"""
QUESTION:
Create a function `generate_alerts` that generates alerts for meetings scheduled with specific attendees when the assistant is activated by the activation word "Boss". The function should take two parameters: `activation_text` and `meetings`. `activation_text` is the text that activates the assistant and `meetings` is a list of dictionaries representing the scheduled meetings, where each dictionary contains 'attendees' and 'time' as keys. The function should only generate alerts for meetings attended by specific attendees if the `activation_text` contains the word "Boss". The function should return a list of alert messages. The list of specific attendees is `['John', 'Jane', 'Michael']`.
"""

def generate_alerts(activation_text, meetings):
    specific_attendees = ['John', 'Jane', 'Michael']
    alert_messages = []
    
    if "Boss" in activation_text:
        for meeting in meetings:
            if any(attendee in specific_attendees for attendee in meeting['attendees']):
                alert_message = f"Alert: Meeting with {', '.join(meeting['attendees'])} at {meeting['time']}."
                alert_messages.append(alert_message)
    
    return alert_messages