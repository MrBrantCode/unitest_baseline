"""
QUESTION:
Design a function named `update_age` that takes two boolean parameters: `isAdult` and `isOld`, and updates the variable `age` accordingly. If `isAdult` is True, assign `age` to 18. If `isAdult` is False and `isOld` is True, increment the current value of `age` by 1.
"""

def update_age(isAdult, isOld, age):
    """
    Updates the age based on the given conditions.

    Args:
        isAdult (bool): Whether the person is an adult.
        isOld (bool): Whether the person is old.
        age (int): The current age of the person.

    Returns:
        int: The updated age.
    """
    if isAdult:
        return 18
    elif not isAdult and isOld:
        return age + 1
    else:
        return age