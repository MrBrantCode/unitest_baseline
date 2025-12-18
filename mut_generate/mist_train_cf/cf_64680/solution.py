"""
QUESTION:
Create a function called `get_reminder` that takes two parameters: `current_month` and `current_year`. The function should display a reminder based on the `current_month` and verify if the `current_year` is a leap year to handle February's reminder accordingly. If `current_month` is not a valid month (between 1 and 12), the function should raise an exception.
"""

class InvalidMonthException(Exception):
    pass

def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

reminders = {
    1: "Reminder for January",
    2: "Reminder for February",
    3: "Reminder for March",
    4: "Reminder for April",
    5: "Reminder for May",
    6: "Reminder for June",
    7: "Reminder for July",
    8: "Reminder for August",
    9: "Reminder for September",
    10: "Reminder for October",
    11: "Reminder for November",
    12: "Reminder for December"
}

days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

def get_reminder(current_month, current_year):
    if current_month < 1 or current_month > 12:
        raise InvalidMonthException("Invalid month number. Should be between 1 and 12.")
    
    if current_month == 2 and is_leap(current_year):
        print("This is a leap year. February has 29 days.")
        days_in_month[2] = 29

    print("Number of days in this month: ", days_in_month[current_month])
    print(reminders[current_month])