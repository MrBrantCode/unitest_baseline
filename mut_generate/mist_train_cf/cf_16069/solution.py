"""
QUESTION:
Create a function called `convert_string_to_floats` that takes a string as input and returns a list of floats. The input string may contain a list of numbers in the format "[num1 num2 num3 ...]", where numbers are separated by spaces. The function should handle cases where the input string may contain invalid characters, have missing or extra spaces between numbers, or have multiple strings with similar format within square brackets. If the input is not in the correct format, the function should return an error message. The input must be a string.
"""

def convert_string_to_floats(input_string):
    try:
        # Remove square brackets from the input string
        input_string = input_string.replace("[", "").replace("]", "")

        # Split the string into a list of substrings using whitespace as delimiter
        substrings = input_string.split()

        # Initialize an empty list to store the floats
        float_list = []

        # Iterate over the substrings
        for substring in substrings:
            # Try converting the substring to a float
            try:
                float_value = float(substring)
                float_list.append(float_value)
            except ValueError:
                # If the substring is not a valid float, return an error message
                return "Error: Invalid input format"

        # Return the list of floats
        return float_list
    except AttributeError:
        # If the input is not a string, return an error message
        return "Error: Input must be a string"