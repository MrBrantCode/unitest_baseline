"""
QUESTION:
# Introduction 

The ragbaby cipher is a substitution cipher that encodes/decodes a text using a keyed alphabet and their position in the plaintext word they are a part of.

To encrypt the text `This is an example.` with the key `cipher`, first construct a keyed alphabet:
```
c       i       p       h       e       r       a       b       d       f       g       j       k       l       m       n       o       q       s       t       u       v       w       x       y       z
```

Then, number the letters in the text as follows:
```
T       h       i       s               i       s               a       n               e       x       a       m       p       l       e       .
1       2       3       4               1       2               1       2               1       2       3       4       5       6       7        
```

To obtain the encoded text, replace each character of the word with the letter in the keyed alphabet the corresponding number of places to the right of it (wrapping if necessary). 
Non-alphabetic characters are preserved to mark word boundaries.

Our ciphertext is then `Urew pu bq rzfsbtj.`

# Task

Wirate functions `encode` and `decode` which accept 2 parameters:
- `text` - string - a text to encode/decode
- `key` -  string - a key

# Notes

- handle lower and upper case in `text` string
- `key` consists of only lowercase characters
"""

from string import ascii_lowercase as aLow
import re

def ragbaby_cipher(text: str, key: str, mode: str) -> str:
    """
    Encodes or decodes a text using the Ragbaby cipher with the given key.

    Parameters:
    - text (str): The text to be encoded or decoded.
    - key (str): The key used to construct the keyed alphabet.
    - mode (str): The mode of operation, either "encode" or "decode".

    Returns:
    - str: The encoded or decoded text.
    """
    if mode not in ["encode", "decode"]:
        raise ValueError("Mode must be either 'encode' or 'decode'")
    
    d = 1 if mode == "encode" else -1
    
    remains = set(aLow)
    alpha = []
    for c in key + aLow:
        if c in remains:
            remains.remove(c)
            alpha.append(c)
    alpha = ''.join(alpha)
    dct = {c: i for i, c in enumerate(alpha)}
    
    def rotateWord(w, alpha, dct, d):
        lst = []
        for i, c in enumerate(w.lower(), 1):
            transChar = alpha[(dct[c] + i * d) % 26]
            if w[i - 1].isupper():
                transChar = transChar.upper()
            lst.append(transChar)
        return ''.join(lst)
    
    return re.sub('[a-zA-Z]+', lambda m: rotateWord(m.group(), alpha, dct, d), text)