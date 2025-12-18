"""
QUESTION:
Create a function `filter_birth_dates` that takes a list of tuples, where each tuple contains a name and a birth date in the format "YYYY-MM-DD". The function should return a dictionary where the birth dates are used as keys and the names are used as values. The birth dates should be stored as `datetime` objects and the dictionary should only include the names of individuals who were born after 1990.
"""

from datetime import datetime

def filter_birth_dates(data):
    """
    This function takes a list of tuples, where each tuple contains a name and a birth date in the format "YYYY-MM-DD".
    It returns a dictionary where the birth dates are used as keys and the names are used as values.
    The birth dates are stored as `datetime` objects and the dictionary only includes the names of individuals who were born after 1990.

    Args:
        data (list): A list of tuples containing names and birth dates.

    Returns:
        dict: A dictionary with birth dates as keys and names as values.
    """
    birth_dates = {}
    for name, date_str in data:
        birth_date = datetime.strptime(date_str, "%Y-%m-%d")
        birth_dates[birth_date] = name

    birth_dates_filtered = {date: name for date, name in birth_dates.items() if date.year > 1990}
    return birth_dates_filtered