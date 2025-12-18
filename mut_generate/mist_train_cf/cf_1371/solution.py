"""
QUESTION:
Create a function `check_unique_characters` that takes a string as input and returns a boolean indicating whether the string contains only unique characters and a dictionary with the count of each unique character in the string. The function should not use any additional data structures that provide constant time complexity lookups, built-in library functions, and should have a time complexity of O(n^2).
"""

def check_unique_characters(string):
    count = {}
    unique_count = 0
    
    for char in string:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
            unique_count += 1
            
    for char in count:
        if count[char] > 1:
            return False, count
        
    return True, count