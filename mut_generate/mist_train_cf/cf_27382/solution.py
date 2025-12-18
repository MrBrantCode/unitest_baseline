"""
QUESTION:
Implement a function `get_east_asian_width_count` that takes a string `text` as input and returns the number of East Asian wide characters in the text. A character is considered East Asian wide if it occupies two columns in a fixed-width text display, such as Chinese, Japanese, and Korean characters.
"""

def get_east_asian_width_count(text: str) -> int:
    count = 0
    for char in text:
        if ord('\uFF61') <= ord(char) <= ord('\uFF9F') or \
           ord('\u3040') <= ord(char) <= ord('\u309f') or \
           ord('\u30A0') <= ord(char) <= ord('\u30FF') or \
           ord('\u31F0') <= ord(char) <= ord('\u31FF') or \
           ord('\uFF10') <= ord(char) <= ord('\uFF19') or \
           ord('\uFF21') <= ord(char) <= ord('\uFF3A') or \
           ord('\uFF41') <= ord(char) <= ord('\uFF5A') or \
           ord('\uFF66') <= ord(char) <= ord('\uFF9D') or \
           ord('\u4E00') <= ord(char) <= ord('\u9FFF') or \
           ord('\u3400') <= ord(char) <= ord('\u4DBF'):
            count += 1
    return count