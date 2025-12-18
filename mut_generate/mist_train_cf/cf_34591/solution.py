"""
QUESTION:
Implement a function `validate_and_process_euro_value` that takes a monetary value as a string, checks if it adheres to Euro currency formatting rules, and returns a boolean value indicating validity and the processed value with the currency symbol appended if valid. The Euro formatting rules are:
- The value should be a non-negative number.
- The value should have a maximum of 2 decimal places.
- The value should not exceed 12 digits in total.

The function should return False for invalid values and True along with the processed value (e.g., '€123.45') for valid values.
"""

from typing import Union

def validate_and_process_euro_value(value: str) -> Union[bool, str]:
    try:
        value = float(value)
        if value < 0:
            return False
        value_str = '{:.2f}'.format(value)
        if len(value_str) > 15 or len(value_str.split('.')[0]) > 12:
            return False
        return True, '€' + value_str
    except ValueError:
        return False