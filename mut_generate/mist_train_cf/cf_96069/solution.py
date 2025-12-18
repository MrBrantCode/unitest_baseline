"""
QUESTION:
Create a function `get_day_of_week` that takes a date string in the format "YYYY-MM-DD" as an argument and returns the corresponding day of the week from Monday to Sunday as a string. The function should handle leap years correctly without using any built-in date or time libraries, and its time complexity should be O(1).
"""

def get_day_of_week(date):
    year, month, day = map(int, date.split('-'))

    if month == 1 or month == 2:
        month += 12
        year -= 1

    q = day
    m = month
    K = year % 100
    J = year // 100

    h = (q + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 - 2 * J) % 7

    days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days_of_week[h]