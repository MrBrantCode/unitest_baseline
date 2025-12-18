"""
QUESTION:
Write a function `replace_in_string(text, original_char, replace_char, length_threshold)` that replaces all occurrences of `original_char` with `replace_char` in the string `text` if the length of `text` is greater than `length_threshold`. If the length of `text` is less than or equal to `length_threshold`, return the original string. The function should return the modified string or the original string based on the length condition.
"""

def replace_in_string(text, original_char, replace_char, length_threshold):
    if len(text) > length_threshold:
        return text.replace(original_char, replace_char)
    else:
        return text