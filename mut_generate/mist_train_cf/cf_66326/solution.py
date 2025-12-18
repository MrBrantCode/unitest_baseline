"""
QUESTION:
Create a function `rot13_coder_decoder(string)` that takes an input string and returns the encoded or decoded string using the ROT13 substitution cipher method. The function should handle both upper and lowercase letters, and maintain non-alphabetical characters unchanged.
"""

def rot13_coder_decoder(string):
    result = ""

    for letter in string:
        unicode = ord(letter)
        if unicode >= ord('a') and unicode <= ord('z'):
            if unicode > ord('m'):
                unicode -= 13
            else:
                unicode += 13
        elif unicode >= ord('A') and unicode <= ord('Z'):
            if unicode > ord('M'):
                unicode -= 13
            else:
                unicode += 13
                
        result += chr(unicode)
        
    return result