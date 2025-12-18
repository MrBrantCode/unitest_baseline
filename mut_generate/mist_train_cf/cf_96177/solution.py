"""
QUESTION:
Write a function `find_longest_word(dictionary, characters)` that finds the longest word in the given dictionary that can be constructed from the given set of characters. The characters in the set can be used multiple times to construct the word. The function should handle the case-insensitivity of the characters in the set and dictionary. The time complexity of the solution should be O(n), where n is the length of the dictionary.
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