"""
QUESTION:
Implement a function named `check_month_name` that takes a string `month_name` as input and checks if it is a valid month name, considering the Gregorian, Islamic, and Hebrew calendars. The function should ignore case sensitivity and leading/trailing whitespace characters. The valid month names are: january, february, march, april, may, june, july, august, september, october, november, december, ramadan, and tishrei. The function should return a string indicating whether the input month name is valid or not.
"""

def check_month_name(month_name):
    month_name = month_name.strip().lower()  # remove leading/trailing whitespace and convert to lowercase

    if month_name in [
        "january", "february", "march", "april", "may", "june", 
        "july", "august", "september", "october", "november", 
        "december", "ramadan", "tishrei"
    ]:
        return "Valid month name"
    else:
        return "Invalid month name"