"""
QUESTION:
Replace all instances of a given character with another character in a string while maintaining the original case sensitivity, excluding replacements within words. The function `replace_character(s, c, r)` should take in three parameters: the string `s`, the character to be replaced `c`, and the replacement character `r`.
"""

def replace_character(s, c, r):
    words = s.split()
    new_words = []
    for word in words:
        if c in word:
            new_word = ""
            for char in word:
                if char.lower() == c.lower():
                    new_word += r if char.islower() else r.upper()
                else:
                    new_word += char
            new_words.append(new_word)
        else:
            new_words.append(word)
    return " ".join(new_words)