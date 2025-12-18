"""
QUESTION:
Write a function `format_date` that formats a given date string from 'YYYY-MM-DD' to 'Month Day, Year'. The function should handle edge cases such as invalid input dates and different date formats.
"""

def format_date(input_date):
    # Split the input date string
    year, month, day = input_date.split('-')

    # Convert the month value to month name
    month_names = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }
    month_name = month_names.get(month)

    # Convert the day value to an integer
    day_value = int(day)

    # Add the appropriate suffix to the day value
    if day_value in (1, 21, 31):
        suffix = 'st'
    elif day_value in (2, 22):
        suffix = 'nd'
    elif day_value in (3, 23):
        suffix = 'rd'
    else:
        suffix = 'th'

    # Concatenate the formatted date components
    formatted_date = f"{month_name} {day_value}{suffix}, {year}"
    return formatted_date