"""
QUESTION:
[Image] 


-----Input-----

The first line of the input is a string (between 1 and 50 characters long, inclusive). Each character will be a letter of English alphabet, lowercase or uppercase.

The second line of the input is an integer between 0 and 26, inclusive.


-----Output-----

Output the required string.


-----Examples-----
Input
AprilFool
14

Output
AprILFooL
"""

def transform_string(input_string: str, shift_value: int) -> str:
    # Convert the input string to lowercase
    lower_string = input_string.lower()
    
    # Initialize an empty list to store the transformed characters
    transformed_chars = []
    
    # Iterate over each character in the lowercase string
    for char in lower_string:
        # Check if the ASCII value of the character plus the shift value is >= 97 ('a')
        if ord(char) + shift_value >= 97:
            # Convert the character to uppercase
            transformed_chars.append(char.upper())
        else:
            # Keep the character in lowercase
            transformed_chars.append(char)
    
    # Join the list of transformed characters into a single string and return it
    return ''.join(transformed_chars)