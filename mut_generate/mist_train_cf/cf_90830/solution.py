"""
QUESTION:
Create a function called `convert_seconds` that takes an integer `seconds` as input and returns a string representing the equivalent time in years, months, weeks, days, hours, minutes, and seconds. The months are assumed to be 4 weeks each and the years are assumed to be 12 months each.
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