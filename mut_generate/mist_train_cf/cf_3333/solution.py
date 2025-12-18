"""
QUESTION:
Write a function named `format_date` that formats a given date string from "DD-MM-YYYY" format to "DD/MM/YYYY" format without using any built-in date formatting functions or libraries. The function should have a time complexity of O(n), where n is the length of the input date.
"""

def format_date(input_date):
    # Split the input date by '-'
    parts = input_date.split('-')
    
    # Rearrange the parts to form the formatted date
    formatted_date = parts[0] + '/' + parts[1] + '/' + parts[2]
    
    return formatted_date