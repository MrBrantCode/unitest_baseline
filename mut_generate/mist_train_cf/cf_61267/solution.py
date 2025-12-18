"""
QUESTION:
Write a function `convert_text_to_hex` that takes a string `text` as input and returns its corresponding hexadecimal value based on ASCII representation as a string. The function should be able to handle strings of up to 10,000 characters and should have a time and space complexity of O(n), where n is the length of the input string.
"""

def convert_text_to_hex(text):
    """
    This function takes a string as input and returns its corresponding hexadecimal value based on ASCII representation as a string.
    
    Time complexity: O(n), where n is the length of the input string.
    Space complexity: O(n), where n is the size of the input.
    
    :param text: Input string to be converted to hexadecimal
    :return: Hexadecimal representation of the input string
    """
    return ''.join(format(ord(ch), '02x') for ch in text)