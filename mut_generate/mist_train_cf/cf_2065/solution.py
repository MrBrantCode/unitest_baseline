"""
QUESTION:
Create a boolean function `check_all_alphabets` that checks whether a given string contains at least one occurrence of each alphabet character, including lowercase and uppercase alphabets, non-ASCII alphabets, and alphabets from non-Latin scripts. The function should have a time complexity of O(n), where n is the length of the string, and should not use any built-in functions or libraries that directly check for alphabet characters.
"""

def check_all_alphabets(string):
    alphabet = [False] * 26

    for char in string:
        char = ord(char)
        
        # Convert lowercase alphabets to uppercase
        if 97 <= char <= 122:
            char -= 32
        
        # Check if the character is an alphabet
        if 65 <= char <= 90:
            alphabet[char - 65] = True
        
        # Check if the character is a non-ASCII alphabet
        elif char >= 128:
            alphabet[25] = True
        
        # Check if all alphabets have been found
        if all(alphabet):
            return True
    
    return False