"""
QUESTION:
Create a function called `invert_case_and_update` that takes a string as an input. Within this string, reverse the character case of each alphabetic character (i.e., convert uppercase to lowercase and vice versa), substitute odd digits with their successive even numerical counterpart, and duplicate each unique symbol or punctuation.
"""

def invert_case_and_update(string: str) -> str:
    output = ''
    for character in string:
        # Checking if it's a letter
        if character.isalpha():
            # Checking if it's uppercase
            if character.isupper():
                # Convert to lowercase
                output += character.lower()
            else:
                # Convert to uppercase
                output += character.upper()
        # Checking if it's a digit
        elif character.isdigit():
            # If it's odd, replace it with the next even digit
            if int(character) % 2 != 0:
                output += str(int(character) + 1)
            else:
                output += character
        else:
            # Double every special character
            output += character * 2
    return output