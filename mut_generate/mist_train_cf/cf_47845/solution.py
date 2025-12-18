"""
QUESTION:
Create a function called `process_sentence` that takes a string input. The function should extract only alphanumeric characters from the input, reverse their order, and replace vowels with corresponding digits (a/A=1, e/E=2, i/I=3, o/O=4, u/U=5) in a case-insensitive manner. The function should return the modified string.
"""

def process_sentence(sentence):
    sentence = ''.join(ch for ch in sentence if ch.isalnum()) 
    sentence = sentence[::-1]
    table = str.maketrans('aeiouAEIOU', '1234512345')
    sentence = sentence.translate(table)
    return sentence