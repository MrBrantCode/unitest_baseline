"""
QUESTION:
Create a function `replace_punctuation` that takes a string as input and replaces all punctuation marks with a space, then removes any consecutive spaces resulting from the replacement. The input string can have a maximum length of 10^6 characters. The function should have a time complexity of O(n), where n is the length of the input string, and should not use any built-in string manipulation functions such as `replace()` or `regex`.
"""

def replace_punctuation(string):
    punctuation_marks = {'.', ',', '!', '-', '...', '—', '–', '(', ')', '[', ']', '{', '}', ':', ';', '?', '/', '\\'}
    string_list = list(string)
    for i in range(len(string_list)):
        if string_list[i] in punctuation_marks:
            string_list[i] = ' '
    new_string = ''.join(string_list)
    new_string = ' '.join(new_string.split())
    return new_string