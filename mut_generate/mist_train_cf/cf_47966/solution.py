"""
QUESTION:
Write a function `convert_list_to_string` that takes a list of words as input and returns a single string where the words are separated by a comma and a space. The function should not use the built-in `join()` function. The input list will only contain strings.
"""

def convert_list_to_string(word_list):
    str_converted = ''
    for word in word_list:
        str_converted += word + ', '
    str_converted = str_converted[:-2]
    return str_converted