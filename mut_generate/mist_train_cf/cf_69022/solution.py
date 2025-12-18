"""
QUESTION:
Create a function named `convert_date` that takes any date string in various formats as input, converts it to the ISO 8601 standard 'YYYY-MM-DD' format, and returns the result. The function should handle invalid input and return an error message with details.
"""

from dateutil import parser

def convert_date(date):
    try:
        d = parser.parse(date)
        return d.strftime('%Y-%m-%d')
    except ValueError as e:
        return f"Error: Invalid date. Details: {e}"