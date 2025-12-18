"""
QUESTION:
Create a function called `translate_string` that takes a string `s` and a language `lang` as arguments. The function should translate symbols, numbers, and escape characters in the input string to their corresponding values in the specified language. It should also convert all lowercase characters in the string to uppercase. The function should return the translated string. The translation rules should be defined in the following dictionaries: `symbol_dict` for symbols, `num_dict` for numbers, and `escape_dict` for escape characters.
"""

def translate_string(s, lang):
    symbol_dict = {"A": {"french": "et"}, "@": {"french": "at"}}
    num_dict = {"1": {"french": "un"}, "2": {"french": "deux"}, "3": {"french": "trois"}, "4": {"french": "quatre"}, "5": {"french": "cinq"}, "6": {"french": "six"}, "7": {"french": "sept"}, "8": {"french": "huit"},"9": {"french": "neuf"}, "0": {"french": "zero"}}
    escape_dict = {"\n": "newline"}

    trans = str.maketrans(string.ascii_lowercase, string.ascii_uppercase)
    res = ''
    for char in s:
        if char in string.ascii_lowercase:
            res += char.translate(trans)
        elif char in symbol_dict.keys():
            res += symbol_dict[char][lang]
        elif char in num_dict.keys():
            res += num_dict[char][lang]
        elif char in escape_dict.keys():
            res += escape_dict[char]
        else:
            res += char
    return res