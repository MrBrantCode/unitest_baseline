"""
QUESTION:
Write a function `convert_to_military` that takes a string representing a 12-hour time in the format "hh:mm:ss AM/PM" and returns a string representing the equivalent time in 24-hour format "hh:mm:ss". The input is case-sensitive, so "AM" and "PM" should be in uppercase.
"""

from datetime import datetime

def convert_to_military(time):
    in_time = datetime.strptime(time, "%I:%M:%S %p")
    out_time = datetime.strftime(in_time, "%H:%M:%S")
    return out_time