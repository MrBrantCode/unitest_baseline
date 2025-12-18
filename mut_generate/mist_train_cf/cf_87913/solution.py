"""
QUESTION:
Write a function called `format_date` that takes a string `input_date` in the format "DD-MM-YYYY" and returns a string representing the date in the format "DD/MM/YYYY". Do not use any built-in date formatting functions or libraries. Ensure the time complexity is O(n), where n is the length of the input date.
"""

def format_date(input_date):
    # Split the input date by '-'
    parts = input_date.split('-')
    
    # Rearrange the parts to form the formatted date
    formatted_date = parts[0] + '/' + parts[1] + '/' + parts[2]
    
    return formatted_date