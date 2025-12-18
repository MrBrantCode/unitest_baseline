"""
QUESTION:
Create a function named `convert_to_float` that takes a list of strings as input, converts each string to a float, and returns a list of the converted float values. If a string cannot be converted to a float, skip it and print an error message. The function should handle both standard floating-point representations and scientific notation. The input list can contain any number of strings.
"""

from typing import List

def convert_to_float(input_list: List[str]) -> List[float]:
    float_list = []
    for x in input_list:
        try:
            float_list.append(float(x))
        except ValueError:
            print(f"Error: '{x}' cannot be converted to a float")
    return float_list