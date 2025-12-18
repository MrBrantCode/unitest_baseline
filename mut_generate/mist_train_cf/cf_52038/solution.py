"""
QUESTION:
Create a function called 'cipher' that takes a string parameter and returns a ciphered string. The ciphering is done by shifting each alphabetical character three positions ahead in the alphabet (wrapping around to the beginning of the alphabet if necessary), while keeping the case of the characters (upper and lower) and leaving non-alphabetical characters unchanged. The function should work for all characters of the lower case and uppercase English alphabets.
"""

def cipher(s):
    result = ''
    
    for char in s:
        if not char.isalpha():
            result += char
            continue
        
        shifted_char = chr((ord(char.lower()) - 97 + 3) % 26 + 97) if char.islower() else chr((ord(char.upper()) - 65 + 3) % 26 + 65)
        result += shifted_char
    
    return result