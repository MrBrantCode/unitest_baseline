"""
QUESTION:
Create a function `is_unique(string)` that takes a string of lowercase alphabets as input and checks if all characters are unique without using any additional data structures. The function should have a time complexity of O(n^2) and not use any built-in library functions. The function should return a boolean indicating whether the string contains only unique characters and a dictionary with the count of each unique character in the string.
"""

def is_unique(string):
    count = {}
    for i in range(len(string)):
        char = string[i]
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    unique = True
    for i in range(len(string)):
        char = string[i]
        if count[char] > 1:
            unique = False
            break
    
    return unique, count