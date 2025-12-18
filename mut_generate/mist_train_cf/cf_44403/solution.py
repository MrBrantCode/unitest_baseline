"""
QUESTION:
Design a function `solve(date)` that takes a string `date` in the format `DDMMYYYY` and returns its corresponding day of the week as a string. The function should not use any built-in date-time function or third-party date library. It should also verify if the input date is valid, considering different numbers of days in different months and leap years. The function should return "Invalid date" if the input date is invalid.
"""

def entrance(date):
    def is_leap(year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False

    def valid_date(day, month, year):
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        if month == 2:
            if is_leap(year):
                if day > 29:
                    return False
            elif day > 28:
                return False
        if month in [4, 6, 9, 11] and day > 30:
            return False
        return True

    def day_of_week(day, month, year):
        t = [ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4 ] 
        year -= month < 3
        return ( year + year // 4 - year // 100 + year // 400 + t[month-1] + day) % 7 

    day = int(date[:2])
    month = int(date[2:4])
    year = int(date[4:])
    if not valid_date(day, month, year):
        return "Invalid date"
    weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return weekday[day_of_week(day, month, year)]