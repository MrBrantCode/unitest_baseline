"""
QUESTION:
Calculate the age of a person in years and days from their birthday to the current date, considering leap years. The function should be named `calculate_age`. The input should include the person's name and their date of birth, as well as the current date, all in the format 'YYYY-MM-DD'. The function should return the difference in time from the person's birthday and their age in years and days.
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_age(name: str, dob_str: str, current_time_str: str) -> str:
    """
    Calculate the age of a person in years and days from their birthday to the current date.

    Args:
    name (str): The person's name.
    dob_str (str): The person's date of birth in the format 'YYYY-MM-DD'.
    current_time_str (str): The current date in the format 'YYYY-MM-DD'.

    Returns:
    str: A string containing the difference in time from the person's birthday and their age in years and days.
    """
    
    # Parse string dates
    dob = datetime.strptime(dob_str, '%Y-%m-%d')
    current_time = datetime.strptime(current_time_str, '%Y-%m-%d')

    # Calculate difference
    diff = relativedelta(current_time, dob)

    # Calculate age in years and days
    years = diff.years
    days = diff.days + diff.years * 365 + (diff.years // 4)  # consider leap years

    # Return results
    return f"Person's name: {name}\nTime from {dob_str} to {current_time_str}: {diff}\n{name}'s age: {years} years and {days} days"