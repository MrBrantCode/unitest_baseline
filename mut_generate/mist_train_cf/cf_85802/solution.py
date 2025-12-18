"""
QUESTION:
Design a function `replace_and_reverse` that takes a string `text`, a list of alphanumeric and special characters `symbols`, and a list of replacement characters `replacements`, and returns the modified string after replacing the specified symbols with the corresponding replacement characters and reversing the resulting string. The function should maintain case sensitivity and accommodate large strings (over 1GB) efficiently. The order of replacement should be maintained, i.e., the first symbol in `symbols` should be replaced by the first character in `replacements`, the second symbol by the second replacement character, and so on.
"""

def replace_and_reverse(text, symbols, replacements):
    trans = str.maketrans(''.join(symbols), ''.join(replacements))
    return text.translate(trans)[::-1]