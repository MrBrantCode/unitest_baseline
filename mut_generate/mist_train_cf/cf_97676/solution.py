"""
QUESTION:
Create a function `calculate_sleep_schedule` that takes in the pet type (dog or cat), sleep duration in hours, and preferred sleep start time, and returns the sleep schedule for the pet, including the sleep start and end times. Assume dogs sleep for 12-14 hours and cats sleep for up to 16 hours. Use the `datetime` module to calculate the sleep times.
"""

import datetime

def calculate_sleep_schedule(pet_type, sleep_duration, preferred_sleep_start_time):
    """
    Calculate the sleep schedule for a pet based on its type and sleep duration.

    Args:
        pet_type (str): The type of pet, either 'dog' or 'cat'.
        sleep_duration (int): The duration of sleep in hours.
        preferred_sleep_start_time (datetime.time): The preferred start time of sleep.

    Returns:
        dict: A dictionary containing the sleep start and end times.
    """
    today = datetime.date.today()
    sleep_start = datetime.datetime.combine(today, preferred_sleep_start_time)
    sleep_end = sleep_start + datetime.timedelta(hours=sleep_duration)
    return {
        "sleep_start": sleep_start,
        "sleep_end": sleep_end
    }