"""
QUESTION:
Write a function `convert_string_to_floats(input_string)` that takes a string as input, extracts a list of numbers from the string, and converts them to floats. The input string may contain square brackets, extra or missing spaces, and invalid characters. The function should return a list of floats if the input string is in the correct format; otherwise, it should return an error message. The input string is expected to be in the format ["number1 number2 number3 ..."] or a string with similar format without square brackets.
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