"""
QUESTION:
Create a function named `concat_strings` that takes two string arguments, checks if they meet the following conditions, and then concatenates and prints the strings. 

Both strings must have at least 8 characters and are not empty. Additionally, each string must contain at least one uppercase letter, one lowercase letter, one digit, and one special character. If any condition is not met, the function should print an error message and return without concatenating the strings.
"""

import string

def concat_strings(str1, str2):
    # Check if the strings have at least 8 characters
    if len(str1) < 8 or len(str2) < 8:
        print("Both strings should have at least 8 characters.")
        return

    # Check if the strings are not empty
    if len(str1) == 0 or len(str2) == 0:
        print("Both strings should not be empty.")
        return

    # Check if both strings contain at least one uppercase, lowercase, digit, and special character
    if not any(char.isupper() for char in str1) or not any(char.isupper() for char in str2):
        print("Both strings should contain at least one uppercase letter.")
        return
    if not any(char.islower() for char in str1) or not any(char.islower() for char in str2):
        print("Both strings should contain at least one lowercase letter.")
        return
    if not any(char.isdigit() for char in str1) or not any(char.isdigit() for char in str2):
        print("Both strings should contain at least one digit.")
        return
    if not any(char in string.punctuation for char in str1) or not any(char in string.punctuation for char in str2):
        print("Both strings should contain at least one special character.")
        return

    # Concatenate the strings and print them
    concatenated_string = str1 + str2
    print(concatenated_string)