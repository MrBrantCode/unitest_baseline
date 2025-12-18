"""
QUESTION:
Implement the function `generate_cryptogram(sentence, shift=3)` to generate a cryptogram from the given sentence by shifting each character in the sentence by a certain amount using the Caesar Cipher encryption algorithm. The function should take two parameters: the input sentence and the shift value (default is 3). The function should preserve the case of the original characters and shift only letters, leaving other characters unchanged.
"""

import string

def generate_cryptogram(sentence, shift=3):
    table = str.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                          string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift] +
                          string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift])
    return sentence.translate(table)