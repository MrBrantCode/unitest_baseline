"""
QUESTION:
Write a function called `convert_date_format` that takes a string in the format 'dd/mm/yyyy' as input, checks if the date is valid (considering leap years), and returns the date in the format 'yyyy/mm/dd'. If the date is invalid, the function should return 'Invalid date'. The function should handle dates within a reasonable range of years.
"""

def convert_date_format(date):
    def is_leap_year(year):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return True
        return False

    def is_valid_date(day, month, year):
        if month < 1 or month > 12:
            return False
        if day < 1:
            return False
        if month == 2:
            if is_leap_year(year):
                if day > 29:
                    return False
            elif day > 28:
                return False
        elif month in [4, 6, 9, 11]:
            if day > 30:
                return False
        elif day > 31:
            return False
        return True

    day, month, year = date.split('/')
    if is_valid_date(int(day), int(month), int(year)):
        return f'{year}/{month.zfill(2)}/{day.zfill(2)}'
    else:
        return 'Invalid date'