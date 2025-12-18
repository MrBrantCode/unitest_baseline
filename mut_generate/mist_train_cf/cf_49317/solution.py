"""
QUESTION:
Implement a function `date_to_day` that takes a string representing a date in the format DDMMYYYY and returns the corresponding day of the week. The function should not use built-in or external date libraries. The Gregorian calendar is assumed (i.e., dates on or after October 15, 1582).
"""

def date_to_day(date):
    day = int(date[:2])
    month = int(date[2:4])
    year = int(date[4:])

    if month < 3:
        month += 12
        year -= 1

    q = day
    m = month
    K = year % 100
    J = year // 100

    f = q + ((13 * (m+1)) // 5) + K + (K//4) +  (J//4) - (2 * J)
    result = f % 7

    return ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'][result]