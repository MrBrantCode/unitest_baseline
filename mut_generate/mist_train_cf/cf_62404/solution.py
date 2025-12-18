"""
QUESTION:
Write a function called `decrypt_rearrange_words` that takes a list of strings `s`, a list of integers `word_order`, and an integer `key` as input. The function should decrypt each string in `s` by shifting each letter by `key` places backwards in the alphabet (wrapping around from 'z' to 'a' or 'Z' to 'A' if necessary), then rearrange the decrypted strings based on the given `word_order`. Non-alphabet characters should remain unchanged. The function should return a string of the rearranged words separated by commas.
"""

def decrypt_rearrange_words(s, word_order, key):
    def decrypt_char(c, key):
        if not c.isalpha():
            return c
        lower_bound = ord('a') if c.islower() else ord('A')
        c_index = ord(c) - lower_bound
        new_c_index = (c_index - key) % 26
        return chr(new_c_index + lower_bound)

    decrypted_words = [''.join(decrypt_char(c, key) for c in word) for word in s]
    word_dict = dict(zip(word_order, decrypted_words))
    ordered_words = [word_dict[i] for i in sorted(word_dict)]
    return ', '.join(ordered_words)