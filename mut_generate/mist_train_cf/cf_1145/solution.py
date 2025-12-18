"""
QUESTION:
Write a function named `reverse_string` that takes a string as input and returns the reverse of the string. The function must have a time complexity of O(n), where n is the length of the string, and can only use basic arithmetic operations and bitwise operations. It cannot use built-in string manipulation methods, loops, or recursion (in the string reversal part), additional data structures or variables, slicing or indexing, concatenation or joining of strings. The function must perform the reverse operation in-place.
"""

def reverse_string(string):
    length = len(string)
    
    if length <= 1:
        return string
    
    # Convert string to a list of characters
    string = list(string)
    
    # Swap characters from the beginning and end of the string
    for i in range(length // 2):
        # XOR swap to swap characters in-place
        string[i] = chr(ord(string[i]) ^ ord(string[length - i - 1]))
        string[length - i - 1] = chr(ord(string[i]) ^ ord(string[length - i - 1]))
        string[i] = chr(ord(string[i]) ^ ord(string[length - i - 1]))
    
    # Convert the list of characters back to a string
    string = ''.join(string)
    
    return string