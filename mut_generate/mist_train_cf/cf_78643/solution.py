"""
QUESTION:
Write a function called `refine_case_and_transform` that takes a string as input and returns a new string with the following transformations: 
- Swap the case of all alphabetical characters (lower to upper and upper to lower), 
- Replace all odd digits with the next even digit, 
- Duplicate all non-alphanumeric characters (considered as symbols).
"""

def refine_case_and_transform(string: str) -> str:
    new_string = ''
    for char in string:
        # check if character is alphabet
        if char.isalpha():
            # if character is uppercase make it lowercase otherwise make it uppercase
            new_string += char.lower() if char.isupper() else char.upper()
        # check if character is digit
        elif char.isdigit():
            # if digit is odd then replace it with next even number
            new_string += str(int(char)+1) if int(char) % 2 != 0 else char
        # if character is symbol then duplicate it
        else:
            new_string += char * 2
    return new_string