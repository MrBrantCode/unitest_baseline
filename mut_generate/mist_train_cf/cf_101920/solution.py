"""
QUESTION:
Create a function `pet_sleep_schedule` that takes the pet type, sleep duration, sleep start time, and current date as inputs and returns the pet's sleep schedule. The function should calculate the sleep end time based on the sleep duration and return the sleep schedule in a formatted string. The sleep duration should be in hours and the sleep start time should be in 24-hour format (HH, MM). The function should work for both dogs and cats, but does not need to account for their individual differences in sleep patterns.
"""

import datetime

def pet_sleep_schedule(pet_type, sleep_duration, sleep_start_time, current_date):
    sleep_start = datetime.datetime.combine(current_date, sleep_start_time)
    sleep_end = sleep_start + datetime.timedelta(hours=sleep_duration)
    return f"Sleep schedule for the {pet_type}:\nSleep time: {sleep_start}\nWake time: {sleep_end}"