"""
QUESTION:
Create a function `color_text` that takes a string as input and returns a string with the word "apple" in blue font color, and the words "blue" and "school" in black font color. The function should use ANSI escape codes for color formatting and should not use any external libraries or modules.
"""

def color_text(input_str):
    BLUE = '\033[34m'
    BLACK = '\033[0m'
    words = input_str.split()
    output_str = ""
    for word in words:
        if word == "apple":
            output_str += BLUE + word + BLACK + " "
        elif word == "blue" or word == "school":
            output_str += BLACK + word + BLACK + " "
        else:
            output_str += word + " "
    return output_str.strip()