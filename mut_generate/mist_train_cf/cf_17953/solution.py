"""
QUESTION:
Create a function `concatenate_strings(string1, string2)` that takes two strings as input and returns their concatenation. The function should remove any leading or trailing white spaces from the input strings before concatenation. If either string is empty after removing white spaces, the function should return "Error: Input strings cannot be empty". Additionally, the function should check if the concatenated string contains any numeric digits and return "Error: Input strings cannot contain numbers" if it does.
"""

def concatenate_strings(string1, string2):
    string1 = string1.strip()
    string2 = string2.strip()

    if string1 == "" or string2 == "":
        return "Error: Input strings cannot be empty"

    concatenated_string = string1 + string2

    if any(char.isdigit() for char in concatenated_string):
        return "Error: Input strings cannot contain numbers"

    return concatenated_string