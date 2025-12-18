"""
QUESTION:
Implement a function `get_reminder` that takes in a month as a string and a day as an integer, and prints a reminder based on whether the date is a weekend, holiday, or a regular day. The function should account for leap years and handle invalid inputs. The month string should be converted to its corresponding number and the function should use exception handling to print different reminders. The function should also consider predefined holidays in the format MM-DD.
"""

import datetime

class CustomException(Exception):
    pass

class WeekendException(CustomException):
    pass

class HolidayException(CustomException):
    pass

HOLIDAYS = ["01-01", "25-12"] # Holidays in the format MM-DD

def is_weekend(date):
    weekday = date.weekday()
    return True if weekday > 4 else False

def is_holiday(date):
    date_str = date.strftime("%m-%d")
    return True if date_str in HOLIDAYS else False

def get_reminder(month, day, year=datetime.datetime.now().year):
    try: 
        # Convert the month name to its corresponding number
        timestamp = datetime.datetime.strptime(month, "%B")
        month = timestamp.strftime("%m")

        date_str = f"{day}-{month}-{year}"
        date = datetime.datetime.strptime(date_str, "%d-%m-%Y")

        if is_weekend(date):
            raise WeekendException
        elif is_holiday(date):
            raise HolidayException
        else:
            print("Regular reminder for this day.")
    
    except WeekendException:
        print("It's a weekend. Chill!")
    
    except HolidayException:
        print("It's a holiday! Enjoy!")

    except Exception as e:
        print("Invalid date or month input.")