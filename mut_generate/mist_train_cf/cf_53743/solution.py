"""
QUESTION:
Write a function `convert_to_minutes` that takes a string representing time in the format 'HH:MM:SS' and returns the total minutes as a float. The function should be able to handle a large dataset and be efficient enough to apply to a pandas Series.
"""

from datetime import datetime

def convert_to_minutes(x):
    _time = datetime.strptime(x, "%H:%M:%S")
    return _time.hour * 60 + _time.minute + _time.second / 60