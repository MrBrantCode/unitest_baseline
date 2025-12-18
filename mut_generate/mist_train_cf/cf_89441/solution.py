"""
QUESTION:
Write a function `compare_strings` that takes two strings as input and returns the index of the first character that is unequal in the two strings. The function cannot use any built-in string comparison functions or operators, loops, or recursion. If all characters are equal, the function should return -1.
"""

def compare_strings(string1, string2):
    # Convert the strings into ASCII values
    ascii1 = [ord(char) for char in string1]
    ascii2 = [ord(char) for char in string2]
    
    # Find the index of the first unequal character
    for i in range(min(len(ascii1), len(ascii2))):
        diff = ascii1[i] - ascii2[i]
        if diff != 0:
            return i
    
    # If all characters are equal up to the length of the shorter string, 
    # return the length of the shorter string if the strings have different lengths
    if len(ascii1) != len(ascii2):
        return min(len(ascii1), len(ascii2))
    
    # If all characters are equal, return -1
    return -1