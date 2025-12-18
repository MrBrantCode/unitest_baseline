"""
QUESTION:
Create a function called `replace_and_count` that takes two parameters: an input string and a dictionary where keys are characters to be replaced and values are their replacements. The function should return the modified string with all replacements made and a dictionary that holds the count of each replaced character.
"""

def replace_and_count(input_str, replace_dict):
    replace_count = {}
    for key, value in replace_dict.items():
        count = input_str.count(key)
        if count > 0:
            input_str = input_str.replace(key, value)
            replace_count[key] = count  # return the original key instead of value in replace_count
    return input_str, replace_count