"""
QUESTION:
Write a function that takes a string representing a date in the format "Month Day, Year" (e.g., "June 13th, 2020") and returns a dictionary with the day, month, and year. Then, write four functions that take an integer representing the day and return the day in Roman numerals in four different formats: Basic Roman Numerals, Roman Numerals with Overline, Roman Numerals with Parentheses, and Roman Numerals with Periods.
"""

def extract_date_info(date_str):
    import re
    date_regex = r"\b([A-Za-z]+) (\d+)(st|nd|rd|th), (\d{4})\b"
    match = re.search(date_regex, date_str)
    if match:
        return {
            'month': match.group(1),
            'day': match.group(2),
            'year': match.group(4)
        }

def to_roman_basic(num):
    roman = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    return roman[num]

def to_roman_overline(num):
    roman = ["", "I̅", "II̅", "III̅", "IV̅", "V̅", "VI̅", "VII̅", "VIII̅", "IX̅", "X̅"]
    return roman[num]

def to_roman_parentheses(num):
    roman = ["", "(I)", "(II)", "(III)", "(IV)", "(V)", "(VI)", "(VII)", "(VIII)", "(IX)", "(X)"]
    return roman[num]

def to_roman_period(num):
    roman = ["", "I.", "II.", "III.", "IV.", "V.", "VI.", "VII.", "VIII.", "IX.", "X."]
    return roman[num]