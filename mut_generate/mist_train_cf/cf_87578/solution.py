"""
QUESTION:
Write a function called `last_index` that takes a string and a character as input and returns the index of the last occurrence of the character in the string. The function should have a time complexity of O(n), where n is the length of the string, and should not use any built-in Python methods that directly solve this problem. If the character is not found in the string, return -1.
"""

def last_index(string, char):
    index = -1  
    for i in range(len(string)):
        if string[i] == char:
            index = i  
    return index