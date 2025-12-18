"""
QUESTION:
Write a function called `filter_emails_by_datetime` to filter emails based on a given datetime with millisecond precision using Outlook interop. Note that the Outlook Mail REST API does not support sub-second precision for datetime filtering. The function should account for this limitation and provide a workaround or a recommendation on how to handle this restriction.
"""

def filter_emails_by_datetime(emails, target_datetime):
    """
    Filter emails based on a given datetime with millisecond precision using Outlook interop.

    Note: The Outlook Mail REST API does not support sub-second precision for datetime filtering.
          This function will round down the target_datetime to the nearest second before filtering.

    Args:
        emails (list): A list of email objects with a 'datetime' attribute.
        target_datetime (datetime): The target datetime to filter emails by.

    Returns:
        list: A list of emails that are older than or equal to the target_datetime.
    """
    # Round down the target_datetime to the nearest second
    target_datetime = target_datetime.replace(microsecond=0)
    
    # Filter emails based on the target_datetime
    filtered_emails = [email for email in emails if email.datetime <= target_datetime]
    
    return filtered_emails