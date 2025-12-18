"""
QUESTION:
Create a function named `detect_whitespace` that takes an input string and returns a dictionary containing the count of different types of Unicode whitespace characters in the input string. The function should identify and classify the whitespace characters by their types (`\t`, `\n`, `\u00A0`, etc.). The dictionary should have the whitespace type as the key and the count as the value. The function should support the following whitespace types: tab (`\t`), newline (`\n`), space (` `), non-breaking space (`\u00A0`), line separator (`\u2028`), paragraph separator (`\u2029`), em space (`\u2003`), thin space (`\u2009`), and zero-width space (`\u200B`).
"""

import re

def detect_whitespace(input):
    # The different types of unicode whitespace characters we're looking for
    whitespace_types = {
        "TAB": "\t",
        "NEWLINE": "\n",
        "SPACE": " ",
        "NO-BREAK SPACE": "\u00A0",
        "LINE SEPARATOR": "\u2028",
        "PARAGRAPH SEPARATOR": "\u2029",
        "EM SPACE": "\u2003",
        "THIN SPACE": "\u2009",
        "ZERO WIDTH SPACE": "\u200B",
    }

    # Initialize a dictionary to hold the count of each type of whitespace
    whitespace_counts = {name: 0 for name in whitespace_types.keys()}

    # Iterate over each type of whitespace and count their respective occurences in the text
    for name, char in whitespace_types.items():
        whitespace_counts[name] = len(re.findall(char, input))

    return whitespace_counts