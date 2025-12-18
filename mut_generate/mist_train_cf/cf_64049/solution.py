"""
QUESTION:
Create a function `translate_to_french` that translates English letters to their corresponding French letters using a dictionary mapping system. The function should take a string of English letters as input and return the translated string of French letters. The translation should be case-insensitive. If the input string contains characters that are not in the dictionary, the function should append these characters to the result string as-is.
"""

eng_to_french = {
                'a':'a',
                'b':'b',
                'c':'c',
                'd':'d',
                'e':'e',
                'f':'f',
                'g':'g',
                'h':'h',
                'i':'i',
                'j':'j',
                'k':'k',
                'l':'l',
                'm':'m',
                'n':'n',
                'o':'o',
                'p':'p',
                'q':'q',
                'r':'r',
                's':'s',
                't':'t',
                'u':'u',
                'v':'v',
                'w':'w',
                'x':'x',
                'y':'y',
                'z':'z',
                }

def translate_to_french(word):
    french_word = ""
    for char in word:
        if char.isalpha():
            french_char = eng_to_french.get(char.lower())
            if french_char:
                french_word += french_char if char.islower() else french_char.upper()
            else:
                french_word += char
        else:
            french_word += char
    return french_word