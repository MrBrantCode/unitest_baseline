"""
QUESTION:
Write a function that determines if writing files to App_Data under medium trust is possible in a .NET framework. The function should return a boolean value indicating whether writing is allowed, along with a message explaining the reason. Note that the function should not include any code execution or file system operations, but rather provide a theoretical explanation of the possibility of writing to App_Data under medium trust.
"""

def can_write_to_app_data(trust_level, has_write_permissions):
    """
    Determines if writing files to App_Data is possible in a .NET framework.

    Args:
    - trust_level (str): The trust level of the .NET framework.
    - has_write_permissions (bool): Whether the user has write permissions to the App_Data folder.

    Returns:
    - tuple: A boolean indicating whether writing is allowed and a message explaining the reason.
    """

    # Check if the trust level is medium
    is_medium_trust = trust_level.lower() == "medium"

    # Check if the user has write permissions
    if is_medium_trust and has_write_permissions:
        # Under medium trust with write permissions, writing to App_Data is allowed
        return (True, "Writing to App_Data is allowed under medium trust with write permissions.")
    elif is_medium_trust and not has_write_permissions:
        # Under medium trust without write permissions, writing to App_Data is not allowed
        return (False, "Writing to App_Data is not allowed due to lack of write permissions.")
    else:
        # Under other trust levels, writing to App_Data is not guaranteed
        return (False, "Writing to App_Data may not be allowed under this trust level.")