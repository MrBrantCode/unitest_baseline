"""
QUESTION:
Create a function `extract_dates(text)` that takes a string `text` as input and extracts dates in the format "Day, Month ddth|st|nd|rd, yyyy". The function should convert the extracted dates to the format "yyyy-mm-dd" and determine the day of the week without using a built-in function for this purpose. The output should be a list of tuples, where each tuple contains the original date string, the converted date string, and the day of the week.
"""

from dateutil import parser
import re

def extract_dates(text):
    """
    Extracts dates in the format "Day, Month ddth|st|nd|rd, yyyy" from a given text, 
    converts them to the format "yyyy-mm-dd", and determines the day of the week.

    Args:
    text (str): The input text to extract dates from.

    Returns:
    list: A list of tuples containing the original date string, the converted date string, and the day of the week.
    """
    matches = re.findall(r"((?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),\s(?:January|February|March|April|May|June|July|August|September|October|November|December)\s(?:\d{1,2}(?:st|nd|rd|th)),\s(?:\d{4}))", text)
    result = []
    for date_str in matches:
        date_obj = parser.parse(date_str)
        result_date = date_obj.strftime('%Y-%m-%d')
        result.append((date_str, result_date, date_obj.strftime('%A')))
    return result