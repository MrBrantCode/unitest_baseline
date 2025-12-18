"""
QUESTION:
Write a function `replace_character(s, c, r)` that replaces all instances of a given character `c` with another character `r` in a string `s`, while maintaining the original case sensitivity of the characters. However, the replacement should only occur when `c` is not within a word, where a word is defined as a sequence of characters separated by spaces or punctuation marks.
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