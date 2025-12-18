"""
QUESTION:
Computation of the date either previous or forthcoming dates is quiet easy. But it is quiet difficult to calculate the day from a particular given date. 
You are required to find a day from a particular date given to you.

-----Input-----
It consists of a single line entry consisting of date in format dd mm yyyy.
i.e. the input line consists of the three numbers written in order followed by spaces.
Eg. Input for 18-12-1990 is be written as 18 12 1990

-----Output-----
It consists of single line output showing the day for that particular date.

-----Example-----
Input:
14 3 2012

Output:
Wednesday
"""

import datetime

def get_day_from_date(day: int, month: int, year: int) -> str:
    """
    Returns the day of the week for a given date.

    Parameters:
    - day (int): The day of the month (1-31).
    - month (int): The month of the year (1-12).
    - year (int): The year (e.g., 2023).

    Returns:
    - str: The day of the week (e.g., "Monday", "Tuesday", etc.).
    """
    date = datetime.date(year, month, day)
    return date.strftime('%A')