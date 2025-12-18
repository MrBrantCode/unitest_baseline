"""
QUESTION:
Create a function named `convert_to_string` that takes a float number as input and returns a string representation of the number rounded to 2 decimal places. The function must also add a leading zero to the string if the rounded number is less than 1.
"""

def convert_to_string(num):
    # Round the number to 2 decimal places
    rounded_num = round(num, 2)
    
    # Convert the rounded number to a string
    num_str = format(rounded_num, ".2f")
    
    # Add a leading zero if the rounded number is less than 1
    if rounded_num < 1:
        num_str = "0" + num_str
    
    return num_str