"""
QUESTION:
Create a function `contains_all_letters` that takes a string `s` as input and returns a boolean indicating whether the string contains all 26 lowercase and uppercase letters of the English alphabet. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1).
"""

def contains_all_letters(s):
    letters = [False] * 26
    
    for char in s:
        if 'a' <= char <= 'z':
            letters[ord(char) - ord('a')] = True
        elif 'A' <= char <= 'Z':
            letters[ord(char) - ord('A')] = True
    
    return all(letters)