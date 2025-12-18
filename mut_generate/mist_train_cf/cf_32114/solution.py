"""
QUESTION:
The `replace_name` function takes a string as input, where the string contains a placeholder "<NAME>" and a player's name surrounded by "#" symbols. The function should replace the "<NAME>" placeholder with the actual player's name and return the modified string. If no player name is found in the input string, the function should return a message indicating that no player name was found.
"""

import re

def entrance(text):
    match = re.search(r'#(.*?)#', text)
    if match:
        name = match.group(1)
        modified_text = text.replace('<NAME>', name)
        return modified_text
    else:
        return "No player name found in the text."