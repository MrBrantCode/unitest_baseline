"""
QUESTION:
Design a function `firstNonRepeat(string)` that finds the index of the first non-repeating alphanumeric character in a given string. Ignore non-alphanumeric characters and return -1 if all alphanumeric characters are repeating. The function should not use any in-built Python functions for string manipulation.
"""

def firstNonRepeat(string):
    size = len(string)
    count = [0] * 256
    
    # In first traversal, count all characters
    for i in range(size):
        if string[i].isalnum():
            count[ord(string[i])]+=1;
            
    # In second traversal, check if current character is present once 
    # Only non-repeated alphanumeric character will return a positive value
    for i in range(size):
        if(string[i].isalnum() and count[ord(string[i])]==1):
            return i
            
    return -1