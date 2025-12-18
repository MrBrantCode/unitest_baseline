"""
QUESTION:
For encrypting strings this region of chars is given (in this order!):

* all letters (ascending, first all UpperCase, then all LowerCase)
* all digits (ascending)
* the following chars: `.,:;-?! '()$%&"` 

These are 77 chars! (This region is zero-based.)

Write two methods: 
```python
def encrypt(text)
def decrypt(encrypted_text)
```

Prechecks:
1. If the input-string has chars, that are not in the region, throw an Exception(C#, Python) or Error(JavaScript).
2. If the input-string is null or empty return exactly this value!

For building the encrypted string:
1. For every second char do a switch of the case.
2. For every char take the index from the region. Take the difference from the region-index of the char before (from the input text! Not from the fresh encrypted char before!). (Char2 = Char1-Char2)
Replace the original char by the char of the difference-value from the region. In this step the first letter of the text is unchanged.
3. Replace the first char by the mirror in the given region. (`'A' -> '"'`, `'B' -> '&'`, ...)

Simple example:

* Input:  `"Business"`
* Step 1: `"BUsInEsS"`
* Step 2: `"B61kujla"`
  * `B -> U`
    * `B (1) - U (20) = -19`
    * `-19 + 77 = 58`
    * `Region[58] = "6"`
  * `U -> s`
    * `U (20) - s (44) = -24`
    * `-24 + 77 = 53`
    * `Region[53] = "1"`
* Step 3: `"&61kujla"`

This kata is part of the Simple Encryption Series:
Simple Encryption #1 - Alternating Split
Simple Encryption #2 - Index-Difference
Simple Encryption #3 - Turn The Bits Around
Simple Encryption #4 - Qwerty

Have fun coding it and please don't forget to vote and rank this kata! :-)
"""

region = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;-?! '()$%&" + '"'

def encrypt(text: str) -> str:
    if not text:
        return text
    
    # Precheck for invalid characters
    if any(char not in region for char in text):
        raise ValueError("Input contains characters not in the defined region.")
    
    letters = list(text)
    
    # Step 1: Switch case for every second character
    for i in range(1, len(letters), 2):
        letters[i] = text[i].swapcase()
    
    swapped = letters[:]
    
    # Step 2: Calculate the difference and replace characters
    for i in range(1, len(letters)):
        letters[i] = region[region.index(swapped[i - 1]) - region.index(swapped[i])]
    
    # Step 3: Replace the first character with its mirror in the region
    letters[0] = region[-(region.index(swapped[0]) + 1)]
    
    return ''.join(letters)

def decrypt(encrypted_text: str) -> str:
    if not encrypted_text:
        return encrypted_text
    
    # Precheck for invalid characters
    if any(char not in region for char in encrypted_text):
        raise ValueError("Input contains characters not in the defined region.")
    
    letters = list(encrypted_text)
    
    # Step 1: Replace the first character with its mirror in the region
    letters[0] = region[-(region.index(letters[0]) + 1)]
    
    # Step 2: Calculate the difference and replace characters
    for i in range(1, len(letters)):
        letters[i] = region[region.index(letters[i - 1]) - region.index(letters[i])]
    
    # Step 3: Switch case for every second character
    for i in range(1, len(letters), 2):
        letters[i] = letters[i].swapcase()
    
    return ''.join(letters)