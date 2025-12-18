"""
QUESTION:
Create a function `check_unique_characters` that takes a string as input and returns a boolean indicating whether the string contains only unique characters and a dictionary containing the count of each unique character in the string. The function should not use any additional built-in data structures besides a dictionary, and its time complexity should be O(n^2). The input string can contain both lowercase and uppercase alphabets, as well as special characters.
"""

def check_unique_characters(string):
    count = {}
    
    for char in string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
            
    for char in count:
        if count[char] > 1:
            return False, count
        
    return True, count