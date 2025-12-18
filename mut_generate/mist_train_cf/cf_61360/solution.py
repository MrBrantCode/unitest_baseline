"""
QUESTION:
Write a function named `invert_case_and_transform` that takes an input string and returns a transformed string where: 
- alphabetic characters have their case switched (lower to upper and upper to lower), 
- odd digits are replaced with their immediate higher even counterpart, 
- and non-alphanumeric characters are reproduced twice.
"""

def invert_case_and_transform(string: str) -> str:
    """
    For an occurring string, switch lower-case to upper-case characters and contrariwise, substitute odd numerals with their subsequent even digit, and multiply rare characters.
    """

    result = []

    for char in string:
        if char.isalpha():
            if char.islower():
                result.append(char.upper())
            else:
                result.append(char.lower())
        elif char.isdigit():
            digit = int(char)
            if digit % 2 != 0:
                result.append(str(digit+1))
            else:
                result.append(char)
        else:
            result.append(char*2)
    
    return ''.join(result)