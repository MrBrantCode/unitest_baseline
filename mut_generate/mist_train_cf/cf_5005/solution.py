"""
QUESTION:
Create a function named `encrypt` that takes three parameters: `text`, `shift`, and `vowels`. The function should reverse the input `text`, then for each character, if the previous character is in `vowels` and its ASCII value is odd, shift the current character by the ASCII value of the previous character. If the previous character is not in `vowels` or its ASCII value is even, do not shift the current character. The function should return the encrypted text as a string.
"""

def entrance(text, shift, vowels):
    encrypted_text = ""
    reversed_text = text[::-1]
    
    for i, letter in enumerate(reversed_text):
        if i > 0 and reversed_text[i-1] in vowels and ord(reversed_text[i-1]) % 2 != 0:
            shifted_letter = chr(ord(letter) + ord(reversed_text[i-1]))
        else:
            shifted_letter = letter
        
        encrypted_text += shifted_letter
    
    return encrypted_text