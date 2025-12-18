"""
QUESTION:
Create a function `check_month_name(month_name)` that checks if a given month name is valid. The function should handle case sensitivity and leading/trailing whitespace characters in the input. A month name is considered valid if it matches any of the following names: the 12 months of the Gregorian calendar (January to December), Ramadan, or Tishrei. The function should not use a switch statement and instead utilize alternative control flow mechanisms.
"""

def check_month_name(month_name):
    month_name = month_name.strip().lower()  # remove leading/trailing whitespace and convert to lowercase

    valid_months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december", "ramadan", "tishrei"]

    if month_name in valid_months:
        return "Valid month name"
    else:
        return "Invalid month name"