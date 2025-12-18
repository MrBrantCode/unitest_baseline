"""
QUESTION:
Write a function `validate_complex_input` that takes a string as input and returns a complex number if the string represents a valid complex number. If the string does not represent a valid complex number, the function should print an error message and return `None`. The function should be able to handle user input that is not a complex number.
"""

def validate_complex_input(input_str):
    """Validate whether the provided string is a complex number"""
    try:
        # Try to convert to complex
        value = complex(input_str)
        return value
    except ValueError:
        # In case of a value error, print error message and return None
        print(f"Error: {input_str} is not a valid complex number!")
        return None