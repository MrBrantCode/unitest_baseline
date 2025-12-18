"""
QUESTION:
Create a function named 'is_unique' that takes a string of lowercase alphabets as input and returns a boolean indicating whether the string contains only unique characters along with a dictionary containing the count of each unique character. The function should have a time complexity of O(n^2) and must not use any additional data structures or built-in library functions.
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