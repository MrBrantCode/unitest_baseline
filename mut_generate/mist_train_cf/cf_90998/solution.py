"""
QUESTION:
Create a function named `convert_seconds` that takes an integer `seconds` as input and returns a string representing the equivalent time in years, months, weeks, days, hours, minutes, and seconds. The function should use the following approximate conversions: 1 year = 365 days, 1 month = 30 days, 1 week = 7 days. The output string should be in the format "X years, Y months, Z weeks, A days, B hours, C minutes, D seconds" where X, Y, Z, A, B, C, and D are integers and the unit name is pluralized if the value is greater than 1.
"""

def convert_seconds(seconds):
    # Number of seconds in each time unit
    time_units = {
        'year': 365 * 24 * 60 * 60,
        'month': 30 * 24 * 60 * 60,
        'week': 7 * 24 * 60 * 60,
        'day': 24 * 60 * 60,
        'hour': 60 * 60,
        'minute': 60,
        'second': 1
    }
    
    result = {}
    
    # Calculate the number of each time unit
    for unit, value in time_units.items():
        if seconds >= value:
            result[unit] = seconds // value
            seconds %= value
    
    # Build the readable format
    time_format = ''
    for unit, value in result.items():
        if value == 1:
            unit += ''
        else:
            unit += 's'
        time_format += f'{value} {unit}, '

    return time_format[:-2]  # Remove the trailing comma and space