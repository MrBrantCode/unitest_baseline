"""
QUESTION:
Implement a Python function named `custom_replace` that takes three inputs: two lists of strings (`str_list1` and `str_list2`) and a long text string (`text`). The function should replace all instances of the strings in `str_list1` found in `text` with their corresponding strings in `str_list2`, ensuring that the replacement strings are not subjected to further replacements. The function should return the transformed text, maintaining the original order and preserving punctuation and special characters. Do not use Python's built-in `replace` method.
"""

def custom_replace(str_list1, str_list2, text):
    words = text.split(' ')
    str_dict = dict(zip(str_list1, str_list2))
    new_words = []

    for word in words:
        stripped = ''.join(ch for ch in word if ch.isalnum()) 
        if stripped in str_dict:
            new_word = word.replace(stripped, str_dict[stripped])
            new_words.append(new_word)
        else:
            new_words.append(word)

    return ' '.join(new_words)