"""
QUESTION:
Write a function `format_date(date)` that takes a string `date` in the format 'YYYY-MM-DD' and returns a string in the format 'Month Day, Year', where 'Day' includes the appropriate suffix ('st', 'nd', 'rd', or 'th').
"""

def format_date(date):
    # Split the date string into year, month, and day
    year, month, day = date.split('-')
    
    # Create a dictionary to map month numbers to month names
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
    
    # Convert the month value to its corresponding name
    month_name = month_names[month]
    
    # Convert the day value to an integer
    day = int(day)
    
    # Add the appropriate suffix to the day value
    if day in [1, 21, 31]:
        suffix = 'st'
    elif day in [2, 22]:
        suffix = 'nd'
    elif day in [3, 23]:
        suffix = 'rd'
    else:
        suffix = 'th'
    
    # Concatenate the formatted date components
    formatted_date = month_name + ' ' + str(day) + suffix + ', ' + year
    
    return formatted_date