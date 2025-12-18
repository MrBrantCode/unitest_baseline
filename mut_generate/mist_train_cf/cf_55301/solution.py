"""
QUESTION:
Replace every occurrence of specified characters in a given text with a semicolon character. The function `replace_characters(text, char_list, replace_char=';')` should take as input a string `text`, a list of characters `char_list` to replace, and an optional replacement character `replace_char` (default is ';'). The function should preserve the original case of alphabets in the text, handle edge cases where the text is null or empty, and manage multiple languages and specific characters from different languages efficiently within time and space complexity limits of O(n), where n is the length of the input string.
"""

def replace_characters(text, char_list, replace_char=';'):
    if text is None or len(text) == 0:
        return text
    else:
        text_list = list(text)
        for i in range(len(text_list)):
            if text_list[i] in char_list:
                text_list[i] = replace_char
        return ''.join(text_list)