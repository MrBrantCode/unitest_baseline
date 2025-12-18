"""
QUESTION:
Write a function called `calculate_birthday_time_difference` that takes two parameters: `name` and `birthdate` (in the format "YYYY-MM-DD") as a string, and `time` (as a datetime object). The function should return the difference in time from the person's birthday to the given time.

The input `birthdate` will be constructed by appending the string " birthdate" to the `name`, then parsing it as a datetime object in the format "name birthdate" (which is equivalent to "%Y-%m-%d" but the actual date is in the format "YYYY-MM-DD" string).
"""

from datetime import datetime

def calculate_birthday_time_difference(name: str, birthdate: str, time: datetime) -> datetime:
    """
    Calculate the difference in time from the person's birthday to the given time.

    Args:
    name (str): The person's name.
    birthdate (str): The person's birthdate in the format "YYYY-MM-DD".
    time (datetime): The time to compare with the person's birthday.

    Returns:
    datetime: The difference in time from the person's birthday to the given time.
    """
    birthday = datetime.strptime(birthdate, "%Y-%m-%d")
    return time - birthday