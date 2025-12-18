"""
QUESTION:
Create a function `convert_temp(temp_list)` that takes a list of temperatures in Fahrenheit as input, converts them to Celsius, and returns a dictionary with Fahrenheit temperatures as keys and their corresponding Celsius temperatures as values. The function should handle non-numeric inputs by skipping them and printing an error message.
"""

def convert_temp(temp_list):
    temp_dict = {}
    for fahrenheit in temp_list:
        try:
            fahrenheit = float(fahrenheit)
            celsius = (fahrenheit - 32) * 5.0/9.0
            temp_dict[fahrenheit] = round(celsius, 2)
        except ValueError:
            print(f"The value {fahrenheit} is not a number. Skipping...")
    return temp_dict