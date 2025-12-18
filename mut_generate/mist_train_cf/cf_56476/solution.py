"""
QUESTION:
Write a function `get_day_counts(Y, M)` that takes two integers `Y` and `M` as input, where `Y` is a year between 1583 and 2100, and `M` is a month between 1 and 12, and returns a tuple containing the total number of days and weekdays in the given month.
"""

def get_day_counts(Y, M):
    if M == 2:
        if Y % 400 == 0 or (Y % 4 == 0 and Y % 100 != 0):
            total_days = 29
        else:
            total_days = 28
    elif M in [4, 6, 9, 11]:
        total_days = 30
    else:
        total_days = 31

    complete_weeks, remaining_days = divmod(total_days, 7)
    weekdays = 5 * complete_weeks

    if remaining_days == 1 or remaining_days == 2:
        weekdays += remaining_days
    elif remaining_days == 3:
        weekdays += 2
    elif remaining_days >= 4:
        weekdays += 3

    return total_days, weekdays