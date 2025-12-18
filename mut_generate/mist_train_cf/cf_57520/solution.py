"""
QUESTION:
Create a function named `convert_time` that takes a string representing a time in 24-hour format (HH:MM) and returns a string representing the time in 12-hour format (HH:MM AM/PM). The function should handle edge cases such as midnight (00:00) and noon (12:00) correctly, and ensure that minutes are always displayed with two digits.
"""

def convert_time(time24):
    h, m = map(int, time24.split(':'))
    tail = "AM" if h < 12 else "PM"
    h %= 12
    if h == 0: h = 12
    return "{}:{:02d} {}".format(h, m, tail)