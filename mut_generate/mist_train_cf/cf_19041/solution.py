"""
QUESTION:
Write a function `is_anagram(string, word_list)` that checks if the input string is an anagram of any word in the given list. The function should return `True` if an anagram is found and `False` otherwise. The input string and the words in the list are case-sensitive and may contain duplicate characters.
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