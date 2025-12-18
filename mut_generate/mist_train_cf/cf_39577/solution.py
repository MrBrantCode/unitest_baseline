"""
QUESTION:
Write a function `day_of_year_to_month_day(day)` that takes an integer `day` (1 <= day <= 365) as input and returns a tuple `(month, day_of_month)` representing the month (1-based index) and the day of the month. The function should assume a non-leap year.
"""

def day_of_year_to_month_day(day):
    days_before_months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(12):
        if days_before_months[i] < day <= (days_before_months[i] + month_lengths[i]):
            return i + 1, day - days_before_months[i]