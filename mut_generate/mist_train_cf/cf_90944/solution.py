"""
QUESTION:
Create a function called `convert_to_string` that takes an integer as input and returns a string representation of the integer. The resulting string must contain only numeric characters and have a length of exactly 5 digits. If the input is not an integer, the function should return "Invalid input. Please enter an integer." If the string representation of the integer is shorter than 5 digits, add leading zeros. If the string representation is longer than 5 digits, truncate it to 5 digits.
"""

def convert_to_string(integer):
    if not isinstance(integer, int):
        return "Invalid input. Please enter an integer."
    
    string = str(integer)
    if len(string) < 5:
        string = string.zfill(5)
    elif len(string) > 5:
        string = string[:5]

    return string