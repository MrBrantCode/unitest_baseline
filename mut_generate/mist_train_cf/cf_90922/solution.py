"""
QUESTION:
Implement a function `replace_string(text, old, new)` that replaces every occurrence of `old` in `text` with `new` while preserving the original case of the letters. The function should handle multiple occurrences of `old` in `text`. Assume `text`, `old`, and `new` are non-empty strings.
"""

def replace_string(text, old, new):
    """
    Replaces every occurrence of `old` in `text` with `new` while preserving the original case of the letters.

    Args:
        text (str): The input string in which to replace occurrences of `old`.
        old (str): The substring to replace in `text`.
        new (str): The string to replace `old` with.

    Returns:
        str: The modified string with all occurrences of `old` replaced by `new`.
    """
    result = ''
    i = 0
    while i < len(text):
        if text[i:i+len(old)].lower() == old.lower():
            result += new
            i += len(old)
        else:
            result += text[i]
            i += 1
    return result