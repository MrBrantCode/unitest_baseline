"""
QUESTION:
Create a function `parse_and_print_date(date_string)` that takes a string in the format "DD MonthName YYYY", where MonthName is one of the following: Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, or Dec. The function should handle leap years correctly, validate the input date string, and handle invalid dates and years outside the range 1900-2100. It should return an error message for invalid inputs and print the date in DD-MM-YYYY format for valid inputs.
"""

def parse_and_print_date(date_string):
    # Split the date string into day, month, and year
    date_parts = date_string.split()
    if len(date_parts) != 3:
        return "Error: Incorrect date format"

    day = date_parts[0]
    month = date_parts[1]
    year = date_parts[2]

    # Validate day, month, and year
    if not day.isdigit() or not year.isdigit():
        return "Error: Incorrect date format"

    day = int(day)
    year = int(year)

    if day < 1 or day > 31:
        return "Error: Invalid day"

    month_names = {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12
    }
    if month not in month_names:
        return "Error: Invalid month"

    month = month_names[month]

    if month == 2:
        # Check for leap year
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day > 29:
                return "Error: Invalid day"
        elif day > 28:
            return "Error: Invalid day"
    elif month in [4, 6, 9, 11] and day > 30:
        return "Error: Invalid day"

    if year < 1900 or year > 2100:
        return "Error: Invalid year"

    # Print the date in DD-MM-YYYY format
    print("{:02d}-{:02d}-{:04d}".format(day, month, year))