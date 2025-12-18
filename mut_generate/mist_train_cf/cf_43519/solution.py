"""
QUESTION:
Create a function `transmute_string` that takes two parameters: a string `s` and a language `language`. The function should convert all uppercase letters in `s` to lowercase, replace numerals with their word equivalents in the specified language, and replace decimal points with their word equivalents in the specified language. The function should return the modified string.

For example, if the input string is "Hello World 123" and the language is "Spanish", the function should return a string where "Hello World" is in lowercase, "123" is replaced with "uno dos tres", and decimal points are replaced with "punto".

The function should support multiple languages.
"""

def transmute_string(s, language):
    lang_dict = {
        "Spanish": {
            "0": "cero",
            "1": "uno",
            "2": "dos",
            "3": "tres",
            "4": "cuatro",
            "5": "cinco",
            "6": "seis",
            "7": "siete",
            "8": "ocho",
            "9": "nueve",
            ".": "punto"
        },
        # Add more languages here...
    }

    numerals = lang_dict[language]
    
    s = s.lower()
    new_s = ''
    for c in s:
        if c.isdigit() or c == '.':
            new_s += numerals[c] + ' '
        else:
            new_s += c

    return new_s.rstrip()