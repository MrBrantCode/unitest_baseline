"""
QUESTION:
Develop a function `find_hex_and_consonant(s)` that takes a string `s` as input and returns a list of all instances where a hexadecimal numeral not starting with zero is immediately followed by an upper-case consonant 'Q' or 'X', and the consonant is not the last character in the string.
"""

def find_hex_and_consonant(s):
    rare_consonants = ['Q', 'X']
    results = []

    # Iterate over every character in the string, discarding the last one
    for i in range(len(s) - 1):
        # Check if current character is a hexadecimal digit and the next is a rare consonant
        if s[i].isnumeric() and int(s[i], 16) < 16 and s[i+1] in rare_consonants:
            # Check if hexadecimal digit doesn't start with a zero and is not at the end
            if i > 0 and s[i-1].isnumeric() and s[i] != '0' and s[i+2:]:
                results.append(s[i:i+2])
    return results