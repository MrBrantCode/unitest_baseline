"""
QUESTION:
Write a function named `validate_and_display` that takes two parameters: `full_name` and `date_of_birth`. The function should validate that `full_name` is not null and does not contain any numeric characters, and `date_of_birth` is not null and is in the format "DD-MM-YYYY". If the input is valid, the function should print the `full_name` and `date_of_birth`. If the input is invalid, the function should print an error message.
"""

import re
from datetime import datetime

def validate_and_display(full_name, date_of_birth):
    
    # Check if full name is not null and is not numeric
    if not full_name or not all(word.isalpha() for word in full_name.split()):
        print("Invalid full name.")
        return

    # Check if date of birth is not null
    if not date_of_birth:
        print("Invalid date of birth.")
        return

    # Validate the format of date of birth
    date_format = "%d-%m-%Y"
    try:
        datetime.strptime(date_of_birth, date_format)
    except ValueError:
        print("Incorrect data format, should be DD-MM-YYYY")
        return

    print("Full Name:", full_name)
    print("Date of Birth:", date_of_birth)