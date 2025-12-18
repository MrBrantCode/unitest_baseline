"""
QUESTION:
Create a function `validate_input_sequence` that takes a sequence (list or tuple) of strings as input and returns `True` if all characters in all strings are alphabets (a-z or A-Z), and `False` otherwise. The function should print an error message if the input is invalid and a success message if the input is valid.
"""

# A python function to check if a input sequence consists only of alphabets
def validate_input_sequence(input_sequence):
    for element in input_sequence:
        for character in element:
            if not character.isalpha():
                print("Invalid input. The sequence should only contain alphabets.")
                return False
    print("Valid input. The sequence only contains alphabets.")
    return True