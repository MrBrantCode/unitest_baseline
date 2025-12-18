"""
QUESTION:
Write a function `remove_string` that takes two parameters: `string_to_remove` and `string_to_modify`. The function should remove all occurrences of `string_to_remove` from `string_to_modify`, ignoring case sensitivity. If `string_to_remove` is found within another word in `string_to_modify`, it should also be removed. The function should return the modified string.
"""

def remove_string(string_to_remove, string_to_modify):
    lowercase_remove = string_to_remove.lower()
    lowercase_modify = string_to_modify.lower()
    modified_words = [word.replace(lowercase_remove, "") if lowercase_remove in word else word for word in lowercase_modify.split()]
    modified_string = " ".join(modified_words)
    return modified_string