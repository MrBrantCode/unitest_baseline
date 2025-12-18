"""
QUESTION:
Write a function `replace_character(s, c, r)` that takes in a string `s`, a character `c`, and a replacement character `r`. Replace all instances of `c` in `s` with `r`, while maintaining the original case sensitivity of the characters. However, do not replace `c` if it is within a word (defined as a sequence of characters separated by spaces or punctuation marks).
"""

def replace_character(s, c, r):
    words = s.split()
    new_words = []
    
    for word in words:
        if c not in word:
            new_words.append(word)
        else:
            new_word = ''
            i = 0
            while i < len(word):
                if word[i] == c:
                    new_word += r
                    i += 1
                    while i < len(word) and not word[i].isalpha():
                        new_word += word[i]
                        i += 1
                else:
                    new_word += word[i]
                    i += 1
            new_words.append(new_word)
    
    return ' '.join(new_words)