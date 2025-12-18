"""
QUESTION:
Develop a function named `substitute_with_colon` that takes two parameters: `text` and `special_characters`. This function should replace every instance of characters specified in the `special_characters` list with a colon, while maintaining the original case of alphabets in the text. The function should also handle edge cases where the `text` is null or empty.
"""

import re

def substitute_with_colon(text, special_characters):
    if text == "" or text is None:  
        return text

    pattern = "[" + re.escape("".join(special_characters)) + "]"
    
    text = re.sub(pattern, ":", text)

    return text