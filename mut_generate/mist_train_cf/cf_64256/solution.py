"""
QUESTION:
Create a function named `rot13` that takes a string `s` as input and returns the encoded string using the ROT13 substitution cipher method. The function should shift both uppercase and lowercase English alphabets 13 places. If the shift crosses 'z' or 'Z', it should rotate back to the start of the alphabet. The function should not modify non-alphabet characters.
"""

def rot13(s):
    result = ""
    
    for v in s:
        c = ord(v)
        
        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13
        result += chr(c)
    
    return result