"""
QUESTION:
Create a function named `inches_to_cm` that takes a single argument representing a length in inches and returns its equivalent length in centimeters using the conversion factor of 1 inch = 2.54 cm. The function should handle potential errors, such as non-numeric inputs, and return an error message instead of raising an exception.
"""

def inches_to_cm(inches):
    try:
        # convert inches to cm
        cm = inches * 2.54
        return cm
    except TypeError:
        return "Invalid input! Please enter numeric value."
    except Exception as e:
        return "Error occurred: " + str(e)