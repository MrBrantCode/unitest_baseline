"""
QUESTION:
Create a function `convert_number_to_string(number)` that takes an integer as input and returns a string representation of the number with each digit separated by a hyphen (-) in reverse order. The function should only work for integers between 1000 and 9999 (inclusive) and return an error message for any other input.
"""

def convert_number_to_string(number):
    # Check if number is within the specified range
    if not (1000 <= number <= 9999):
        return "Error: Number is not within the range 1000 to 9999."
    
    # Convert number to string and remove decimal point if it exists
    number_str = str(number).replace(".", "")
    
    # Reverse the string
    reversed_str = number_str[::-1]
    
    # Insert hyphens between each digit
    final_str = "-".join(reversed_str)
    
    return final_str