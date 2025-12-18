"""
QUESTION:
Write a function `check_string` that takes an input string as an argument and returns `True` if all characters in the string are alphanumeric, and `False` otherwise. The function should also print a message indicating whether all characters are alphanumeric or not. If a non-alphanumeric character is found, print the character.
"""

def check_string(input_string):
    for char in input_string:
        # check if current character is alphanumeric
        if not char.isalnum():
            print(f"'{char}' is not alphanumeric.")
            return False
    print("All characters are alphanumeric.")
    return True