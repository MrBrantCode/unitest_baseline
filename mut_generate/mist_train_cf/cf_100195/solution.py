"""
QUESTION:
Create a function named "convertToBold" that takes a string "text" as input and returns a string where all alphanumeric characters (both uppercase and lowercase letters, and numbers) are converted to their bold equivalents. The function should not modify non-alphanumeric characters.
"""

def convertToBold(text):
    result = ""
    for char in text:
        if not char.isalnum():
            result += char
            continue
        
        if char.islower():
            char = char.upper()
        
        bold_char = chr(ord(char) + 120419)
        result += bold_char
    
    return result