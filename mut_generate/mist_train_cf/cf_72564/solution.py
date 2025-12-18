"""
QUESTION:
Create a function named `compare_dates` that takes two dates as input and returns a boolean indicating whether the first date is earlier than the second. The date should be represented as a class with year, month, and day attributes. The function should compare the dates by year, then month, and finally day. Note that the function does not need to handle invalid dates or dates before the common era (BCE).
"""

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

def is_earlier(date1, date2):
    """
    Compare two dates.

    Args:
    date1 (Date): The first date.
    date2 (Date): The second date.

    Returns:
    bool: True if date1 is earlier than date2, False otherwise.
    """
    if date1.year < date2.year:
        return True
    elif date1.year == date2.year:
        if date1.month < date2.month:
            return True
        elif date1.month == date2.month:
            if date1.day < date2.day:
                return True
    return False