"""
QUESTION:
Write a function `count_occurrences(string, characters)` that takes a string and a list of characters as input and returns the total count of occurrences of all characters in the string, ignoring case sensitivity. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def count_occurrences(string, characters):
    string = string.lower()
    characters = [ch.lower() for ch in characters]
    
    count = 0
    for ch in characters:
        count += string.count(ch)
    
    return count