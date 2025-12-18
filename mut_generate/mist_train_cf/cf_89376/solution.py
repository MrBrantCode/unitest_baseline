"""
QUESTION:
Write a function `replace_character(s, c, r)` that takes in three parameters: a string `s`, a character `c` to be replaced, and a replacement character `r`. The function should replace all instances of `c` with `r` in `s`, while maintaining the original case sensitivity, but only if `c` is not within a word (a sequence of characters separated by spaces or punctuation marks).
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