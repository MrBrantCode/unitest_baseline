"""
QUESTION:
Create a function `is_ambigram` that takes an alphanumeric string as input and returns a boolean value indicating whether the string could potentially be a simple rotational (180 degree) ambigram when visualized. The function should ignore font, styling, case-sensitivity, and other visual design elements. It should consider a limited set of characters that can form ambigrams when rotated 180 degrees.
"""

def is_ambigram(input_string):
    ambigram_chars = {'h':'y', 'n':'u', 's':'s', 'z':'z', 'x':'x', 'o':'o', 'p':'q', 'b':'d', 'd':'p', 'q':'b', 'u':'n', 'y':'h', 'i':'i', '1':'1', '0':'0', '8':'8'}
    
    input_string = input_string.lower()
    reversed_string = input_string[::-1]
    
    for i in range(len(input_string)):
        if input_string[i] not in ambigram_chars or ambigram_chars[input_string[i]] != reversed_string[i]:
            return False
    
    return True