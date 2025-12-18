"""
QUESTION:
Create a function `rearrange_words_encrypt` that takes in a string `s`, a list of integers `word_order`, and an integer `key`. The function should split the string into words, rearrange them according to the `word_order` list, and then encrypt each word using a Caesar cipher with the given `key`. The function should return a list of encrypted words.

The `word_order` list has the same length as the number of words in the string, and each position in the list corresponds to a new location for the word at that position in the original string. The Caesar cipher should shift each character in the word by the given `key`, wrapping around the alphabet if necessary, and leaving non-alphabetical characters unchanged.
"""

def rearrange_words_encrypt(s, word_order, key):
    words = s.split()
    rearranged = [words[i] for i in word_order]

    encrypted = []
    for word in rearranged:
        new_word = ''.join([chr((ord(char) - 97 + key) % 26 + 97) if 'a' <= char <= 'z' 
                            else chr((ord(char) - 65 + key) % 26 + 65) if 'A' <= char <= 'Z' 
                            else char 
                            for char in word])
        encrypted.append(new_word)
    return encrypted