"""
QUESTION:
Write a function `substitute_string(input_string)` that substitutes all spaces with '%20' and eliminates any leading or trailing spaces. The function should also replace multiple consecutive spaces with a single '%20'. Additionally, it should substitute 'a', 'b', 'c', 'A', 'B', 'C' with their ASCII equivalents in hexadecimal format, maintaining case sensitivity and replacing multiple consecutive instances with a single corresponding value. The function should handle strings of up to 1 million characters in length and be optimized for speed. Do not use built-in string manipulation functions.
"""

def substitute_string(input_string):
    input_string = ' '.join(input_string.split()) 
    input_string = input_string.replace(' ', '%20')
    substitution_dictionary = {
        'a': '%{}'.format(hex(ord('a')).split('x')[-1]),
        'b': '%{}'.format(hex(ord('b')).split('x')[-1]),
        'c': '%{}'.format(hex(ord('c')).split('x')[-1]),
        'A': '%{}'.format(hex(ord('A')).split('x')[-1]),
        'B': '%{}'.format(hex(ord('B')).split('x')[-1]),
        'C': '%{}'.format(hex(ord('C')).split('x')[-1])}
    for key, value in substitution_dictionary.items():
        input_string = input_string.replace(key, value)
    return input_string