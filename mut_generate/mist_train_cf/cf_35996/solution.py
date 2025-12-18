"""
QUESTION:
Implement the `parse_mail` function to extract the sender's email address, subject of the email, and date and time the email was sent from each email in an mbox format file. The function should take the path to the mbox file as input and return a list of dictionaries, where each dictionary contains the extracted information for a single email. The 'date_sent' value should be a datetime object. Use the `mailbox` and `email.utils` modules.
"""

import mailbox
from email.utils import parsedate_to_datetime

def parse_mail(file_path):
    emails_data = []
    mbox = mailbox.mbox(file_path)
    
    for message in mbox:
        sender = message['From']
        subject = message['Subject']
        date_sent = parsedate_to_datetime(message['Date'])
        
        email_info = {
            'sender': sender,
            'subject': subject,
            'date_sent': date_sent
        }
        emails_data.append(email_info)
    
    return emails_data