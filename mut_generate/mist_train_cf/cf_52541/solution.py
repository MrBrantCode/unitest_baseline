"""
QUESTION:
Develop a function called `alphabetic_rearrangement` that takes a string as input, rearranges its alphabetic characters in alphabetical order (ignoring non-alphabetic characters and case sensitivity), and returns the rearranged string along with a dictionary containing the count of each alphabetic character.
"""

def alphabetic_rearrangement(string):
    frequency_map = {}
    sorted_string = ''
    
    for c in string:
        if c.isalpha():  
            c = c.lower()  
            if c not in frequency_map:
                frequency_map[c] = 1
            else:
                frequency_map[c] += 1
                
    for char_code in range(ord('a'), ord('z')+1):  
        char = chr(char_code)
        if char in frequency_map:
            sorted_string += char * frequency_map[char]
            
    return sorted_string, frequency_map