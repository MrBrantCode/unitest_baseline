"""
QUESTION:
Write a function `CET_to_UTC_plus_5(hours_CET)` that converts a given hour in 24-hour Central European Time (CET) format to its equivalent hour in UTC+5 format. The function should take an integer `hours_CET` (ranging from 0 to 23) as input and return the corresponding hour in UTC+5 format.
"""

def CET_to_UTC_plus_5(hours_CET):
    hours_UTC_plus_5 = (hours_CET + 4) % 24
    if hours_UTC_plus_5 < 0:
        hours_UTC_plus_5 += 24
    return hours_UTC_plus_5