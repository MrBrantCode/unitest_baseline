"""
QUESTION:
Write a function `remove_elements_and_repeats(text)` that takes a string `text` as input, converts it to lowercase, and returns a string with all vowels, numerical digits, and punctuation symbols removed, and no duplicate consonants. The remaining consonants should appear in their original order in the string.
"""

def remove_elements_and_repeats(text):
    text = text.lower()
    vowels = ['a','e','i','o','u']
    consonants = [chr(c) for c in range(ord('a'), ord('z')+1) if chr(c) not in vowels ]
    symbols = [
        ",", ".", "!", "@", "#", "$", 
        "%", "^", "&", "*", "(", ")", 
        "-", "_", "+", "=", "{", "}", 
        "[", "]", ":", ";", "\"", "\'", 
        "<", ">", "/", "?", "~", "`", 
        "|", " ", "0", "1", "2", "3", 
        "4","5", "6", "7", "8", "9", "\\"
    ]
    removal_list = vowels + symbols
    for removal in removal_list:
        text = text.replace(removal,'')
    
    return ''.join(sorted(set(text), key=text.index))