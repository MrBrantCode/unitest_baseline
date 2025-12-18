"""
QUESTION:
Design a function called `to_braille` that takes a string of lowercase English letters as input and returns a string representing the Braille translation of the input, where each Braille character is represented as a 6-digit binary number and separated by a space. The function should use the standard Braille alphabet mapping for letters 'a' to 'z'.
"""

def to_braille(text):
    """Converts the inputted text into Braille"""
    braille_alphabet = {
        'a':'100000', 'b':'110000', 'c':'100100', 
        'd':'100110', 'e':'100010', 'f':'110100', 
        'g':'110110', 'h':'110010', 'i':'010100', 
        'j':'010110', 'k':'101000', 'l':'111000', 
        'm':'101100', 'n':'101110', 'o':'101010', 
        'p':'111100', 'q':'111110', 'r':'111010', 
        's':'011100', 't':'011110', 'u':'101001', 
        'v':'111001', 'w':'010111', 'x':'101101', 
        'y':'101111', 'z':'101011'}
    
    return ' '.join([braille_alphabet[char] for char in text])