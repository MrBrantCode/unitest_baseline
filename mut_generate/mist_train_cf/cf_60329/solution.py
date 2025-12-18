"""
QUESTION:
Write a function `julian_day_of_week(day, month, year)` that takes a date in the format DDMMYYYY and returns the corresponding day of the week in the Julian calendar, without using any built-in date and time functions. The function should consider Monday as the first day of the week (day number 0) up to Sunday (day number 6).
"""

def julian_day_of_week(day, month, year):
    a = (14 - month)//12
    y = year + 4800 - a
    m = month + 12*a - 3
    jdn = day + ((153*m + 2)//5) + 365*y + y//4 - 32083
    return (jdn + 1 ) % 7