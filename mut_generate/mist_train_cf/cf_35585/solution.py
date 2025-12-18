"""
QUESTION:
Write a function called `process_input_string` that takes a string as input and extracts the number enclosed in square brackets and the number that follows it. If the number enclosed in square brackets is even, the function should double the second number; if it's odd, the function should triple the second number. If the string contains the phrase "ou mais", the function should append " - Special Offer" to the result. Return the result of these operations as a string.
"""

import re

def process_input_string(input_string):
    # Extract numbers and phrases from the input string using regular expressions
    numbers = re.findall(r'\d+', input_string)
    phrase_present = "ou mais" in input_string

    # Perform operations based on the extracted information
    first_number = int(numbers[0])
    second_number = int(numbers[1])
    if first_number % 2 == 0:
        result = 2 * second_number
    else:
        result = 3 * second_number

    # Add " - Special Offer" to the result if the phrase is present
    if phrase_present:
        result_str = str(result) + " - Special Offer"
    else:
        result_str = str(result)

    return result_str