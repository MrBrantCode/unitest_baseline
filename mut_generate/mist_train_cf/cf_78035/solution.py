"""
QUESTION:
Create a function `reverse_capitalization_substitute` that takes a string as input and returns a string where:
- the case of all letters is reversed (lower-case to upper-case and vice versa)
- odd digits are replaced with the next even number
- each special character appears twice
The input string can contain letters, digits, and special characters.
"""

def reverse_capitalization_substitute(string: str) -> str:
    """ Within an input string, convert lower-case letters to upper-case, vice versa, switch odd numbers with the next even number, and duplicate singular symbols.
    """
    output = ""

    for chr in string:
        if chr.isalpha():
            if chr.isupper():
                output += chr.lower()
            else:
                output += chr.upper()
        elif chr.isdigit():
            if int(chr) % 2 == 1:
                output += str(int(chr) + 1)
            else:
                output += chr
        else:
            output += chr * 2

    return output