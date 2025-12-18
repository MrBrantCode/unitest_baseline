"""
QUESTION:
Implement a function named `determine_day_type` that takes a string parameter "day" representing the day of the week and returns a string indicating whether the day is a day of rest, the first day of the week, a work day, or an invalid day. The function should support the following day types: Sunday is a day of rest, Monday is the first day of the week, Tuesday to Friday are work days, and Saturday is a day of work. If the input day is not one of the seven days of the week, the function should return "Invalid day entered".
"""

def determine_day_type(day):
    if day == "Sunday":
        return "Sunday is a Day of Rest"
    elif day == "Monday":
        return "Monday is the First Day of the Week"
    elif day in ["Tuesday", "Wednesday", "Thursday", "Friday"]:
        return f"{day} is a Work Day"
    elif day == "Saturday":
        return "Saturday is a Day of Work"
    else:
        return "Invalid day entered"