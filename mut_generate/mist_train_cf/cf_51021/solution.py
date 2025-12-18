"""
QUESTION:
Implement a function `translate(sentence)` that takes a string `sentence` as input and returns its translation based on a predefined codebook. The codebook is a dictionary where keys are unique symbols and values are their corresponding meanings. If a symbol in the input sentence is not found in the codebook, the function should return an error message.
"""

def translate(sentence):
    codebook = {'^': 'apple', '&': 'dog', '$': 'cat', '#': 'car', '@': 'house', '%': 'tree',
                '*': 'phone', '+': 'book', '=': 'pen', '!': 'shirt', '?': 'shoes', '<': 'sky',
                '>': 'moon', '[': 'sun', ']': 'star'}
    
    translation = ''
    for char in sentence:
        if char in codebook:
            translation += codebook[char] + ' '
        else:
            return f"Error: '{char}' does not exist in the codebook."
    return translation