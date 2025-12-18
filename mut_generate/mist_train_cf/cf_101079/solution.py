"""
QUESTION:
Create a function `calculate_hours_slept` in the `SleepCalculator` class that takes the start and end times of sleep and multiple naps as input and returns the total hours slept. The function should calculate the total hours slept by adding up the duration of all the naps and subtracting that from the total time between the sleep start and end times. The input sleep times and nap times should be in a format that can be used to calculate the duration, such as datetime objects in Python. The function should be able to handle any number of naps, including zero.
"""

def calculate_hours_slept(sleep_start_time, sleep_end_time, naps=None):
    if naps is None:
        naps = []
    
    if len(naps) == 0:
        total_hours_slept = (sleep_end_time - sleep_start_time).total_seconds() / 3600.0
    else:
        total_nap_time = sum((nap[1] - nap[0]).total_seconds() / 3600.0 for nap in naps)
        total_sleep_time = (sleep_end_time - sleep_start_time).total_seconds() / 3600.0
        total_hours_slept = total_sleep_time - total_nap_time

    return total_hours_slept