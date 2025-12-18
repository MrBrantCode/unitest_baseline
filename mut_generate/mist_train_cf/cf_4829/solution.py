"""
QUESTION:
Write a function `print_days_in_month` that takes a list of dates in the format "MM/DD/YYYY" and prints the number of days in each month for each date in the list. The function should handle leap years correctly and have a time complexity of O(n), where n is the number of dates in the list.
"""

def print_days_in_month(date_list):
    def is_leap_year(year):
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False

    def days_in_month(month, year):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month == 2:
            if is_leap_year(year):
                return 29
            else:
                return 28
        else:
            return 30

    for date in date_list:
        month, day, year = map(int, date.split('/'))
        num_days = days_in_month(month, year)
        print(f"Date: {date}, Days in Month: {num_days}")