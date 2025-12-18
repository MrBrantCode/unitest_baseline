"""
QUESTION:
Create a function named `third_from_end` that takes a string as input. The function should return the character that is third from the end of the string, disregarding whitespace and punctuation. If the string has less than three alphabetic characters, the function should return the message 'There are less than three alphabetic characters in the string.'
"""

def third_from_end(txt):
    # Remove punctuation and spaces
    processed = ''.join(c for c in txt if c.isalpha())
    
    # Check for insufficient characters
    if len(processed) < 3:
        return 'There are less than three alphabetic characters in the string.'
    
    # Return the third character from the end
    return processed[-3]