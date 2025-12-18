"""
QUESTION:
Write a function `convert_seconds(seconds)` that takes an integer number of seconds as input and returns a string representing the equivalent time in years, months, weeks, days, hours, minutes, and seconds. Assume a year has 365 days and a month has 30 days. The output string should be in the format 'X years, Y months, Z weeks, A days, B hours, C minutes, D seconds', where X, Y, Z, A, B, C, and D are the corresponding time values. The function should handle the plural form of time units correctly.
"""

def entrance(seconds):
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
    
    for unit, value in time_units.items():
        if seconds >= value:
            result[unit] = seconds // value
            seconds %= value
    
    time_format = ''
    for unit, value in result.items():
        if value == 1:
            unit += ''
        else:
            unit += 's'
        time_format += f'{value} {unit}, '

    return time_format[:-2]