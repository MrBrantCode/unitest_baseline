"""
QUESTION:
Write a function named `find_longest_word` that takes two parameters: a list of words (`dictionary`) and a string of characters (`characters`). The function should return the longest word from `dictionary` that can be formed using the characters in `characters`, considering that each character in `characters` can be used multiple times. The function should be case-insensitive and have a time complexity of O(n), where n is the length of `dictionary`.
"""

def find_longest_word(dictionary, characters):
    characters = characters.lower()
    longest_word = ""
    
    for word in dictionary:
        word = word.lower()
        valid = True
        char_count = {}
        
        for char in word:
            if char not in characters or char_count.get(char, 0) >= characters.count(char):
                valid = False
                break
            char_count[char] = char_count.get(char, 0) + 1
        
        if valid and len(word) > len(longest_word):
            longest_word = word
    
    return longest_word