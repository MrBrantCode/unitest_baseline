"""
QUESTION:
Create a function `reverse_and_check_anagram` that takes a word as input and returns the word with its characters reversed, along with a boolean indicating whether the reversed word has the same character frequency distribution as the original word. The function should handle case sensitivity and any characters in the input word.
"""

def reverse_and_check_anagram(word):
    # Reverse the word
    reversed_word = word[::-1]
    
    # Create frequency distribution of characters in the original and reversed word
    original_freq = {}
    for char in word:
        if char in original_freq:
            original_freq[char] += 1
        else:
            original_freq[char] = 1
            
    reversed_freq = {}
    for char in reversed_word:
        if char in reversed_freq:
            reversed_freq[char] += 1
        else:
            reversed_freq[char] = 1
            
    # Check if the frequency distributions are the same
    is_anagram = original_freq == reversed_freq
    
    return reversed_word, is_anagram