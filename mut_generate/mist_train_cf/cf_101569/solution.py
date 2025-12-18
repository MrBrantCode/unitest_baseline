"""
QUESTION:
Implement a function named `convert_to_chinese` that takes a string as input and returns its corresponding Chinese characters using Unicode. The function should utilize a custom dictionary to map rare or specialized characters that are not found in the Unicode table.
"""

def convert_to_chinese(input_string):
    custom_dict = {'𠮷': 0x20BB7}
    unicode_list = [custom_dict[char] if char in custom_dict else ord(char) for char in input_string]
    return ''.join([chr(char) for char in unicode_list])