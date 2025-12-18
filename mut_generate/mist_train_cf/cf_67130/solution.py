"""
QUESTION:
Create a function `update_age(data, increment)` that takes a list of user objects `data` and an integer `increment` as input. The function should return a new list of user objects with each user's age incremented by the given `increment` value. If a user's age exceeds 50 after incrementing, add a new property `"senior"` set to `true`. The function must ensure that the original input `data` remains unchanged.
"""

import copy

def update_age(data, increment):
    """
    This function increments the age of each user in the given data by the specified increment.
    If a user's age exceeds 50 after incrementing, it adds a new property "senior" set to True.

    Args:
        data (list): A list of user objects.
        increment (int): The value to increment the age by.

    Returns:
        list: A new list of user objects with updated ages.
    """
    updated_data = copy.deepcopy(data)  # ensure immutability of the input
    for user in updated_data:
        user["age"] += increment  # increment age
        if user["age"] > 50:  # check if user's age exceed 50
            user["senior"] = True  # add senior property
    return updated_data