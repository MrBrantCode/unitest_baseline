"""
QUESTION:
Create a boolean function `contains_all_alphabets` that checks whether a given string contains all alphabets, with a time complexity of O(n), where n is the length of the string. The function should not use any built-in functions or libraries that directly check for alphabet characters, and it should only consider lowercase and uppercase alphabets, ignoring case.
"""

def contains_all_alphabets(phrase):
    alphabet_count = [0] * 26  

    for char in phrase:
        if 'a' <= char <= 'z':  
            index = ord(char) - ord('a')
            alphabet_count[index] += 1
        elif 'A' <= char <= 'Z':  
            index = ord(char) - ord('A')
            alphabet_count[index] += 1

    for count in alphabet_count:
        if count == 0:  
            return False

    return True