"""
QUESTION:
Design a function `get_longest_word` that takes an array of strings as input and returns the longest word from the array, considering each string can contain special characters and whitespace. The function should not use any built-in functions or libraries to find the longest word. The time complexity should be O(n), where n is the total number of characters in all the strings combined.
"""

def entrance(strings):
    longest_word = ""
    current_word = ""
    
    for string in strings:
        for char in string:
            if char.isalnum() or char.isspace():
                current_word += char
            elif current_word:
                if len(current_word) > len(longest_word):
                    longest_word = current_word
                current_word = ""
        
        if current_word and len(current_word) > len(longest_word):
            longest_word = current_word
        current_word = ""
    
    return longest_word