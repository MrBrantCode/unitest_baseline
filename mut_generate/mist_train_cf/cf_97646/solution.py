"""
QUESTION:
Write a Python function `convert_date` that takes a date string in 'mm/dd/yyyy' format as input. The function should return the date in 'dd-mm-yyyy' format along with its day of the week and a textual representation of the date, but only if the year is a leap year according to the Gregorian calendar. If the year is not a leap year, the function should return an error message. The output should be in a LaTeX table format with columns for numerical format, textual format, and day of the week.
"""

import datetime

def convert_date(date_string):
    date_obj = datetime.datetime.strptime(date_string, '%m/%d/%Y')
    if date_obj.year % 4 == 0 and (date_obj.year % 100 != 0 or date_obj.year % 400 == 0):
        converted_date_string = date_obj.strftime('%d-%m-%Y')
        day_of_week = date_obj.strftime('%A')
        month_name = date_obj.strftime('%B')
        return f"begin{{tabular}}{{|c|c|c|}}\nhline\nNumerical format & Textual format & Day of the week \nhline\n{converted_date_string} & {date_obj.day} {month_name} {date_obj.year} & {day_of_week}\nhline\nend{{tabular}}"
    else:
        return f"Error: The year {date_obj.year} is not a leap year."