"""
QUESTION:
Write a function `is_anagram(string, word_list)` that takes a string and a list of words as input. The function should return True if the string is an anagram of a word in the list, and False otherwise. The input list may or may not be alphabetically sorted, but the function should not modify the original list.
"""

def is_anagram(string, word_list):
    # Sort the characters of the string
    sorted_string = sorted(string)
    
    # Iterate through each word in the list
    for word in word_list:
        # Sort the characters of the word
        sorted_word = sorted(word)
        
        # Check if the sorted string is equal to the sorted word
        if sorted_string == sorted_word:
            return True
    
    return False