"""
QUESTION:
Implement the `validate_ticket_data` function, which takes a dictionary `ticket_data` as input and returns a boolean value indicating whether the data is valid based on the following rules:
- The `location` field should only contain alphanumeric characters, commas, and spaces.
- The `comment` field should only contain alphanumeric characters, commas, and spaces.
- The `status` field should only contain one of the predefined values: "resolved", "pending", or "in progress".
"""

def validate_ticket_data(ticket_data):
    """
    Validates ticket data based on predefined rules.

    Args:
        ticket_data (dict): Dictionary containing ticket data.

    Returns:
        bool: True if the data is valid, False otherwise.
    """
    return (
        all(char.isalnum() or char in (',', ' ') for char in ticket_data.get("location", ""))
        and all(char.isalnum() or char in (',', ' ') for char in ticket_data.get("comment", ""))
        and ticket_data.get("status") in ("resolved", "pending", "in progress")
    )