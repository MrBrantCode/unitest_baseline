"""
QUESTION:
Create a function `convert_currency` that takes a string value as input and returns a float. The string may contain commas as thousand separators and a dollar sign. If the string is empty, it should be converted to a float value of 0. If the string cannot be converted to a float, it should be converted to NaN (Not a Number).
"""

def convert_currency(val):
    """
    Convert the string number value to a float
     - Remove $
     - Remove commas
     - Convert to float type
    """
    if val == '':
        return 0.0
    new_val = val.replace(',','').replace('$', '')
    try:
        return float(new_val)
    except ValueError:
        return float('nan')