"""
QUESTION:
Create a function named `flip_case_and_modify` that takes a string as input and returns a modified string. In the modified string, invert the case of alphabetic characters, replace any odd integer with its succeeding even integer, and duplicate any non-alphanumeric characters.
"""

def flip_case_and_modify(string: str) -> str:
    """ For an inputted sequence of characters, invert lowercase to uppercase and vice versa, substitute odd numerals with its succeeding even numeral, and duplicate any peculiar symbols. """

    modified_string = ''
    for char in string:
        if char.isalpha():
            modified_string += char.swapcase()
        elif char.isdigit():
            if int(char) % 2 != 0:
                modified_string += str(int(char) + 1)
            else:
                modified_string += char
        else:
            modified_string += char * 2

    return modified_string