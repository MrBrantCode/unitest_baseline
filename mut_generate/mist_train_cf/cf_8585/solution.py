"""
QUESTION:
Create a function named `check_unique` that takes a string of lowercase alphabets as input, checks if all characters are unique, and returns True if they are, False otherwise. The string length is at most 10^6 characters. The function should also check for duplicate substrings of length greater than 3 and return False if any are found. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string.
"""

def check_unique(string):
    if len(string) > 10**6: 
        return False

    character_set = set() 
    start = 0 
    end = 0 

    while end < len(string):
        if end - start > 2 and string[start:end+1] in string[end+1:]:
            return False
        
        if string[end] in character_set:
            return False
        
        character_set.add(string[end]) 
        end += 1

        if end == len(string):
            start += 1
            end = start
            character_set = set()

    return True