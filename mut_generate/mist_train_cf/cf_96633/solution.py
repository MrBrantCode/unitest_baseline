"""
QUESTION:
Write a function `longest_word_length(string)` that takes a string as input and returns the length of the longest word that can be formed by rearranging the characters of the string. The function should have a time complexity of O(n log n), where n is the length of the string.
"""

def longest_word_length(string):
    characters = sorted(list(string))
    
    max_length = 0
    current_length = 1
    
    for i in range(1, len(characters)):
        if characters[i] == characters[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
    
    max_length = max(max_length, current_length)
    
    return max_length