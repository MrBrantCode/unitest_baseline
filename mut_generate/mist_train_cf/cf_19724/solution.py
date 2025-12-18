"""
QUESTION:
Write a function `convert_date_time(input_str)` that takes a string `input_str` in the format "YYYY-MM-DD HH:MM:SS" and returns the date and time in the format "DD-MM-YYYY HH:MM". The function should handle potential errors during the conversion process and return an error message if the input format is invalid. The solution should have a time complexity of O(1) and a space complexity of O(1), and should not use any built-in date/time libraries or functions.
"""

def convert_date_time(input_str):
    try:
        date_str, time_str = input_str.split(" ")
        year, month, day = date_str.split("-")
        hour, minute, second = time_str.split(":")

        output_str = f"{day}-{month}-{year} {hour}:{minute}"
        return output_str
    except ValueError:
        return "Error: Invalid date/time format"