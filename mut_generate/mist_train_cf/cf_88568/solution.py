"""
QUESTION:
Write a function `format_date` that takes a string `date` in the format 'YYYY-MM-DD' as input and returns a string representing the date in the format "Month Day, Year". The function should validate the input date and handle edge cases such as invalid month values, invalid day values, and different date formats. It should also handle leap years correctly.
"""

import calendar

def format_date(date):
    # Step 1: Validate input date format
    if len(date) != 10 or date[4] != '-' or date[7] != '-':
        return "Invalid date format. Please provide the date in 'YYYY-MM-DD' format."

    year, month, day = date.split('-')
    
    # Step 2: Validate month and day values
    try:
        month = int(month)
        day = int(day)
    except ValueError:
        return "Invalid month or day value."
    
    if month < 1 or month > 12:
        return "Invalid month value."
    
    if day < 1 or day > calendar.monthrange(int(year), month)[1]:
        return "Invalid day value."
    
    # Step 3: Convert month value to month name
    month_name = calendar.month_name[month]
    
    # Step 4: Validate month name
    if not month_name:
        return "Invalid month name."
    
    # Step 5: Add appropriate suffix to day value
    suffix = 'th'
    if day % 10 == 1 and day != 11:
        suffix = 'st'
    elif day % 10 == 2 and day != 12:
        suffix = 'nd'
    elif day % 10 == 3 and day != 13:
        suffix = 'rd'
    
    # Step 7: Format the date string
    formatted_date = f"{month_name} {day}{suffix}, {year}"
    
    # Step 8: Return the formatted date
    return formatted_date