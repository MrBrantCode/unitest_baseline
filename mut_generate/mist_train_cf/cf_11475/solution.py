"""
QUESTION:
Write a function called `convert_to_12_hour_format` that takes a string representing time in 24-hour format (HH:MM) and returns the equivalent time in 12-hour format (HH:MM AM/PM). The function should correctly handle noon (12:00) and midnight (00:00) cases.
"""

def convert_to_12_hour_format(time):
    hour, minute = map(int, time.split(':'))
    if hour == 0:
        return f'12:{minute:02d} AM'
    elif hour == 12:
        return f'{hour}:{minute:02d} PM'
    elif hour > 12:
        return f'{hour - 12}:{minute:02d} PM'
    else:
        return f'{hour}:{minute:02d} AM'