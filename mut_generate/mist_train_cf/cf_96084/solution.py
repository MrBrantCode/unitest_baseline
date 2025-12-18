"""
QUESTION:
Write a function named `cut_string` that takes a string as input, cuts it into substrings every 4 characters, and returns a list of these substrings, excluding any that contain numbers.
"""

def cut_string(input_string):
    substrings = []
    temp_string = ""

    for char in input_string:
        temp_string += char

        if len(temp_string) % 4 == 0:
            if not any(char.isdigit() for char in temp_string):
                substrings.append(temp_string)
                temp_string = ""

    if temp_string != "":
        if not any(char.isdigit() for char in temp_string):
            substrings.append(temp_string)

    return substrings