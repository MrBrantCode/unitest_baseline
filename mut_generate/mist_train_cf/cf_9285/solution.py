"""
QUESTION:
Create a function named `convert_seconds(seconds)` that takes the number of seconds as input and returns a string representing the equivalent duration in years, months, weeks, days, hours, minutes, and seconds. The function should perform the conversion using integer division and modulo operations, and return the result in the format "{years} years, {months} months, {weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds". Note that a month is assumed to be equivalent to 4 weeks, and a year is assumed to be equivalent to 12 months.
"""

def convert_seconds(seconds):
    minutes = seconds // 60
    seconds = seconds % 60

    hours = minutes // 60
    minutes = minutes % 60

    days = hours // 24
    hours = hours % 24

    weeks = days // 7
    days = days % 7

    months = weeks // 4
    weeks = weeks % 4

    years = months // 12
    months = months % 12

    return f"{years} years, {months} months, {weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"