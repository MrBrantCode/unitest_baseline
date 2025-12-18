"""
QUESTION:
Create a function `parse_and_print_date(date_string)` to parse and print the date in DD-MM-YYYY format from the given input date string in "DD MonthName YYYY" format. The function should handle leap years, validate the input date string, and handle invalid dates, and years before 1900 and after 2100. The function should return an error message for any invalid input.
"""

def parse_and_print_date(date_string):
    date_parts = date_string.split()
    if len(date_parts) != 3:
        return "Error: Incorrect date format"

    day = date_parts[0]
    month = date_parts[1]
    year = date_parts[2]

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
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day > 29:
                return "Error: Invalid day"
        elif day > 28:
            return "Error: Invalid day"
    elif month in [4, 6, 9, 11] and day > 30:
        return "Error: Invalid day"

    if year < 1900 or year > 2100:
        return "Error: Invalid year"

    return "{:02d}-{:02d}-{:04d}".format(day, month, year)