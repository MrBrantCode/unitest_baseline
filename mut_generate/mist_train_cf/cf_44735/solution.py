"""
QUESTION:
Write a Python function `reverse_sentences(text)` that takes a string of multiple English sentences as input, reverses the order of words in each sentence individually, and returns the resulting string. The reversal operation should preserve the punctuation marks that define different sentences, which are full stops, question marks, or exclamations. Do not use any predefined reverse function in Python.
"""

def reverse_sentences(text):
    punctuation = '.!?'
    sentences = []
    start = 0

    for i in range(len(text)):
        if text[i] in punctuation:
            sentences.append(text[start:i+1].strip())
            start = i+1

    output = ''

    for sentence in sentences:
        words = sentence[:-1].split()
        reverse_sentence = ' '.join(word for word in words[::-1])
        output += reverse_sentence + sentence[-1] + ' '

    return output.strip()