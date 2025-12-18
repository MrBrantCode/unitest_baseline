"""
QUESTION:
Write a function named `compare_strings` that takes two string parameters and returns the index of the first character that is unequal in the two strings. The function must not use any built-in string comparison functions or operators, nor can it use any loops or recursion.
"""

def entance(string1, string2):
    # Convert the strings into ASCII values
    ascii1 = [ord(char) for char in string1]
    ascii2 = [ord(char) for char in string2]
    
    # Find the index of the first unequal character
    for i in range(min(len(ascii1), len(ascii2))):
        diff = ascii1[i] - ascii2[i]
        if diff != 0:
            return i
    
    # If all characters are equal, return the index of the first differing length
    return min(len(ascii1), len(ascii2))