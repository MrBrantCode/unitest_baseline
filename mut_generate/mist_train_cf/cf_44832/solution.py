"""
QUESTION:
Create a function named `middle_lexical_unit` that takes two parameters: `text` and `pattern`. The function should return the middle lexical unit from the trio of units in the `text` that matches the `pattern`. The smallest and largest units in the trio should be discarded. In case of a tie, the function should consider the first instance. If the `pattern` does not match any trio in the `text`, the function should return an empty string.
"""

import re

def middle_lexical_unit(text, pattern):
    phrase = re.findall(pattern, text)
    if phrase:
        phrase = phrase[0].split()
        phrase.remove(min(phrase, key=len))
        phrase.remove(max(phrase, key=len))
        return phrase[0]
    else:
        return ''