"""
QUESTION:
Create a function named `reverse_and_check_anagram` that takes a string as input, reverses the string, and checks if the reversed string is an anagram of the original string. The function should not use any external libraries. It should return a tuple containing the reversed string and a boolean indicating whether the reversed string is an anagram of the original string.
"""

def reverse_and_check_anagram(word):
    # Reverse the word
    reversed_word = word[::-1]
    
    # Check if the word is an anagram
    is_anagram = sorted(word) == sorted(reversed_word)

    return (reversed_word, is_anagram)