"""
QUESTION:
Create a function `format_text` that takes in a string `text` and a list of `formatting_options`, and returns the formatted text. The formatting options are represented as strings and can include the following: "blinkRapid", "inverse", "conceal", "crossedOut", "black", "red", "green". The function should apply the formatting options to the input string in the order they appear in the list. If the same option is specified multiple times, it should be applied each time it appears. The function should use ANSI escape codes for formatting.
"""

def format_text(text, formatting_options):
    formatting_codes = {
        "blinkRapid": "\033[6m",
        "inverse": "\033[7m",
        "conceal": "\033[8m",
        "crossedOut": "\033[9m",
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m"
    }
    
    formatted_text = ""
    for option in formatting_options:
        if option in formatting_codes:
            formatted_text += formatting_codes[option]
    
    formatted_text += text + "\033[0m"
    return formatted_text