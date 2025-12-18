"""
QUESTION:
Write a function `replace_with_dict(input_string, replacements)` that replaces occurrences of keys in `input_string` with their corresponding values from the `replacements` dictionary. The function should correctly handle special characters with diacritics or modifiers and consider the length of each key. 

The `input_string` is a string containing characters to be replaced, and the `replacements` is a dictionary containing key-value pairs for replacements. The function should return the input string after performing the replacements.
"""

def replace_with_dict(input_string, replacements):
    result = input_string
    sorted_replacements = sorted(replacements, key=len, reverse=True)  # Sort keys by length in descending order

    for key in sorted_replacements:
        if key in result:
            value = replacements[key]
            key_length = len(key)
            start_index = 0
            while start_index < len(result):
                index = result.find(key, start_index)
                if index == -1:
                    break
                result = result[:index] + value + result[index + key_length:]
                start_index = index + len(value)  # Move start_index to the end of the replacement value
    return result