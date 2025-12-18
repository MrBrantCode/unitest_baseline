"""
QUESTION:
Develop a function `print_day_and_check_holiday` that takes a date string in the format 'YYYY-MM-DD' as an argument. The function should print the name of the day of the week for the given date, and also check if the date is a public holiday in a specific country (to be specified by a dictionary of public holidays). The function should only accept dates within the range of January 1st, 1900 to December 31st, 2099.
"""

import datetime

def print_day_and_check_holiday(date):
    try:
        # Convert the given date string to a datetime object
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
        
        # Check if the date is within the valid range
        if date_obj.year < 1900 or date_obj.year > 2099:
            print("Invalid date range. Please enter a date between January 1st, 1900 and December 31st, 2099.")
            return
        
        # Get the name of the day
        day_name = date_obj.strftime('%A')
        
        # Print the name of the day
        print("The day is", day_name)
        
        # Check if the date is a public holiday
        public_holidays = {
            # Add public holidays of the specific country here
            '2022-01-01': "New Year's Day",
            '2022-12-25': "Christmas Day",
        }
        
        if date in public_holidays:
            print("It is a public holiday in our country:", public_holidays[date])
        else:
            print("It is not a public holiday in our country.")
        
    except ValueError:
        print("Invalid date format. Please enter a date in the format 'YYYY-MM-DD'.")