"""
QUESTION:
Design a function `encode_message` and `decode_message` to create a two-layer encrypted communication system with the following requirements:

- The system uses a cipher with a given dictionary (`symbol_phrase_dict`) that maps symbols to unique phrases or idioms.
- The `encode_message` function takes a message and a key as input, replaces each word in the message with its corresponding symbol from the dictionary, and applies a Caesar cipher by shifting the ASCII value of each symbol by the key value.
- The `decode_message` function takes an encoded message and a key as input, reverses the Caesar cipher, and replaces each symbol with its corresponding phrase from the dictionary.
- If a word or symbol is not found in the dictionary, it should be left unchanged in the output.
- The system should use a key-based authentication for the encoding and decoding process.

The dictionary `symbol_phrase_dict` is predefined as:
```python
symbol_phrase_dict = {
    '!': 'apple',
    '@': 'banana',
    '#': 'cat',
    '$': 'dog',
    '%': 'egg',
    '^': 'fish',
    '&': 'grape',
    '*': 'hat',
    '(': 'ice',
    ')': 'juice'
}
```
"""

# Define your symbol – phrase dictionary
symbol_phrase_dict = {
    '!': 'apple',
    '@': 'banana',
    '#': 'cat',
    '$': 'dog',
    '%': 'egg',
    '^': 'fish',
    '&': 'grape',
    '*': 'hat',
    '(': 'ice',
    ')': 'juice'
}

# Reverse dictionary for decryption
phrase_symbol_dict = {v: k for k, v in symbol_phrase_dict.items()}

# Function to encode
def encode_message(message, key):
    encoded = ""
    words = message.split(' ')
    for word in words:
        if word in phrase_symbol_dict:
            encoded += chr(ord(phrase_symbol_dict[word]) + key)
        else:
            encoded += word    # if the word not in dictionary, keep it
    return encoded

# Function to decode
def decode_message(message, key):
    decoded = ""
    for symbol in message:
        if chr(ord(symbol) - key) in symbol_phrase_dict:
            decoded += symbol_phrase_dict[chr(ord(symbol) - key)] + ' '
        else:
            decoded += symbol    # if the symbol not in dictionary, keep it
    return decoded.strip()    # remove the trailing space