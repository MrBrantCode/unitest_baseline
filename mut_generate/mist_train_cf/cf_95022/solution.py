"""
QUESTION:
Develop a function named `count_weekdays` that takes two dates in the format "DD Month, YYYY" as input and returns the number of weekdays (Monday to Friday) between these two dates, excluding public holidays. The function should also accept a list of public holidays in the same date format, although this list is not explicitly passed as a parameter and should be defined within the function.
"""

from datetime import datetime, timedelta

def count_weekdays(date1, date2):
    # List of public holidays
    public_holidays = [
        datetime.strptime("1 May, 2020", "%d %B, %Y").date(),  
        # add more public holidays if needed
    ]
    
    # Convert input dates to datetime objects
    date1 = datetime.strptime(date1, "%d %B, %Y").date()
    date2 = datetime.strptime(date2, "%d %B, %Y").date()
    
    # Initialize count variable
    count = 0
    
    # Iterate through each date between date1 and date2
    current_date = date1
    while current_date <= date2:
        # Check if the date is a weekday and not a public holiday
        if current_date.weekday() < 5 and current_date not in public_holidays:
            count += 1
        
        # Move to the next date
        current_date += timedelta(days=1)
    
    return count