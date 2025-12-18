"""
QUESTION:
Create a function `text_sub` that takes three parameters: an input string, a replacement symbol, and a boolean for case sensitivity. The function should replace all non-alphanumeric characters in the input string with the replacement symbol, and optionally preserve the original letter casing if the case sensitivity boolean is `True`. If the case sensitivity boolean is `False`, the function should convert the input string to lowercase before making the substitutions.
"""

import re

def text_sub(input_str, replacement_symbol, case_sens):
    if not case_sens:
        input_str = input_str.lower()
    output_str = re.sub('[^0-9a-zA-Z]+', replacement_symbol, input_str)
    return output_str