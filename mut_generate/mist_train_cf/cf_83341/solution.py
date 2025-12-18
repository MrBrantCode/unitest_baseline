"""
QUESTION:
Create a Python function named `extract_domain` that takes a list of email addresses as input and returns a list of the domain sections from the valid email addresses. The function should be able to handle email addresses with varying formats, such as "john.doe@example.com", "jane_doe@example_org", or "jack-doe@example.net". If an email address does not contain an "@" symbol, the function should indicate an error or anomaly in the format of the provided email.
"""

def extract_domain(emails):
    """Extract domain from a list of email addresses"""
    try:
        return [email.split("@")[1] for email in emails if "@" in email]
    except IndexError:
        return "Anomaly in the format of provided emails."