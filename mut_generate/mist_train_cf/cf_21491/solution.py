"""
QUESTION:
Create a function called `updateProfileField` that takes two parameters: `fieldName` and `newValue`. This function should update the corresponding field in a user's profile document with the new value. The profile document has the following structure: 
- It contains the fields `name`, `email`, `profile_image`, `age`, and `hobbies`.
- It also contains a nested document `address` with the fields `street`, `city`, `state`, and `country`.

The function should return the updated profile document. Assume that the `fieldName` and its `newValue` will always be valid and compatible with the existing profile document structure.
"""

def updateProfileField(profile, fieldName, newValue):
    """
    Updates the corresponding field in a user's profile document with the new value.

    Args:
    profile (dict): The user's profile document.
    fieldName (str): The name of the field to update.
    newValue: The new value for the field.

    Returns:
    dict: The updated profile document.
    """

    if fieldName in profile:
        profile[fieldName] = newValue
    elif fieldName in profile['address']:
        profile['address'][fieldName] = newValue

    return profile