"""
QUESTION:
Write a function called `compute_date_difference` that takes two dates in the format "MM-DD-YYYY" as input, calculates the difference between them, and returns the result in years, months, days, hours, minutes, and seconds. The function should handle leap years correctly.
"""

from datetime import datetime

def compute_date_difference(date1, date2):
    # Convert input dates to datetime objects
    date1 = datetime.strptime(date1, "%m-%d-%Y")
    date2 = datetime.strptime(date2, "%m-%d-%Y")
    
    # Calculate the difference between the two dates
    timedelta = date2 - date1
    
    # Extract years, months, days, hours, minutes, and seconds from timedelta object
    years = timedelta.days // 365
    months = timedelta.days % 365 // 30
    days = timedelta.days % 365 % 30
    hours = timedelta.seconds // 3600
    minutes = (timedelta.seconds % 3600) // 60
    seconds = (timedelta.seconds % 3600) % 60
    
    # Return the difference in years, months, days, hours, minutes, and seconds
    return years, months, days, hours, minutes, seconds