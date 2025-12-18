"""
QUESTION:
Create a function `color_string` that takes a string `s` as input and returns the string with the word "apple" in blue font color and the words "blue" and "school" in black font color using ANSI escape codes. Do not use any external libraries or modules. The function should support any input string.
"""

def color_string(s):
    # Define ANSI escape codes for color formatting
    BLUE = '\033[34m'
    BLACK = '\033[0m'

    # Split input string into words
    words = s.split()
    
    # Initialize output string
    output_str = ""

    # Loop through words and format them based on their value
    for word in words:
        if word == "apple":
            output_str += BLUE + word + BLACK + " "
        elif word == "blue" or word == "school":
            output_str += BLACK + word + BLACK + " "
        else:
            output_str += word + " "
    
    # Return formatted string
    return output_str