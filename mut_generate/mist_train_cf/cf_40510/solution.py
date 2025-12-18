"""
QUESTION:
Implement the function `organize_emails(headers)` that takes a list of email headers as input, where each header is a dictionary containing "name" and "value" keys, and organizes the emails into folders based on the sender's email address. The function should return a dictionary where the keys are the sender's email addresses and the values are lists of email headers from that sender. The input list of email headers is not empty, and the "From" header is always present for each email.
"""

def organize_emails(headers):
    organized_emails = {}
    for header in headers:
        if header.get("name") == 'From':
            sender = header.get("value")
            organized_emails.setdefault(sender, []).append(header)
    return organized_emails