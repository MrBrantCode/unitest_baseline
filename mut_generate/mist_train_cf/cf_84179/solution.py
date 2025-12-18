"""
QUESTION:
Create a function called `process_email_data` that takes in an email data object as input and returns the processed email data in a format suitable for storage in a MongoDB database. The function should be able to handle large-scale email data and ensure data integrity and security. The solution should also consider potential future enhancements and technological advancements.
"""

def process_email_data(email_data):
    """
    Process email data and return it in a format suitable for storage in a MongoDB database.

    Args:
        email_data (dict): Email data object.

    Returns:
        dict: Processed email data.
    """

    # Remove any unnecessary fields from the email data
    processed_data = {
        "from": email_data.get("from", ""),
        "to": email_data.get("to", ""),
        "subject": email_data.get("subject", ""),
        "body": email_data.get("body", ""),
    }

    # Add any additional fields required for storage in MongoDB
    processed_data["created_at"] = datetime.now()

    return processed_data